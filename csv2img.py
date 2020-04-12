#! -*- coding: utf-8 -*-
"""
原始文件:
    fer2013.csv
原始数据格式:
    emotion pixels usage

步骤:
    1. 从fer2013.csv文件中，根据usage将文件分割成
       训练集，验证集和测试集
"""

import csv


def read_from_csv(filename, has_head=True):
    """
    读取csv文件并分割出训练集、验证集和测试集数据
    Args:
        filename: csv文件
        has_head: csv文件第一行是否为title
    Returns:
        dastasets: {
            usage: {
                emotion: [pixels]
            }
        }
    """
    datasets = dict()

    with open(filename, 'r') as f:
        # 读取csv, csvr是generator
        csvr = csv.reader(f)

        # 当第一行是title时，则跳过第一行
        if has_head:
            next(csvr)

        for emotion, pixels, usage in csvr:
            if datasets.get(usage):
                if datasets[usage].get(emotion):
                    datasets[usage][emotion].append(pixels)
                else:
                    datasets[usage][emotion] = [pixels]
            else:
                datasets[usage] = {emotion: [pixels]}
    return datasets


from PIL import Image
import numpy as np


def pixel2img(pixel_str, imgpath):
    """
    将像素转换为图片
    Args:
        pixel_str: 像素列表，str类型
        imgpath: 保存图片路径
    """
    pixel_arr = np.asarray(pixel_str.split(), dtype=np.float).reshape(48, 48)
    img = Image.fromarray(pixel_arr).convert('L')
    img.save(imgpath)



def main(filename, saveroot):
    """
    入口函数
    Args:
        filename: csv文件
        data_root: 图片数据保存i目录
    """
    datasets = read_from_csv(filename, saveroot)

    import os
    for usage, emotion_data in datasets.items():
        for emotion, pixels in emotion_data.items():
            data_emotion_root = os.path.join(saveroot, usage, emotion)
            # 创建图片保存目录
            if not os.path.exists(data_emotion_root):
                os.makedirs(data_emotion_root)
            for index, pixel in enumerate(pixels, 1):
                imgpath = os.path.join(data_emotion_root, '%05d.png' % index)
                print(imgpath)
                # 保存图片
                pixel2img(pixel, imgpath)


import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='转换csv文件为图片数据')
    parser.add_argument('-f', '--filename', type=str, help='csv文件路径')
    parser.add_argument('-d', '--saveroot', type=str, help='图片保存目录')
    args = parser.parse_args()
    main(args.filename, args.saveroot)

