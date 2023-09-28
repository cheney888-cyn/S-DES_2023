import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QFileDialog
from sdes import SDES
class SDESApp(QWidget):
    def __init__(self):
        super().__init__()
        ASCII= False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('S-DES 加密解密')
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout()

        # 明文输入框
        self.plain_text_label = QLabel('明文或密文 (8位二进制):')
        self.plain_text_input = QLineEdit()
        layout.addWidget(self.plain_text_label)
        layout.addWidget(self.plain_text_input)

        # 密钥输入框
        self.key_label = QLabel('密钥 (10位二进制):')
        self.key_input = QLineEdit()
        layout.addWidget(self.key_label)
        layout.addWidget(self.key_input)

        # 生成密钥按钮
        self.generate_key_button = QPushButton('生成密钥')
        self.generate_key_button.clicked.connect(self.generate_key)
        layout.addWidget(self.generate_key_button)

        # 加密按钮
        self.encrypt_button = QPushButton('加密')
        self.encrypt_button.clicked.connect(self.encrypt)
        layout.addWidget(self.encrypt_button)

        # 解密按钮
        self.decrypt_button = QPushButton('解密')
        self.decrypt_button.clicked.connect(self.decrypt)
        layout.addWidget(self.decrypt_button)

        # 结果显示
        self.result_label = QLabel('')
        layout.addWidget(self.result_label)
        self.setLayout(layout)

        # 导出按钮
        self.export_button = QPushButton('导出')
        self.export_button.clicked.connect(self.export_data)
        layout.addWidget(self.export_button)

    def generate_key(self):
        # 调用SDES类的生成密钥方法
        sdes = SDES()
        key = sdes.generate_random_key()
        # 显示生成的密钥
        self.key_input.setText(''.join(map(str, key)))

    def ascii_to_binary(self,character):
        # 使用format函数将字符的ASCII值转换为8位二进制字符串
        binary_representation = format(ord(character), '08b')
        return binary_representation

    def encrypt(self):
        plaintext = self.plain_text_input.text()
        key = self.key_input.text()
        self.ASCII = False  # 设置为False

        # 检查是否为空
        if len(plaintext) == 0:
            QMessageBox.critical(self, '错误', '必须输入明文')
            return

        # 检查明文是否全为0或1
        for i in range(len(plaintext)):
            if plaintext[i] != '0' and plaintext[i] != '1':
                self.ASCII = True
                break
        plaintextlist = []
        if self.ASCII:
            print("ASCII加密")
            # 尝试将明文转换为ASCII编码
            print(plaintext)
            for char in plaintext:
                binary_representation = self.ascii_to_binary(char)
                print(binary_representation)
                plaintextlist.append(binary_representation)
        else:
            print("二进制加密")
            # 检查明文是否为8位
            if len(plaintext) % 8 != 0:
                QMessageBox.critical(self, '错误', '明文必须为多个8位二进制字符')
                return
            for i in range(0, len(plaintext), 8):
                plaintextlist.append(plaintext[i:i + 8])
        sdes = SDES()
        ciphertextlist = []
        for i in range(len(plaintextlist)):
            ciphertext = sdes.encrypt([int(bit) for bit in plaintextlist[i]], [int(bit) for bit in key])
            # 显示加密结果
            print(ciphertext)
            if self.ASCII:
                # ASCII加密展示，将二进制字符串转换为ASCII字符
                # ciphertextlist.append(ciphertext)
                binary_string = ''.join(map(str, ciphertext))
                # 将二进制字符串转换为整数
                ascii_code = int(binary_string, 2)
                print(ascii_code)
                # 将整数转换为字符
                if ascii_code > 127:
                    utf8_character = chr(ascii_code).encode('utf-8')
                    ciphertextlist.append(utf8_character.decode('utf-8'))
                    print(utf8_character.decode('utf-8'))
                else:
                    # 否则将整数转换为ASCII字符
                    ciphertextlist.append(chr(ascii_code))
                    print(chr(ascii_code))

                encrypted_text = "".join(["".join(map(str, cipher)) for cipher in ciphertextlist])
                self.result_label.setText(f'加密结果: {encrypted_text}')
            else:
                # 二进制加密展示
                ciphertextlist.append(ciphertext)
                encrypted_text = " ".join(["".join(map(str, cipher)) for cipher in ciphertextlist])
                self.result_label.setText(f'加密结果: {encrypted_text}')



    def decrypt(self):
        return

    def export_data(self):
        plaintext = self.plain_text_input.text()
        key = self.key_input.text()
        result = self.result_label.text()

        # 使用文件对话框选择保存文件路径
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_name, _ = QFileDialog.getSaveFileName(self, "保存信息", "", "文本文件 (*.txt);;所有文件 (*)",
                                                   options=options)

        if file_name:
            # 将明文和密钥保存到文件中
            with open(file_name, 'w') as file:
                file.write(f"明文: {plaintext}\n")
                file.write(f"密钥: {key}")
                file.write(f"加密结果: {result}")
            QMessageBox.information(self, '信息', '结果已成功导出到文件。')


def main():
    app = QApplication(sys.argv)
    window = SDESApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
