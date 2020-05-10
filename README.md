#课题：基于深度学习的大规模艺术品属性分类研究

##任务：
###基于深度学习方法，对大规模的艺术品进行分类，比如按照种类、作者、时期等属性分类。

##数据集：
###从新浪收藏-艺术品数据库（http://data.collection.sina.com.cn/）中爬取

##代码运行环境及配置：
###Windows 10
###Anaconda3
###Python3.7
###Tensorflow 2.0
###PyCharm 2019.3.2

##代码存于./include内，共五个文件：
###GetImageGO.py:对数据集进行爬取，储存于本地D:\BSdata\Picture
###INITimage.py:对爬取的数据集进行预处理、批次处理，便于训练
###NewModel.py:搭建简单的卷积神经网络,对卷积层、池化层、全连接层进行定义，计算loss、accuracy并优化
###Training.py:对爬取的指定数据集进行训练，每100步输出一次结果，同时将训练模型保存于本地D:\BSdata\model
###test.py：利用训练出的模型对指定测试集进行测试
