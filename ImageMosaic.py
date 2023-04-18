# -*- coding: utf-8 -*-
# python3.6
from PIL import Image

# 处理报错Exception has occurred: DecompressionBombError Image size exceeds limit of 178956970 pixels
Image.LOAD_TRUNCATED_IMAGES = True
Image.MAX_IMAGE_PIXELS = None

# 定义拼图函数
def image_masaic(image_path, rows, cols, image_type):
    # 计算每张图片的宽度和高度
    image = Image.open(image_path + "1" + image_type)
    width, height = image.size
    # 创建拼图画布
    result = Image.new(image.mode, (width * cols, height * rows))
    # 循环拼接每张图片
    heightAcc = 0
    for row in range(rows):
        widthAcc = 0
        for col in range(cols):
            filename = image_path + str(row * cols + col+1) + image_type
            try:
                sub_image = Image.open(filename)
            except:
                print("错误，找不到"+ filename)
                break
            else:
                result.paste(sub_image, (widthAcc,  heightAcc))
                widthAcc = widthAcc + sub_image.width
        heightAcc = heightAcc + sub_image.height
    # 返回拼接后的图片
    return result

# 输入
print("要求文件名从1开始按顺序编号")
image_path = input("文件夹路径:")+"\\"
image_type = input("图片文件扩展名:")
rows = input("行数：")
cols = input("列数：")
output_path = input("输出路径：")
result = image_masaic(image_path, int(rows), int(cols),'.'+image_type)
result.save(output_path)
result.show()
print("输出完成")