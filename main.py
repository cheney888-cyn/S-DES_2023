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

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    print_hi('PyCharm')

#测试
sdes = SDES()
text=[0,1,1,1,0,0,1,1]
print(sdes.SBox(text))