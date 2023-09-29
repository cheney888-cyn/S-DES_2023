import random
class SDES:
    def __init__(self):
        # 初始置换IP置换表
        self.IP = [2, 6, 3, 1, 4, 8, 5, 7]
        # 初始逆置换IP^-1置换表
        self.IP_INV = [4, 1, 3, 5, 7, 2, 8, 6]
        # 扩展置换EP置换表
        self.EP = [4, 1, 2, 3, 2, 3, 4, 1]
        # P4置换表
        self.P4 = [2, 4, 3, 1]
        # P8置换表
        self.P8 = [6, 3, 7, 4, 8, 5, 10, 9]
        # P10置换表
        self.P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
        # S-盒S0和S1
        self.S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 0, 2]]
        self.S1 = [[0, 1, 2, 3], [2, 3, 1, 0], [3, 0, 1, 2], [2, 1, 0, 3]]
        # spbox置换表
        self.SPBOX = [2, 4, 3, 1]

    # 初始置换IP
    def IP_Transform(self, data):
        output = [0] * 8

        for i in range(8):
            output[i] = data[self.IP[i] - 1]

        return output

    # 初始逆置换IP^-1
    def IP_INV_Transform(self, data):
        output = [0] * 8

        for i in range(8):
            output[i] = data[self.IP_INV[i] - 1]

        return output

    def generate_random_key(self):
        # 生成一个长度为10的随机二进制密钥
        key = [random.randint(0, 1) for _ in range(10)]
        return key

    # 10bits密钥K生成
    def Key_Generate(self, key):
        # P10置换
        p10_key = []
        for i in range(10):
            p10_key.append(key[self.P10[i] - 1])
        print("p10_key")
        print(p10_key)
        # 循环左移
        left_key = p10_key[:5]
        right_key = p10_key[5:]
        left_key = left_key[1:] + left_key[:1]
        right_key = right_key[1:] + right_key[:1]
        q_key = left_key + right_key
        # P8置换
        p8_key = [0] * 8
        for i in range(8):
            p8_key[i] = q_key[self.P8[i] - 1]
        # 子密钥K1和K2生成
        # 循环左移1位得到K1
        k1 = p8_key
        # 循环左移2位得到K2
        left_key1 = left_key[1:] + left_key[:1]
        right_key1 = right_key[1:] + right_key[:1]
        q_key1 = left_key1 + right_key1

        # P8置换
        p8_key1 = [0] * 8
        for i in range(8):
            p8_key1[i] = q_key1[self.P8[i] - 1]
        k2 = p8_key1
        return k1, k2

    # EP扩展
    def expandFunction(self, data):
        expand_data = []
        for i in range(8):
            expand_data.append(data[self.EP[i]-1])
        return expand_data
    # 异或运算
    def xorCalculation(self, data1, data2):
        result = []
        for i in range(len(data1)):
            result.append(data1[i]^data2[i])
        return result

    # S盒运算
    def SBox(self, data):
        left= data[0:4]
        right = data[4:8]
        #print(left)
        #rint(right)
        row = left[0]*2+left[3]
        col = left[1]*2+left[2]
        s0 = self.S0[row][col]
        row = right[0]*2+right[3]
        col = right[1]*2+right[2]
        s1 = self.S1[row][col]
        result=[]
        result.append(s0//2)
        result.append(s0%2)
        result.append(s1//2)
        result.append(s1%2)
        return result
    # P4直接置换
    def P4Function(self, data):
        result = []
        for i in range(4):
            result.append(data[self.P4[i]-1])
        return result
        # F函数

    def FFunction(self, data, key):
        expand_data = self.expandFunction(data)
        xor_data = self.xorCalculation(expand_data, key)
        sbox_data = self.SBox(xor_data)
        p4_data = self.P4Function(sbox_data)
        return p4_data

        # 拆分

    def split(self, data):
        return data[0:4], data[4:8]
        # 加密
    def encrypt(self, data, key):
        k1, k2 = self.Key_Generate(key)
        ipData = self.IP_Transform(data)
        left, right = self.split(ipData)
        fk1Data = self.FFunction(right, k1)
        xorData1 = self.xorCalculation(left, fk1Data)
        #print(xorData1)
        fk2Data = self.FFunction(xorData1, k2)
        xorData2 = self.xorCalculation(fk2Data, right)
        #print(xorData2)
        Data = xorData2 + xorData1
        #print(Data)
        ipInvdata = self.IP_INV_Transform(Data)
        return ipInvdata

    #解密
    def decrypt(self, data, key):
        k1, k2 = self.Key_Generate(key)
        ipData = self.IP_Transform(data)
        left, right = self.split(ipData)
        fk1Data = self.FFunction(right, k2)
        xorData1 = self.xorCalculation(left, fk1Data)
        fk2Data = self.FFunction(xorData1, k1)
        xorData2 = self.xorCalculation(fk2Data, right)
        Data = xorData2 + xorData1
        ipInvdata = self.IP_INV_Transform(Data)
        return ipInvdata

#
# #测试
sdes = SDES()
# text=[1,0,1,0,1,0,1,0]
key=[1,0,1,0,1,0,1,0,1,0]
print(sdes.Key_Generate(key))
# #print(sdes.generate_random_key())
