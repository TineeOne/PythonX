
第一次碰头会

-[X] 了解各组员目前 py 掌握情况
-[X] 讨论可选项目 根据情况确定项目 
-[X] 各组员时间安排 
-[ ] 确定 github 协作开发流程
-[ ] 明确技术细节 参考资料 [用 Python 爬取实习信息](https://mp.weixin.qq.com/s?__biz=MzA4MjEyNTA5Mw==&mid=2652564266&idx=3&sn=c8e2d01c3162a4f677c334a932baa376&chksm=8464c360b3134a769f24670aeff63eac857e12866daa0cb703923ed669624d1381967c873f84&mpshare=1&scene=1&srcid=0104Z2uQZk2HC3SwQzLLGz0I&key=0b73c2abb17af438b2e8571dae45fb2a4243a95a11bbcebd6f4aea5f14383a4a6665b54339cf86e0ca1f4e86bc5d9946fbca1bbe292febd46ba6dfde42a7e8492764450b3bb290937f53676c33cdd337&ascene=0&uin=MTc3MjY5NzYwNA%3D%3D&devicetype=iMac+MacBookPro12%2C1+OSX+OSX+10.11.6+build(15G1217)&version=12020010&nettype=WIFI&fontScale=100&pass_ticket=WmjSCw5wxD7D21WG59N0WVSRTv0rU7iT2zw0DM9rM0JRi0nbN18H4VYnOR24FdIi)
- [ ] 分配任务 
### 坑

* Zoom 一位成员说话其他人听不到 解决：换用设备，手机-笔记本
* 会议时间略久，技术设备问题 对项目的理解和实现可能性讨论略久 解决：明确需求，直接演示人工如何操作，找出可以自动化的部分，再讨论可能性

### 组员
* 广鹤 @ 广州 时间比较充裕 希望能用 python 解决实际问题, 可投入 2~3h/d
* 罗颖 @ 工作较忙 周末可挤出整块时间讨论分享
* 婉君 @Twanjun 汕头 目前在忙毕业论文 + 实习 可投入时间 1h/d
* 董琛 @TineeOne 北京 2~3h/d




### 项目情况

-缘起：小鹤即将去外地游学打工一年，需在当地找到一些打短工机会。当地论坛不定期有招聘信息发出，希望能够用程序自动抓取特定网站的招聘邮箱，匹配对应职位，定时自动发送求职邮件。

-需求泛化：短期内找兼职、打短工的人，不太需要考虑职位需求，需要给大量招聘单位发送简历。
- 实现可能：爬取特定网站邮箱数据建立数据库，提前定义邮件模板，定时自动发送求职简历邮件。

### 项目执行方案

* MVP 的核心功能？
	- 抓取天维论坛（特定网站）中的招聘邮箱
	- 生成 list1（收件人群发的格式）
	
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
 
 
个人感想：因为小鹤强烈需要这一点，大家就如何理解和实现需求讨论很久，查资料发现技术上不少难点，考虑到各组员目前的技术（基本卡在真实世界 API 这块），最后讨论结果，从需求出发的话，主要是爬虫编写，部署在命令行，自动发送邮件稍后再说。
 
- 170305 大妈反馈：

哪来迷津
唯自不信
元能早赋
最小原型
早立早成
编剧思维
规则推进
其它无它
享受编程
升级思维
自在数据

编程思维

编剧思维 or 编程思维？

项目选题参考：

* [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)

170306

- 汇报项目进展
- 提醒大家需要同意协作邀请
- 向梁培利教练请教 爬虫 难点
- 确定协作流程