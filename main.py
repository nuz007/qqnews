import requests,os,time,html2text
from bs4 import BeautifulSoup as bs
starttime=time.time()
def timex():return time.strftime('%Y-%m-%d %H:%M:%S:{}'.format(int(time.time()*1000)%1000))
url1='https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=24hours&srv_id=pc&offset=0&limit=199&strategy=1&ext={"pool":["top","hot"],"is_filter":7,"check_type":true}'
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
        s=f"<h1>{i[0]}</h1>"+ss
        s=s.replace("//inews.gtimg.com","https://inews.gtimg.com").replace("</img>","</img><br/>")
        s=html2text.html2text(s)
        if len(s.split())<=4:continue
        if os.path.exists(f"{time.strftime('%Y-%m-%d')}/{i[0]}.md"):continue
        with open(f"{time.strftime('%Y-%m-%d')}/{i[0]}.md","w",encoding="utf-8") as x:x.write(s)
    except:pass
