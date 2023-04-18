## 简单的切片拼接程序ImageMosaic

基于python3.6开发，保证python环境高于此版本。

#### 使用方法

运行cmd，在所在目录下运行：

```
python ImageMosaic.py
```

输入参数包括：

- 文件路径
- 输入图片扩展ing
- 行数
- 列数
- 输出路径
![图片](https://user-images.githubusercontent.com/106393608/232687131-2a4ba12e-c290-4d1c-b3d2-e20bbf30a7aa.png)



#### 预处理

切片图片需放置在同一路径下，图片文件按1，2，3……命名，图片顺序按第一行+第二行……排列；

已知支持png、jpg格式，其它格式没测试过；

需要预估切片拼接规模，输入行数及列数；

若输入切片不规则，可能需要手动计算更改一下画布尺寸

```
result = Image.new(image.mode, (W, H))
```

