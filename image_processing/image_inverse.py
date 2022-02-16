import matplotlib
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt


def set_chinese():  #设置中文字体
    import matplotlib
    matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
    matplotlib.rcParams['axes.unicode_minus'] = False


def image_log(input):  #对图像就行对数变换，压缩图像范围
    return np.log(1+input)


def image_inverse(input):  #反转变换 Y= Xmax-X
    value_max = np.max(input) # 求图像中最大灰度值
    output = value_max-input
    return output


if __name__ == '__main__':
    set_chinese()
    gray_img = np.asarray(Image.open('picture/pic2.jpg').convert('L'))
    inv_img = image_inverse(gray_img)

    ## 反转变换实现
    fig = plt.figure()
    ax1 = fig.add_subplot(121)
    ax1.set_title('原图')
    ax1.imshow(gray_img, cmap='gray', vmin=0, vmax=255)

    ax2 = fig.add_subplot(122)
    ax2.set_title('反转后图')
    ax2.imshow(inv_img, cmap='gray', vmin=0, vmax=255)
    plt.show()

    # 对数变换实现
    # input = np.array([[10, 150],
    #                   [250, 25500]])
    # output = image_log(input)
    # print(output)
    #
    # fig = plt.figure()
    # ax1 = fig.add_subplot(121)
    # ax1.set_title('原图')
    # ax1.imshow(input, cmap='gray', vmin=0, vmax=25500)
    #
    # ax2 = fig.add_subplot(122)
    # ax2.set_title('对数变换后')
    # ax2.imshow(output, cmap='gray')
    # plt.show()


