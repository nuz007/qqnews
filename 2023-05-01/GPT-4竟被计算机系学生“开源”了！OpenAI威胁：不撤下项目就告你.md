# GPT-4竟被计算机系学生“开源”了！OpenAI威胁：不撤下项目就告你

![](https://inews.gtimg.com/newsapp_bt/0/15787581106/1000)

众所周知，ChatGPT是免费的，但想尝试最新最强的GPT-4，基本上就只有「氪金」这一条路可以走——

虽然也有一些集成了GPT的网站，比如微软的必应、You.com等，但他们多少都会夹带点私货。

那么，如果想体验更加原生的GPT-4，但又不想花钱怎么办？

最近，一个名为GPT4Free项目横空出世。不仅在GitHub上斩获18.5k星，而且登上了Trending周榜。

然而，制作这个项目的CS学生Xtekky却表示，OpenAI现在要求他在五天内关闭整个项目，否则将面临诉讼。

![](https://inews.gtimg.com/newsapp_bt/0/15787581126/1000)_项目地址：https://github.com/xtekky/gpt4free_

这其中的矛盾在于，GPT4Free所使用的这些网站本身，都是给OpenAI支付了大量费用，才用上的GPT模型。

因此，通过脚本进来的查询，网站不仅要掏腰包买单，而且自己还没得到任何流量。

如果这个网站是依靠广告收入来抵消API使用成本的话，那么这一通操作下来，就有可能会赔钱。

**01 变相「开源」GPT-4**

现在，想要用上GPT-4，除了直接充会员外，就只能排队等API，然后继续氪金……

而GPT4Free，则可以让我们通过You.com、Quora和CoCalc等网站，免费使(bai)用(piao)GPT-4和GPT-3.5模型。

同时，GPT4Free配置起来也非常简单。

首先，在电脑上的WSL2（Windows Subsystem for
Linux）安装GPT4Free。这只需要几分钟，包括克隆GitHub仓库，使用pip安装一些必需的库，以及运行一个Python脚本。

启动脚本后，使用浏览器访问http://localhost:8501，就可以获得一个聊天机器人了。

![](https://inews.gtimg.com/newsapp_bt/0/15787581128/1000)

在后端，GPT4Free利用的是像You.com这类通过GPT-3.5/GPT-4来提供答案的网站，所使用的各种API地址。

具体来说，GPT4Free脚本会先访问https://you.com/api/streamingSearch，并传送各种参数过去，然后获取返回的JSON并对其进行格式化。

此外，GPT4Free仓库还有从Quora、Forefront和TheB等其他网站获取数据的脚本，任何开发者都可以基于这些脚本制作自己的聊天机器人。

对此，Xtekky表示：「大家可以通过只打开这些网站的标签页来实现同样的效果。我可以在我的浏览器上打开Phind、You等网站的标签页并发起大量请求。我的仓库只是以更简单的方式实现了这一点。」

![](https://inews.gtimg.com/newsapp_bt/0/15787581152/1000)

周日，Xtekky发布了一则公告称，他正在对自己的聊天机器人进行一些改进。

这个聊天机器人独立于GitHub仓库，主要是作为演示如何使用GPT4Free的实例。

Xtekky表示，他计划将聊天机器人迁移到一个不同的域名，将其重新命名为g4f（GPT4Free的缩写），并更改logo（现在的与OpenAI非常相似）。

![](https://inews.gtimg.com/newsapp_bt/0/15787581153/1000)_目前正在维护当中_

**02 被OpenAI找上门**

Xtekky表示，由于项目并没有直接连到该公司的API，OpenAI不应该因为他使用其他网站的API而针对他，尤其是这些API在公共网络上并没有得到保护。

「OpenAI也可以联系这些网站并警告/通知它们，然后与我合作撤下内容，但看起来这个（法律威胁）完全来自OpenAI，他们的意思基本上就是，我的这个项目是在直接攻击OpenAI，」Xtekky说道。

如果这些网站的所有者对他的脚本查询有问题，他们应该直接与他联系。比如，Xtekky已经应部分网站的要求，撤下了使用phind.com、ora.sh和writesonic.com的脚本。

或许更重要的是，Xtekky指出，这些网站可以通过常见的安全措施阻止外部使用其内部API，比如阻止来自非自家IP的API流量。

Xtekky表示，他已经建议给他写信的所有网站应该确保他们的API安全，但没有一个网站采取了相应措施。因此，即使他从自己的仓库撤下这些脚本，其他开发者也可以做同样的事情。

![](https://inews.gtimg.com/newsapp_bt/0/15787581154/1000)

现在，即便是面对OpenAI的警告，Xtekky还是决定保留这个仓库。并且，他还直接告诉OpenAI，如果他们想要撤下它，他们应该向GitHub而不是他本人提出正式请求。

「我认为他们之前联系我是为了迫使我自己删除这个仓库，」他说，「但正确的方式应该是通过GitHub提交正式的DMCA请求。」

而且，即便是GPT4Free从未存在过，只要这些网站的API继续没有保护，任何人都可以找到使用它们的方法。

「现在，GitHub的用户正在各处共享和托管这个项目，」Xtekky说，「删除我的仓库将无关紧要。」

参考资料：

https://www.tomshardware.com/news/openai-sends-shutdown-letter-to-gpt4free

https://github.com/xtekky/gpt4free

