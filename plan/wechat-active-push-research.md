# 微信主动推送调研

## 结论

当前 cc-connect 的个人微信通道可以接收你主动发来的消息，并在会话里回复；但云端定时主动发送会被微信侧拒绝，日志表现为 `weixin: sendMessage: ret=-2`。因此它不适合作为稳定的睡前主动提醒通道。

最适合当前学习提醒的落地方式是：用微信服务号/接口测试号的模板消息，把“睡前复习提醒”主动推送到你的微信。它是官方接口、能到普通微信，但偏单向通知；你回复后的深度聊天仍走现有 cc-connect 会话。

如果以后想把“主动提醒 + 微信里持续对话 + Agent 命令”合在一起，更长期的方案是企业微信/WeChat Work 自建应用或机器人。cc-connect 本身支持 WeChat Work，但需要 `corp_id`、`corp_secret`、`agent_id` 等企业微信应用凭据。

## 方案 A：微信服务号/接口测试号模板消息

用途：每天睡前主动发一条复习提醒到普通微信。

需要你手动准备一次：

1. 打开微信公众平台接口测试号或服务号后台。
2. 拿到 `AppID` 和 `AppSecret`。
3. 用你的微信关注测试号，拿到你的 `OpenID`。
4. 新建一个模板，建议字段为：`title`、`time`、`content`、`remark`。
5. 拿到模板 ID。

云端已准备脚本：

```bash
python3 tools/wechat_template_push.py --dry-run \
  --content "今天睡前复习 5 分钟：回顾一个概念、一道错题、一个明天要继续的问题。"
```

正式运行前，把下面变量放在云端私密环境里，不写入 Git：

```bash
export WECHAT_MP_APPID="你的 AppID"
export WECHAT_MP_SECRET="你的 AppSecret"
export WECHAT_MP_OPENID="你的 OpenID"
export WECHAT_MP_TEMPLATE_ID="你的模板 ID"
```

确认能发出后，再接回每天 21:40 或睡前时间的定时任务。

## 方案 B：企业微信 / WeChat Work

用途：如果希望 cc-connect 本身支持主动消息、命令和连续对话，可以迁到企业微信应用/机器人。

需要准备：

- 企业微信企业 ID：`corp_id`
- 自建应用 Secret：`corp_secret`
- 应用 ID：`agent_id`
- 如走回调，还需要 callback token 与 AES key

优点是更适合 Agent 长期运行；缺点是配置链路比测试号模板消息重，且接收体验更接近企业微信应用通知。

## 不建议作为主方案

第三方聚合推送服务虽然上手更快，但学习复盘、日记素材、生活记录可能包含隐私。除非只推送很短的无敏感提醒，否则不建议把它作为主通道。

## 官方资料

- 微信服务号模板消息：https://developers.weixin.qq.com/doc/service/guide/product/template_message/Template_Message_Interface.html
- 微信服务号开发指南：https://developers.weixin.qq.com/doc/service/guide/dev/
- 企业微信发送应用消息：https://developer.work.weixin.qq.com/document/path/90236
- 企业微信消息推送配置：https://developer.work.weixin.qq.com/document/path/91770
- cc-connect 项目说明：https://github.com/chenhg5/cc-connect