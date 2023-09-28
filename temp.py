import random

def generate_random_key():
    # 生成一个长度为10的随机二进制串
    key = [random.randint(0, 1) for _ in range(10)]
    return key

# 调用函数生成随机密钥
random_key = generate_random_key()
print(random_key)
