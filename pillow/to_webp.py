# coding=utf-8
from PIL import Image
import os


def img_is(file_name):
    imgType_list = ['.jpg', '.bmp', '.png', '.jpeg', '.rgb', '.tif']
    if os.path.splitext(file_name)[-1] in imgType_list:
        return True


def open_img_file(file_dir):
    for root, dirs, files in os.walk(file_dir):
        '''
        root 当前目录路径
        dirs 当前路径下所有子目录
        files 当前路径下所有非目录子文件
        '''
        for f in files:
            if img_is(f):
                to_webp(root, f)
            else:
                return False


def to_webp(root, f):
    print(root + '/' + f)
    im = Image.open(root + '/' + f).convert("RGB")
    im.save(os.path.splitext(f)[0] + ".webp", "WEBP")
    print("转换图片 %s to %s" % (f, os.path.splitext(f)[0] + ".webp"))


def run():
    open_img_file("./")  # 当前路径下的图片


if __name__ == '__main__':
    run()
