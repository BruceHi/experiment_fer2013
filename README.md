# FER2013数据处理
## 目录结构
- csv2img.py    # csv转image代码
- fer2013       # 原始数据目录，主要使用fer2013/fer2013.csv
- images        # 转换后的图片文件保存目录
- run.sh        # 程序运行代码

## 快速开始
### Windows系统
```shell
python csv2img.py -f fer2013\fer2013.csv -d images
```

### Linux系统
```shell
sh run.sh -f fer2013/fer2013.sh -d images
```
