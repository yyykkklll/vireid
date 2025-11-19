import socket
import os
import platform

print("=" * 30)
print(f"我是谁 (Hostname): {socket.gethostname()}")
print(f"我在哪 (OS): {platform.system()} {platform.release()}")
print(f"当前工作目录: {os.getcwd()}")
print("=" * 30)

# 如果你是做深度学习的，可以验证显卡：
try:
    import torch
    print(f"Cuda 可用: {torch.cuda.is_available()}")
    if torch.cuda.is_available():
        print(f"显卡名称: {torch.cuda.get_device_name(0)}")
except ImportError:
    pass