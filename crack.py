import time
from sdes import SDES


def brute_force_decrypt(ciphertext, known_plaintexts, max_key_attempts=1024):
    sdes = SDES()
    start_time = time.time()  # 记录开始时间
    key_list = []
    for key in range(0, max_key_attempts):
        key_binary = bin(key)[2:].zfill(10)  # 将整数密钥转换为10位二进制表示
        flag = 0
        for i in range(len(known_plaintexts)):
            decrypted = sdes.decrypt(ciphertext[i], [int(bit) for bit in key_binary])
            print(decrypted)
            print(known_plaintexts[i])
            # 如果解密结果与已知的明文不匹配，表示这个密钥不正确
            if decrypted != known_plaintexts[i]:
                break
            else:
                flag += 1
                print(flag)
        # 如果对于所有明文密文对都匹配，表示找到了正确的密钥
        if flag == len(known_plaintexts):
            key_list.append(key_binary)

    # 如果找到了一个或多个密钥
    if key_list:
        end_time = time.time()  # 记录结束时间
        elapsed_time = end_time - start_time
        return key_list, elapsed_time
    else:

        # 如果遍历所有可能的密钥都没有匹配，返回 None 表示失败
        return None, None


if __name__ == "__main__":
    known_plaintexts = [
        [0,0,0,0,1,1,1,1],[ 0,0,0,1,0,0,0,0],[ 0,0,0,1,0,0,0,1]
    ]
    ciphertexts = [
        [1,0,1,0,1,1,0,1], [0,0,1,0,0,0,0,1], [1,0,0,1,1,0,0,1]
    ]
    found_key, elapsed_time = brute_force_decrypt(ciphertexts, known_plaintexts)
    if found_key:
        print(f"找到正确的密钥: {found_key},共{len(found_key)}个")
        print(f"破解所需的时间: {elapsed_time:.2f} 秒")
    else:
        print("未找到正确的密钥")
