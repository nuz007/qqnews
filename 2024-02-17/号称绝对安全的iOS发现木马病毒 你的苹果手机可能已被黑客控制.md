# 号称绝对安全的iOS发现木马病毒 你的苹果手机可能已被黑客控制

# 号称绝对安全的iOS发现木马病毒 你的苹果手机可能已被黑客控制

![](https://inews.gtimg.com/news_bt/O_JfWJfqcYDn79PevXyDBc1-aOwjj3DubbzFRJlwGiRJoAA/1000)

**划重点**

  * _1_ 网络安全公司Group-IB发现了首款针对iOS系统的木马病毒。
  * _2_ GoldDigger原本是针对安卓系统开发的，现在的改进版本开始威胁iOS用户。
  * _3_ 苹果似乎已经发现这种病毒的威胁，并采取了封锁措施。

**腾讯科技讯**
2月17日消息，据外媒报道，苹果始终致力于为其操作系统提供安全补丁，然而这些补丁却常常成为黑客攻击用户的手段。近期，网络安全公司Group-
IB揭露了一种名为“GoldDigger”的新型木马病毒，其目标是针对iOS用户，企图窃取他们的银行账户信息。

![](https://inews.gtimg.com/news_bt/OlBO6GKY_9HYRT-
BJomZdvU4j2k6lR44V2Kpm_RymchnYAA/1000)

据悉，GoldDigger木马病毒最初是为安卓系统开发的，但现已成功被移植至iPhone和iPad平台。Group-
IB公司警告称，这可能是首个针对iOS的木马，其危害程度可能极高，因为它具备收集用户面部识别数据、身份证件以及短信的能力。

掌握这些信息后，黑客会运用先进的人工智能工具进行深度伪造，进而非法侵入受害者的银行账户。当受害者意识到账户遭到入侵时，往往为时已晚。

![](https://inews.gtimg.com/news_bt/OSyjNYYkrRQtsglXtFacHaxKAcJ6asv2q-oVqQaf3DyJ0AA/1000)
_图1：GoldDigger变种的首个恶意软件样本_

最初，GoldDigger通过苹果的TestFlight平台传播，该平台允许开发者发布应用程序的测试版，无需经过应用商店的审核程序。然而，在苹果迅速将其从TestFlight中移除后，黑客不得不采用更为复杂的手段，即利用移动设备管理（MDM）配置文件。这些配置文件通常用于企业管理其设备，但黑客却将其用于诱骗用户安装恶意软件，从而绕过应用商店下载应用程序。一旦得逞，他们便能收集到所需的敏感信息。

目前，GoldDigger的主要攻击目标是越南和泰国的用户。然而，该木马同样具备攻击全球其他地区用户的能力。Group-
IB强调，这款木马病毒正处于“活跃进化阶段”，其威胁不容忽视。

**Group-IB的关键发现**

——Group-IB的威胁情报部门发现了一个以前不为人知的iOS木马病毒GoldPickaxe.iOS，它会收集身份证件、短信和面部识别数据。

——GoldPickaxe木马病毒在iOS和安卓平台都存在。

——GoldFactory开发的复杂木马套件自2023年年中以来一直处于活跃状态。

![](https://inews.gtimg.com/news_bt/OvxUUKR9FQePbw2ChsPkLsIjF9l22vL9Ts-
azWPVv8U1YAA/1000)

——GoldFactory可能是个组织严密的网络犯罪集团，与新型银行木马Gigabud关系密切。

——社会工程是将恶意软件传递到整个GoldFactory特洛伊木马家族受害者设备上的主要方法。

——GoldPickaxe.iOS通过苹果的TestFlight或通过社交工程让受害者安装MDM配置文件扩散。

——GoldPickaxe木马收集面部资料、身份证件、拦截短信。为了利用从iOS和安卓用户那里窃取的生物识别数据，网络犯罪分子使用人工智能换脸服务进行深度伪造，将他们的脸替换成受害者的脸。这种方法可能被网络犯罪分子用来访问未经授权的受害者银行账户。

——由GoldFactory开发的木马病毒受害者多位于越南和泰国。

——在关于GoldDigger的初步报告发布后，Group-IB的研究人员发现了一种名为GoldDiggerPlus的恶意软件新变体。

——GoldDiggerPlus扩展了GoldDigger的功能，并使威胁行为者能够实时呼叫其受害者。

——它是通过特殊设计的APK实现的，被Group-
IB称为GoldKefu。当受害者点击联系客服按钮试图警报时，GoldKefu会检查当前时间是否在网络犯罪分子设置的工作时间内。如果是这样的话，该恶意软件将试图找到一个空闲的接线员进行呼叫。这就像是网络罪犯在运营一个真正的客户服务中心。

——Group-IB发现的所有特洛伊木马都处于活跃的进化阶段。

**四大GoldDigger木马病毒变种**

早在2023年10月，Group-
IB就发布了一份震撼的报告，揭示了一个之前鲜为人知的安卓木马——GoldDigger，该木马专门针对越南的50多家金融机构发动猛烈攻击。GoldDigger之所以得名，是因为其APK文件中包含了一个名为GoldActivity的攻击活动。自首次发现这个木马以来，Group-
IB的威胁情报部门持续对其进行严密监控，并发现了一个令人不安的现象：一个针对亚太地区的庞大攻击性银行木马病毒集群。

![](https://inews.gtimg.com/news_bt/O_koZAIoyQBpNe28cGXjugw6phbMHTEQrpCkYe7xj9KzQAA/1000)

在这个集群中，有一个尤为引人注目的新型移动木马病毒，专门针对iOS用户，被命名为GoldPickaxe.iOS。

据Group-
IB研究人员发现，GoldPickaxe.iOS具备收集面部识别数据、窃取身份文件以及拦截短信的能力。与此同时，它的安卓版本也拥有相同功能，并且还展示了安卓木马的其他典型特征。

Group-
IB将这一整个威胁集群归咎于名为GoldFactory的威胁行为者。GoldFactory开发了一套高度复杂的移动银行恶意软件，主要针对亚太地区的用户。尽管目前的证据显示该病毒特别关注两个亚太国家，但有迹象表明，GoldFactory的业务范围可能会扩展到越南和泰国以外的地区。Group-
IB已经向受到GoldFactory木马攻击的品牌发出了通知，提醒他们加强安全防范。

![](https://inews.gtimg.com/news_bt/OZL5eUs75Mf1Oh5SnosgSALee8KPron8zW7tjGejMz4dkAA/1000)
_图2：GoldFactory特洛伊木马演变时间轴_

**GoldPickaxe.iOS的两条感染途径**

GoldPickaxe.iOS的扩散方式与众不同。

CryptoRAM活动就是一个典型案例，犯罪分子利用苹果的TestFlight平台分发假冒的加密货币应用。TestFlight原本是开发者在苹果应用商店正式发布iOS应用前，用于分发和测试应用的工具。它提供了多种测试方法，并允许开发者邀请用户测试他们的应用。

![](https://inews.gtimg.com/news_bt/Osq9Bd6mEOvaCvd-
_L9vbuORPgYIccgGKdaz3GqKBqm5wAA/1000)

另一种策略则涉及通过移动设备管理（MDM）操控苹果设备。MDM是一种全面而集中的解决方案，用于管理和保护组织内的移动设备，如智能手机和平板电脑。其主要目标是简化设备管理任务、增强安全性、确保符合组织策略以及部署应用程序。在苹果生态系统中，MDM允许通过向设备发送配置文件和命令来无线配置设备。

值得注意的是，TestFlight方法在GoldFactory的恶意活动中仅用于早期阶段。然而，随着网络犯罪分子转向使用MDM方法，战略上发生了重大转变。

这种转变的原因可能在于，上传至TestFlight的应用程序需要提交给苹果的审查程序。在撰写本文时，TestFlight无法访问iOS木马病毒，这可能是因为苹果的审查已经发现了GoldPickaxe.iOS恶意软件并采取了封锁措施。因此，网络犯罪分子调整了他们的分发策略，选择了MDM方法来绕过与TestFlight相关的严格控制，继续他们的非法活动。

Group-IB已经向苹果公司通报了关于GoldFactory活动的信息。（编译/金鹿）

