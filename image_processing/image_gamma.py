import matplotlib
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button, RadioButtons


def set_chinese(): #设置中文字体
    import matplotlib
    matplotlib.rcParams['font.sans-serif'] = ['KaiTi']
    matplotlib.rcParams['axes.unicode_minus'] = False


def gamma_transition(input, gamma=1, eps=0): #默认gamma=1即恒等变换，eps=0
    return 255.*(((input+eps)/255.)**gamma)


def crt_correction(val,output):
    gamma_correct=round(slider2.val)
    crt_output = gamma_transition(output, gamma=gamma_correct, eps=0)
    ax2.set_title('矫正后gamma= '+str(gamma))
    ax2.imshow(output, cmap='gray', vmin=0, vmax=255)


def update_gamma(event):
    gamma = slider1.val
    output = gamma_transition(gray_img, gamma=gamma, eps=0)
    ax1.set_title('gamma函数变换后,gamma= '+str(round(gamma,2)))
    ax1.imshow(output, cmap='gray', vmin=0, vmax=255)
    ax2.hist(output.flatten(), bins=50, density=True, color='r', edgecolor='k')
    plt.draw()


def reset(event):
    slider1.reset()
    gamma = slider1.val
    output = gamma_transition(gray_img, gamma=gamma, eps=0)
    ax1.set_title('gamma函数变换后,gamma= '+str(gamma))
    ax1.imshow(output, cmap='gray', vmin=0, vmax=255)
    ax2.hist(output.flatten(), bins=50, density=True, color='r', edgecolor='k')

    # input_arr = np.array([[0, 50, 100, 150],
    #                       [0, 50, 100, 150],
    #                       [0, 50, 100, 150],
    #                       [0, 50, 100, 150]])
if __name__ == '__main__':

    set_chinese()
    gray_img = np.asarray(Image.open('../picture/pic2.jpg').convert('L'))
    fig = plt.figure()

    ax0 = fig.add_subplot(131)
    ax0.set_title('输入矩阵')
    ax0.imshow(gray_img, cmap='gray', vmin=0, vmax=255)

    ax1 = fig.add_subplot(132)
    #更新gamma函数，并实时显示映射后的图像
    plt.subplots_adjust(bottom=0.4)
    s1 = plt.axes([0.2, 0.1, 0.6, 0.1], facecolor='lightgoldenrodyellow')#[left bottom width height]
    slider1 = Slider(s1,'参数gamma', 0.0, 2.0,
                   valfmt='% f', valinit=1.0, valstep=0.01)

    slider1.set_val(1)  # gamma初始值为1
    output = gamma_transition(gray_img)
    ax1.set_title('gamma函数变换后,gamma= ' + str(slider1.val))
    ax1.imshow(output, cmap='gray', vmin=0, vmax=255)

    ax2=fig.add_subplot(133)
    ax2.hist(output.flatten(),bins=50,density=True,color='r',edgecolor='k')

    #调整gamma
    axAdjust = plt.axes([0.6, 0.025, 0.1, 0.04])
    buttonAdjust = Button(axAdjust, 'Adjust',  hovercolor='red')
    buttonAdjust.on_clicked(update_gamma)
    #重置gamma
    resetax = plt.axes([0.8, 0.025, 0.1, 0.04])
    button = Button(resetax, 'Reset',  hovercolor='yellow')
    button.on_clicked(reset)

    # gamma=slider1.val
    # output = gamma_transition(input_arr, gamma=gamma, eps=0)
    # #矫正crt作用后图像的gamma
    # ax2 = fig.add_subplot(133)
    # plt.subplots_adjust(bottom=0.4)
    # s2 = plt.axes([0.5, 0.1, 0.4, 0.1], facecolor='lightgoldenrodyellow')#[left bottom width height]
    # slider2 = Slider(s2,'矫正参数gamma', 0.0, 1.0,
    #                valfmt='% f', valinit=0.5, valstep=0.1)
    # slider2.on_changed(crt_correction)
    # slider2.reset()
    # slider2.set_val(0.5)

    plt.show()