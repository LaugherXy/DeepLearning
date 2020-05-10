#任务：<br>
##基于深度学习方法，对大规模的艺术品进行分类，比如按照种类、作者、时期等属性分类。<br>
<br>
##数据集：<br>
###从新浪收藏-艺术品数据库（http://data.collection.sina.com.cn/）中爬取<br>
<br>
##代码运行环境及配置：<br>
###Windows 10<br>
###Anaconda3<br>
###Python3.7<br>
###Tensorflow 2.0<br>
###PyCharm 2019.3.2<br>
<br>
##代码存于./include内，共五个文件：<br>
###GetImageGO.py:对数据集进行爬取，储存于本地D:\BSdata\Picture<br>
###INITimage.py:对爬取的数据集进行预处理、批次处理，便于训练<br>
###NewModel.py:搭建简单的卷积神经网络,对卷积层、池化层、全连接层进行定义，计算loss、accuracy并优化<br>
###Training.py:对爬取的指定数据集进行训练，每100步输出一次结果，同时将训练模型保存于本地D:\BSdata\model<br>
###test.py：利用训练出的模型对指定测试集进行测试<br>
