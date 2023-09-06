from PIL import Image, ImageDraw, ImageFont
import os
import logging
import time
import sys

# 设置日志输出









def image_read(image_path: str, debug: bool = False) -> tuple:
    """将输入的图像文件(文件路径)进行读取，并逐行扫描后，将像素数据写入列表对象并返回

    Args:
        image_path (str): 图像文件的路径

    Returns:
        tuple: (X_image:int, Y_image:int, img_pixels:list, img_data_image:Image)
        X_image (int): 图像文件的路径
        Y_image (int): 二进制数据的处理顺序
        img_pixels (int): 图像的像素数据
        img_data_image (Image): 图像对象
    """
    img_data_image = Image.open(image_path)
    img_data_image.convert("RGBA")
    if debug == True:
        img_data_image.show()
    X_image, Y_image = img_data_image.size
    img_pixels = []
    for y in range(Y_image):
        for x in range(X_image):
            img_pixels.append(img_data_image.getpixel((x, y)))
    return X_image, Y_image, img_pixels, img_data_image


def text2img(text: str) -> Image:
    """将一段文本生成为一个图像对象，仅支持英文（ascii码的范围要在range(256)之间）

    Args:
        text (str): 输入的文本

    Returns:
        Image: 返回的图像对象
    """
    # 文本仅支持英文（ascii码的范围要在range(256)之间）
    im = Image.new("RGBA", (len(text) * 35, 80), (255, 255, 255))
    dr = ImageDraw.Draw(im)
    font = ImageFont.truetype(os.path.join("fonts", "arial.ttf"), 64)
    dr.text((15, 5), text, font=font, fill="#000000")
    im.show()


def image_binarization(pixels_data: list, threshold: int | None, X_image=None, Y_image=None, debug: bool = False) -> list:
    data_res = []
    for pixel in pixels_data:
        sum = 0
        for chennel in pixel:
            sum += chennel
        if sum < threshold:
            data_res.append(1)
        else:
            data_res.append(0)
    if debug == True:
        img_test = Image.new("RGBA", (X_image, Y_image))
        for y in range(Y_image):
            for x in range(X_image):
                if data_res[y * X_image + x] == 1:
                    img_test.putpixel((x, y), (255, 255, 255))
                else:
                    img_test.putpixel((x, y), (0, 0, 0))
    return data_res
