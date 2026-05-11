import torch
from torch import nn
from PIL import Image
import numpy as np
import os

class Generator(nn.Module):
    def __init__(self, input_size = 10):
        super(Generator, self).__init__()

        def block(in_num, out_num, norm_=True):  # 定义网络的块结构
            layers = [nn.Linear(in_num, out_num)]  # 线性层
            if (norm_):
                layers.append(nn.BatchNorm1d(out_num, 0.75))  # 批标准化层
            layers.append(nn.LeakyReLU())  # 激活函数层
            return layers

        self.model = nn.Sequential(
            *block(input_size, 128, norm_=False),  # 线性层+激活函数层
            *block(128, 256),  # 线性层+批标准化层+激活函数层
            *block(256, 512),
            *block(512, 1024),
            nn.Linear(1024, 28*28),  # 线性层
            nn.Tanh()  # 激活函数层，输出在[-1,+1]之间
        )

    def forward(self, x):
        y = self.model(x)
        y = y.view(x.size(0), 28, 28)
        return y

def saveImage(images, filename):  # 按5行5列保存25个图像到一个png文件
    bigImg = np.ones((150, 150))*255  # 先生成宽高均为150的全白大图数组
    for i in range(len(images)):
        row = int(i / 5) * 30  # 计算每个子图在大图中的左上角位置
        col = i % 5 * 30
        img = images[i]
        bigImg[col:col + 28, row:row + 28] = (1-img)*255/2  # 将子图放入大图中
    f = Image.fromarray(bigImg).convert('L')  # 将数组转换为8位灰度图
    f.save(filename, 'png')  # 保存文件

def createLabels(device, img_num, input_size, real=0):
    f_y1 = np.random.randint(0, 10, (img_num, 1))
    f_y2 = np.random.rand(img_num, input_size - 1)
    arr2 = np.concatenate((f_y1, f_y2), axis=1, dtype=np.float32)
    in_random = torch.tensor(arr2).to(device)  # 输入向量
    # f_labels = torch.zeros(img_num).view((img_num, 1)).to(device)
    return in_random, torch.from_numpy((f_y1* real+(1-real)*10).squeeze().astype(np.int64)).to(device)

if __name__=='__main__':
    num = 0
    img_num = 25
    input_size=10
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    generator = torch.load('gen_mnist.pth').to(device)
    os.makedirs('imgs', exist_ok=True)  # 建立生成图像的存储目录
    while num >=0 and num <=9:
        num = input("pls input number(0-9, others for quit):")
        num = int(num)
        f_y1 = np.ones((img_num,1))*num
        f_y2 = np.random.rand(img_num, input_size - 1)
        arr2 = np.concatenate((f_y1, f_y2), axis=1, dtype=np.float32)
        in_random = torch.tensor(arr2).to(device)  # 输入向量
        f_imgs = generator(in_random)
        saveImage(f_imgs[:25].detach().cpu().numpy(),"imgs/mnist%d.png" % num)
