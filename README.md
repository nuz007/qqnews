# 腾讯新闻归档

本归档由爬虫生成，每天建立一个文件夹。
每1~2小时会爬取一次，归档从2022年12月27日开始更新。

爬取格式为 Markdown


源代码:

.github/workflows/spider.yml

```yml
name: spider
on:
  push:
    branches:
      - main
  schedule:
    - cron: "0 * * * *"

jobs:
  run-python-script:
    runs-on: ubuntu-latest
    steps:
      - name: checkoutss
        uses: actions/checkout@v2

      - name: instpython3
        uses: actions/setup-python@v2
        with:
          python-version: '3.11.1'
      - name: Commit files
        run: |
          git config --local user.email "bot@github.com"
          git config --local user.name "bot"
          git remote set-url origin https://${{ github.actor }}:${{ secrets.GITHUB_TOKEN }}@github.com/${{ github.repository }}
          git pull --rebase
          pip3 install requests
          pip3 install bs4
          python main.py
          git add .
          git commit --allow-empty -m "爬取腾讯新闻"
          git push -f
```

main.py

```python
import requests,os,time,html2text
from bs4 import BeautifulSoup as bs
starttime=time.time()
def timex():return time.strftime('%Y-%m-%d %H:%M:%S:{}'.format(int(time.time()*1000)%1000))
logfile=open("log.txt","a",encoding="utf-8")
logfile.write(f"============{timex()}============\n开始新的一轮爬取\n\n")
url1='https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=24hours&srv_id=pc&offset=0&limit=199&strategy=1&ext={"pool":["top","hot"],"is_filter":7,"check_type":true}'
#url2='https://r.inews.qq.com/gw/event/hot_ranking_list?ids_hash=&offset=2&page_size=1'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 Edg/108.0.1462.54"}
qq1=requests.get(headers=headers,url=url1).json()
datalist=[]
for i in qq1["data"]["list"]:
    tmptitle=i["title"]
    tmpurl=i["url"]
    datalist.append(tuple([tmptitle,tmpurl]))
tmphtml=""
tmpbs=""
if not os.path.exists(f"{time.strftime('%Y-%m-%d')}"):os.makedirs(f"{time.strftime('%Y-%m-%d')}")
for i in datalist:
    try:
        tmphtml=requests.get(i[1]).text
        tmpbs=bs(tmphtml,"html.parser")
        ss=str(tmpbs.select("body > div.qq_conent.clearfix > div.LEFT > div.content.clearfix")[0])
        if not(ss):continue
        s=f"<h1>{i[0]}</h1>"+ss
        if os.path.exists(f"{time.strftime('%Y-%m-%d')}/{i[0]}.md"):
            logfile.write(f"============{timex()}============\n重复文件\n标题:{i[0]}\n链接:{i[1]}\n\n")
            continue
        with open(f"{time.strftime('%Y-%m-%d')}/{i[0]}.md","w",encoding="utf-8") as x:x.write(html2text.html2text(s.replace("//inews.gtimg.com","https://inews.gtimg.com").replace("</img>","</img><br/>")))
        logfile.write(f"============{timex()}============\n爬取成功\n标题:{i[0]}\n链接:{i[1]}\n\n")
    except:logfile.write(f"============{timex()}============\n爬取失败\n标题:{i[0]}\n链接:{i[1]}\n\n")
logfile.write(f"============{timex()}============\n本轮爬取结束\n用时:{int(time.time()-starttime)}秒\n\n")

```

# 给个fork呗
