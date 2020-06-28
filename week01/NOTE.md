# 学习笔记

### 创建项目：<br/>
scrapy startproject project_name

### 初始化爬虫项目：<br/>
cd first_scrapy_project<br/>
scrapy genspider example example.com

### 启动爬虫：<br/>
scrapy crawl example.py

### yield的用法：<br/>
带yield的函数是一个生成器，而不是一个真正的函数了，这个生成器有一个方法就是next函数，next就相当于“下一步”生成哪个数，这一次的next开始的地方是接着上一次的next停止的地方执行的，所以调用next的时候，生成器并不会从函数的最开始敌方执行，只是接着上一步停止的地方开始，然后遇到yield后，return出要生成的数，此步就结束。

### 列表推导式：<br/>
推导式不仅简短优雅，更为重要的是推导式的效率要比普通的for循环要高，把需要几行的for循环用一行代码简洁的写出来。