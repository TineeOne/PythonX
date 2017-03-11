# -*- coding:utf-8 *-

from bs4 import BeautifulSoup #导入bs4库
import requests
import requests.exceptions
from urllib.parse import urlsplit
from collections import deque
import re

#定义列表，用于存放要抓取的网页地址（地址队列）
new_urls = deque(['http://bbs.skykiwi.com/forum.php?mod=forumdisplay&fid=55'])

#将运行过的url存起来，避免重复处理，以set()可以保证元素不重复
processed_urls = set()

#定义一个email集合，用于存储收集到邮箱地址
emails = set()

while len(new_urls):
    #不断取出队列的地址进行处理，直到队列里没有地址为止
    url = new_urls.popleft()
    #取出地址后，立即把这个地址加到已处理的地址列表
    processed_urls.add(url)

    #从当前地址中提取出根地址，这样当从文档中找到相对地址时，就可以把它转换成绝对地址
    parts = urlsplit(url)
    base_url = '{0.scheme}://{0.netloc}'.format(parts)
    path = url[:url.rfind('/')+1] if'/'in parts.path else url

    print('Processing %s' % url) #打印出爬取过的网页
    try: #获取网页响应内容，如果出现错误，则跳过继续
        response = requests.get(url)
    except(requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
        continue

    #用正则表达式匹配邮箱地址
    new_emails = set(re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", response.text, re.I))
    #将匹配到的地址添加到emails集合中
    emails.update(new_emails)

    #提取完刚刚爬取的网页内容的email地址后，找到当前网页中的其他网页地址，并将其添加到待处理的url地址队列里
    #这里使用BeautifulSoup库来分析网页html
    soup = BeautifulSoup(response.text)

    #这个库的find_all方法可以根据html标签名来抽取元素
    for anchor in soup.find_all("a"):
        link = anchor.attrs["href"] if "href" in anchor.attrs else""
        if link.startswith('/'):  #如果这个地址以斜线开头，那么把它当做相对地址，然后加上必要的根地址
            link = base_url + link
        elif not link.startswith('http'):
            link = path + link
        #如果地址队列没有，而且之前也没有处理过，那我们就把这个地址加入地址队列里:
        if not link in new_urls and not link in processed_urls::
            new_urls.append(link)

    with open('email.txt', 'w') as f: #将提取的邮箱数据保存在当前目录下的email.txt中
        for m in emails:
            f.write(m+'\n')


