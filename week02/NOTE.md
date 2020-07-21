# 学习笔记

### 程序异常捕获及处理</br>
使用try...except...finally...这种方式，捕捉程序运行过程中的异常；还可使用类的继承方法，自行定义Exception来捕获处理特定异常

### PyMySQL丰富PIPELINE管道方式</br>
事务操作谨记要commit提交才能生效

### cookie模拟及验证码识别

### 爬虫中间件及代理IP</br>
设立系统代理IP池，重写中间件补充自己加的功能；部署分布式爬虫，使用scrapy-redis来使scarapy支持分布式，通过各机器对redis执行优先级、调度、去重等工作