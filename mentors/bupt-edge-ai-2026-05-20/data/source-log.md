# Source Log - BUPT Edge AI Mentor Research

更新时间：2026-05-20 11:16-12:40 CST

## Source Policy
- 在职与方向优先使用北邮官方页面、学院导师表和招生 PDF。
- 论文元数据优先使用 OpenAlex；姓名高度重名时不自动归属，改写“需人工复核”。
- 不下载盗版论文全文，只保存公开元数据、DOI/URL、摘要线索和阅读建议。

## Official Sources
| ID | Source | Status | Use |
|---|---|---|---|
| SCS-04-PDF | https://scs.bupt.edu.cn/__local/8/73/8C/CCB861FF245158D36385A36F04C_28951161_D9026.pdf?e=.pdf | downloaded/parsed | 计算机04组：卞佳丽、戴志涛、蒋砚军、高占春、张成文；嵌入式人工智能、移动智能感知、智能硬件。 |
| SCS-contact | https://scs.bupt.edu.cn/info/1305/2982.htm | direct fetch returned 412; search cache used | 计算机学院导师页；用于确认多位计算机学院候选的当前导师页存在和方向摘要。 |
| SEE-team-detail | https://see.bupt.edu.cn/__local/E/F9/0C/F093AC0665CC74B5BD22FBC9250_B85693F2_133C9B.pdf | downloaded/parsed | 电子工程学院09组详细介绍：王莉、王小娟、宋梅组等。 |
| SEE-team-list | https://xxgk.bupt.edu.cn/__local/F/FE/1E/C8D4C8D67CD2C387365EC47775C_840ECE9B_24EAB.pdf | downloaded/parsed | 电子工程学院导师组总表：范春晓组、张洪欣组、张琦组等。 |
| AI-Zhang-Lin | https://ai.bupt.edu.cn/kxyj/yjfx.htm | direct fetch returned 412/search cache used | 人工智能学院张琳团队：智能边缘计算、车联网分布式AI、边缘智能信息处理。 |
| ICT-direction | https://xxgk.bupt.edu.cn/info/1079/2451.htm | direct fetch returned 412/search cache used | 信通院方向15：无线通信与边缘智能，招生导师含冯春燕、郭彩丽、张天魁等。 |

## Paper Metadata Sources
| ID | URL | Use |
|---|---|---|
| OpenAlex | https://docs.openalex.org/ | 主论文元数据；按 BUPT institution `I139759216` 和作者 ID 抓取。 |
| Semantic Scholar | https://www.semanticscholar.org/product/api | 备用论文索引；本次未批量调用，后续可用于补引用和摘要。 |
| DBLP | https://dblp.org/ | 备用 CS 论文索引；适合计算机学院老师二次核验。 |
| Crossref | https://www.crossref.org/documentation/retrieve-metadata/rest-api/ | DOI 备用元数据。 |

## Known Limitations
- 北邮多个 HTML 页面在 PowerShell 抓取时返回 HTTP 412；报告保留可访问 URL，并用搜索缓存摘要、可下载 PDF、OpenAlex 论文元数据交叉验证。
- `Li Wang`、`Qi Zhang`、`Fang Zhao`、`Lin Zhang`、`Na Liu` 等英文名高度重名，未把不确定 OpenAlex 论文硬归属到候选老师。
- 国内论文库（知网/万方/维普）公开元数据通常需要人工检索或登录，本次仅记录公开可核验线索，不抓取付费库全文。
