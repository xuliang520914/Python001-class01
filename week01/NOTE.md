### 第一周学习笔记
- 第一个爬虫
```python
# 获取豆瓣电影排名前250名的第一页的电影名称和链接
import requests
from bs4 import BeautifulSoup as bs
# 使用.get请求
# response = requests.get('请求的链接地址', 'headers字典信息')
user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
header = {'user-agent': user_agent}
response = requests.get('https://movie.douban.com/top250', headers = header)
# 模拟header信息，是为了防止爬虫被拦截的手段之一，为了接近于浏览器访问
# response.text 获取页面内容 response.status_code获取请求返回的状态码

# 解析网页信息
bs_info = bs(response.text, 'htmp.parser)

# 过滤出想要的信息，然后遍历信息
for tags in bs_info.find_all('div', attrs={'class':'hd'}):
    for tag in tags.find_all('a',):
        print(tag.get('href'))
        print(tag.find('span').text)
```

- 使用`XPath`解析网页
```python
import lxml.etree
$url = 'https://movie.douban.com/subject/1292052/' # 进入详情页面抓取信息

# 解析部分替换
# xml化处理
selector = lxml.etree.HTML(response.text)
film_name = selector.xpath('//*[@id="content"]/h1/span[1]/text()')

plan_date = selector.xpath('//*[@id="info"]/span[10]/text()')
# ...上映日期，评分等等
film_list = [film_name, plan_date]

# pandas库写入csv
import pandas as pd
pd_movie = pd.DataFrame(data=film_list)

# windows使用gbk
pd_movie.csv('./movie.csv', encoding='utf8', index=False, header=False)

```

- `scrapy`
    - 安装
  
    - 结构

    - 