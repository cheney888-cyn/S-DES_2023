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
        self.S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]
        self.S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]

    # 初始置换IP
    def IP_Transform(self, data):

    # 初始逆置换IP^-1
    def IP_INV_Transform(self, data):

    # 扩展置换EP
    def EP_Transform(self, data):

    # 10bits密钥K生成
    def Key_Generate(self, key):

    # 子密钥K1和K2生成
    def SubKey_Generate(self, key):

    #
