# FER2013数据处理
## 目录结构
- csv2img.py        # csv转image代码
- fer2013           # 原始数据目录
    - fer2013.csv   # csv文件，（数据不完整，需下载并覆盖该文件）
- images            # 转换后的图片文件保存目录
- run.sh            # 程序运行代码

## 快速开始
### Windows系统
```shell
python csv2img.py -f fer2013\fer2013.csv -d images
```

### Linux系统
```shell
sh run.sh -f fer2013/fer2013.sh -d images
```
