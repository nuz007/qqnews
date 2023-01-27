import requests,os,time,html2text,sys,traceback
from bs4 import BeautifulSoup as bs
starttime=time.time()
url1='https://i.news.qq.com/trpc.qqnews_web.kv_srv.kv_srv_http_proxy/list?sub_srv_id=24hours&srv_id=pc&offset=0&limit=190&strategy=1&ext={"pool":["top","hot"],"is_filter":7,"check_type":true}'
headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
qq1=requests.get(headers=headers,url=url1).json()
datalist=[]
for i in qq1["data"]["list"]:
    tmptitle=i["title"]
    tmpurl=i["url"]
    if time.strftime("%Y%m%d") not in tmpurl:
        print(f"EXPIRED\n{tmptitle}\n{tmpurl}\n\n")
        continue
    datalist.append(tuple([tmptitle,tmpurl]))
tmphtml=""
tmpbs=""
if not os.path.exists(f"{sys.path[0]}/{time.strftime('%Y-%m-%d')}"):os.makedirs(f"{sys.path[0]}/{time.strftime('%Y-%m-%d')}")
for i in datalist:
    time.sleep(1)
    try:
        tmphtml=requests.get(i[1]).text
        tmpbs=bs(tmphtml,"html.parser")
        ss=str(tmpbs.select("div.LEFT div.content.clearfix")[0])
        s=f"<h1>{i[0]}</h1>"+ss
        s=s.replace("//inews.gtimg.com","https://inews.gtimg.com").replace("</img>","</img><br/>")
        s=html2text.html2text(s)
        if len(s.split())<=3:
            print(f"INVALID\n{i[0]}\n{i[1]}\n\n")
            continue
        if os.path.exists(f"{sys.path[0]}/{time.strftime('%Y-%m-%d')}/{i[0]}.md"):
            print(f"EXIST\n{i[0]}\n{i[1]}\n\n")
            continue
        with open(f"{sys.path[0]}/{time.strftime('%Y-%m-%d')}/{i[0]}.md","w",encoding="utf-8") as x:x.write(s)
        print(f"SUCCESS\n{i[0]}\n{i[1]}\n\n")

    except Exception as e:print(f"ERROR\n{i[0]}\n{i[1]}\n{e.args}\n======\n{traceback.format_exc()}\n")
