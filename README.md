## 项目名称：让工作来找你

## 项目简介：

* 你的项目重点解决用户什么问题？
	- 招聘邮箱信息分散在各个二级网页，需要逐个点开 - 找到邮箱 - 复制 - 保存为联系人/粘贴到收件人列表
* 目标用户是怎样的？
	- 找兼职、打短工的人，需要给大量招聘单位发送简历，对职位匹配度要求不高
	
#### 项目成员：

* @13416136446  项目创意发起，起名
* @lying87  
* @Twanjun 
* @linfeng365 
* @TineeOne（组长）协作流程记录

项目代码地址：https://github.com/TineeOne/PythonX

### 项目执行方案

* MVP 的核心功能？

	- 抓取天维论坛（特定网站）中的招聘邮箱
		- 定义需要爬取的数据，即 Item，需要创建一个类，根据需要对 Item 进行建模
			- 邮箱地址
			- 职位关键词？
		- 编写 spider，包含初始 URL，如何跟进网页中的链接，如何分析页面内容。  需要继承刚刚创建的类，并定义以下属性：
			- `name`：唯一，用于区别 Spider
			- `start_urls`：包含需要爬取的 URL 列表 
			- `parse()` ：函数，负责解析返回的数据，提取数据（生成 Item）并生成需要进一步处理的对象 - 跟进，
			- 用 Selectors 提取 Item，通过观察源码确定合适的 XPath 表达式 - 分析并提取
		- 保存爬取到的数据
			 - 使用 Feed exports，生成 json 格式文件
	
* 附加功能：
	- 自动发送求职邮件
	- 生成 list2（邮箱对应相应职位）
	- 回复的邮件对应 list2 的职位
	
* 技术细节：
	- 编写爬虫抓取特定网站的邮箱 scrapy
	- 将爬取到的 Item 储存到 Pipeline [Item Pipeline — Scrapy 0.24.1 文档](http://scrapy-chs.readthedocs.io/zh_CN/latest/topics/item-pipeline.html#topics-item-pipeline)
	- 自动群发邮件 
		- [python发送各类邮件的主要方法 - 小五义 - 博客园](http://www.cnblogs.com/xiaowuyi/archive/2012/03/17/2404015.html)
		- [Python Sending Email using SMTP](https://www.tutorialspoint.com/python/python_sending_email.htm) 


* 难点：
 - 爬虫编写、数据存储与提取
 - 部署平台

### 项目进程：

- 170304（8wd6） 晚 第一次线上碰面，拟确定项目名称，理清项目基本情况
- 170305 (9wd0) 确定项目名称，完成项目概述
- 170306（9wd1）明确分工及协作流程，开工
- 拟 9wd2~d5，完成 MVP
- 9wd6，小组碰面，讨论优化方向及路演准备
- 官方路演初步安排 12wd0
	
##### 参考资料：

* [HbFinalTaskIdea · AIMinder/Py103 Wiki](https://github.com/AIMinder/Py103/wiki/HbFinalTaskIdea)
* [GitHub flow - User Documentation](https://help.github.com/articles/github-flow/)
* [如何正确的使用github进行项目的协同开发? - 知乎](https://www.zhihu.com/question/27087744)
	

清单：

- [X] 了解各组员目前 py 掌握情况
- [X] 讨论可选项目 根据情况确定项目 
- [X] 各组员时间投入 
- [X] 完成项目概述
- [X] 明确 MVP 技术细节 
- [X] 进度安排初步完成
- [ ] 确定 github 协作开发流程
- [ ] 明确个人分工

### - CHANGELOG	

- 170305 TineeOne 增补项目概况，MVP 分解
- 170304 TineeOne 汇总