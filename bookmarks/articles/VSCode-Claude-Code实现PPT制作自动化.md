# VSCode + Claude Code 实现 PPT 制作自动化

来源：知乎专栏 `skills合辑`
作者：RunfarAI AI | LLM算法
日期：2026-05-15
链接：https://zhuanlan.zhihu.com/p/2036573821294088294

## 核心内容

用 VSCode + Claude Code 插件 + DeepSeek V4 Pro 自动生成 PPT。

## 环境配置

1. **VSCode** + **Claude Code 插件**（扩展商店安装）
2. **Python 3.10+** + **Anaconda 虚拟环境**
3. **DeepSeek V4 Pro** API（5月底前打2折）→ CC Switch 配置 API Key
4. 在 `settings.json` 中配置 `claudeCode.environmentVariables`

## 方案一：ppt-master（推荐）

- GitHub: `github.com/hugohe3/ppt-master`
- 生成的是**真正可编辑的 pptx 文件**（SVG + 文本，不是一张大图）
- 需要 conda 虚拟环境安装依赖
- 在 Claude Code 输入需求即可自动生成
- 作者评价：几乎碾压普通 PPT 制作者

```bash
conda create -n ppt-maker python=3.12
cd ppt-master
conda activate ppt-maker
pip install -r requirements.txt
```

测试命令：`请创建一个 3 页测试 PPT，封面 + 内容页 + 封底，主题"Hello World"`

## 方案二：axi-front-design-skill

- GitHub: `github.com/bbostaice/axi-front-design-skill`
- 生成 HTML 格式伪 PPT，需用 `claude-office-skills` 转为 pptx
- 效果不如方案一

## 标签

`PPT自动化` `Claude Code` `DeepSeek` `AI工具` `效率`
