#!/bin/sh
filename=$1 # csv文件路径
saveroot=$2 # 图片保存目录


python csv2img.py \
    --filename $filename \
    --saveroot $saveroot
