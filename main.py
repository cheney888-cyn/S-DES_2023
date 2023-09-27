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
        self.P10 = [3, 5, 2, 7, 4, 0, 1, 9, 8, 6]
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

    # 扩展置换EP
    def EP_Transform(self, data):
        output = [0] * 8

        for i in range(8):
            output[i] = data[self.EP[i] - 1]

        return output

    # 10bits密钥K生成
    def Key_Generate(self, key):

        # P10置换
        p10_key = [0] * 10
        for i in range(10):
            p10_key[i] = key[self.P10[i] - 1]

        # 循环左移
        left_key = p10_key[:5]
        right_key = p10_key[5:]
        left_key = left_key[1:] + left_key[:1]
        right_key = right_key[1:] + right_key[:1]

        # P8置换
        p8_key = self.P8[5] + self.P8[2] + self.P8[6] + self.P8[3] + self.P8[7] + self.P8[4] + self.P8[9] + \
                 self.P8[8]

        return p8_key

    # 子密钥K1和K2生成
    def SubKey_Generate(self, key):
        p10_key = self.Key_Generate(key)

        # 循环左移一位得到K1
        c1 = p10_key[:4]
        d1 = p10_key[5:]
        c1 = c1[1:] + c1[:1]
        d1 = d1[1:] + d1[:1]
        k1 = c1 + d1

        # 循环左移两位得到K2
        c2 = c1[1:] + c1[:1]
        d2 = d1[1:] + d1[:1]
        k2 = c2 + d2

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
        print(left)
        print(right)
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


#测试
sdes = SDES()
text=[0,1,1,1,0,0,1,1]
print(sdes.SBox(text))