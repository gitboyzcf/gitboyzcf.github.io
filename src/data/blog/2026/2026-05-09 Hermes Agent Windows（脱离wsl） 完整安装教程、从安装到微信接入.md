---
author: boyzcf
pubDatetime: 2026-05-09 11:51:34
modDatetime: 2026-05-12 15:19:58
title: Hermes Agent Windows 完整安装教程：从安装到微信接入
slug:
featured: false
draft: true
tags:
  - 模板
description: 模板详情
---

![[../../../assets/images/pub/rzyd.webp]]

## 目录


# Hermes Agent Windows 完整安装教程：从安装到微信接入

> **本文基于真实安装经验整理**，涵盖：Hermes Agent 安装、迁移到非系统盘、微信（clawBot）接入配置、常见问题排查。

---

## 一、Hermes Agent 是什么？

**Hermes Agent** 是由 [Nous Research](https://nousresearch.com) 开发的开源 AI Agent 框架。它可以把大语言模型（LLM）接入到各种消息平台（微信、Telegram、Discord 等），让 AI 成为你的"数字员工"，自动处理消息、执行任务、操作本地文件。

**Agent** 意为智能体，能够利用对话或者自住做出决策的机器人，相当于大脑负责调用各种技能（skills）、工具（tools），配合模型上下文协议（MCP）连接各种外部平台

**核心特性：**
- 🤖 支持多种 LLM 模型（OpenAI、Anthropic、Kimi、DeepSeek、Qwen、Mimo、本地模型等）
- 💬 多平台消息网关（微信、钉钉、飞书、Telegram、Discord、Slack 等）
- 🖥️ 直接操作你的电脑（文件、代码、浏览器）
- 🔧 可扩展的技能系统（Skills）
- 🕐 定时任务（Cron Jobs）

---

## 二、安装前准备

### 2.1 系统要求

| 项目 | 要求 |
|------|------|
| 操作系统 | Windows 10/11（64位） |
| Python | 3.10 或更高版本 |
| 内存 | 建议 8GB+ |
| 磁盘空间 | 至少 5GB 可用空间 |
| 网络 | 可访问 GitHub 和模型 API |

你不需要手动安装 Python、Node.js、ripgrep 或 ffmpeg。安装程序会发现缺失的部分并帮你安装。只要确保 git 可用（`git --version`）。

### 安装 Git（已安装可跳过）

Hermes 需要通过 Git 克隆代码，如果还没有安装：

1. 访问 [git-scm.com](https://git-scm.com/download/win) 下载安装包
2. 一路默认安装即可
3. 验证：`git --version`

---

## 三、安装 Hermes Agent


### 3.1 默认安装（C 盘）

在电脑左下角搜索框部分搜索并打开 **PowerShell**，右击以管理员的方式打开，然后运行下面命令：

```bash
# 安装
irm https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.ps1 | iex
```

等待⌛️一段时间。。。

无任何报错展示一下内容即为成功
![[../../../assets/images/2026/Pasted image 20260509133541.png]]


默认情况下，Hermes 的配置和数据会存放在：
- 配置文件：`C:\Users\<你的用户名>\.hermes\.env`
- 缓存数据：`C:\Users\<你的用户名>\.hermes\`


#### 开始配置
**注意:  出现选择下图这种选择,输入相对应的标号即可, 如下图 输入1  或 2,  输入后回车就是选择**

![[../../../assets/images/2026/Pasted image 20260509133659.png]]
这个是希望怎么配置hermes,根据情况选择,我这里选择 1 简单配置,后期可以通过`hermes setup`命令再次配置

![[../../../assets/images/2026/Pasted image 20260509134517.png]]

这个就是配置模型供应商,  因为我之前配置过Kimi模型,  这里 我还继续使用, **自己选择已有的供应商按要求输入key和请求地址**,  不知道的可以去供应商官网查看

![[../../../assets/images/2026/Pasted image 20260509135151.png]]
配置好选择模型版本,  可以在官网查看,  不同版本功能不同,  这里我选择**kimi2.6**

![[../../../assets/images/2026/Pasted image 20260509135313.png]]
这里选择hermes在哪个终端运行命令 ,  默认本地终端即可


![[../../../assets/images/2026/Pasted image 20260509135514.png]]
这里配置hermes消息平台, 就是接入飞书或者微信, 我这里选择默认(也可以选择跳过) , 后续通过 `hermes setup gateway` 可以再次配置

![[../../../assets/images/2026/Pasted image 20260509151200.png]]
我这里选择 14 接入微信平台, 选择完之后 就会出现一个二维码 用微信扫下，微信连接成功后，后续问题只选择默认就行
![[../../../assets/images/2026/Pasted image 20260509151908.png]]
微信连接配置完成后，图片中的问题回复y启动网关，先记住上面图片上的自己的**User ID**

此时微信号中 就会出现 **clawBot** 的AI小助手, 通过聊天就可以操作电脑


### 3.2 迁移到其他盘符（推荐，不需要则跳过）

**为什么要迁移？**
- C 盘空间有限，Hermes 的模型缓存、日志文件会逐渐增大
- 重装系统时数据不会丢失
- 更方便备份和管理

**迁移步骤：**


```bash
# 查看安装路径
hermes config path
# 移动hermes数据
move C:\Users\zcf\AppData\Local\hermes D:\hermes
# 在原位置创建符号连接为了环境变量还从c盘找
mklink /D C:\Users\zcf\AppData\Local\hermes D:\hermes
# 启动hermes，启动成功即为迁移成功
```



---

## 四、常见问题排查

### 6.1 安装问题

#### Q: `pip install` 报错权限不足

```bash
# 方案 1：用户级安装
pip install --user -e .

# 方案 2：使用虚拟环境（推荐）
python -m venv venv
source venv/Scripts/activate  # Windows Git Bash
pip install -e .
```

#### Q: `hermes` 命令找不到

```bash
# 检查 Python Scripts 是否在 PATH
echo $PATH | grep Python

# 临时添加
export PATH="$PATH:/c/Users/<用户名>/AppData/Local/Programs/Python/Python310/Scripts"
```

### 6.2 网关问题

#### Q: `schtasks /Create` 拒绝访问

**原因**：创建 Windows 计划任务需要管理员权限。

**解决**：
1. 右键 Git Bash →"以管理员身份运行"
2. 重新执行 `hermes gateway install`

**替代方案**（不需要管理员）：

```bash
# 手动创建用户级任务
schtasks /Create /TN "HermesGateway" /TR "hermes gateway run" /SC ONLOGON /RL LIMITED

# 或添加到启动文件夹
mkdir -p "$APPDATA/Microsoft/Windows/Start Menu/Programs/Startup"
echo "hermes gateway run" > "$APPDATA/Microsoft/Windows/Start Menu/Programs/Startup/hermes.bat"
```

#### Q: 网关启动后提示 "No user allowlists configured"

**原因**：安全机制，防止未授权访问。

**解决**：

```env
# 方案 1：配置白名单（推荐）
WEIXIN_DM_POLICY=allowlist
WEIXIN_ALLOWED_USERS=你的微信ID@im.wechat

# 方案 2：临时开放（不安全，仅测试）
GATEWAY_ALLOW_ALL_USERS=true
```

### 6.3 微信连接问题

#### Q: 微信状态显示 `disconnected`

```bash
# 1. 检查凭证
cat ~/.hermes/.env | grep WEIXIN

# 2. 检查网络
ping ilinkai.weixin.qq.com

# 3. 查看详细日志
cat ~/.hermes/logs/gateway.log | tail -n 50

# 4. 重启网关
hermes gateway restart
```

#### Q: 能收到消息但 AI 不回复

**排查步骤**：

1. 检查 LLM 配置是否正确（API Key 是否有效）
2. 查看 agent 日志：`cat ~/.hermes/logs/agent.log`
3. 检查模型额度是否用完
4. 尝试切换模型（如从 GPT-4 换到 GPT-4o-mini）

### 6.4 磁盘/路径问题

#### Q: 如何确认 Hermes 正在使用 D 盘？

```bash
# 查看当前配置路径
hermes config env-path

# 查看运行状态
hermes gateway status

# 检查状态文件
cat /d/hermes/gateway_state.json

# 应包含：
# {
#   "platforms": {
#     "weixin": {
#       "state": "connected",
#       "account": "4534b6a2"
#     }
#   }
# }
```

---

## 五、进阶配置

### 5.1 多平台同时接入

Hermes 可以同时接入多个平台：

```env
# 微信 + Telegram 同时在线
WEIXIN_TOKEN=xxx
WEIXIN_ACCOUNT_ID=xxx
TELEGRAM_BOT_TOKEN=xxx
TELEGRAM_ALLOWED_USERS=your_telegram_id

# 平台策略
WEIXIN_DM_POLICY=allowlist
TELEGRAM_DM_POLICY=allowlist
```

### 5.2 自定义技能（Skills）

Hermes 支持通过 Skills 扩展功能：

```bash
# 查看可用技能
hermes skills list

# 加载技能
hermes skills load web-search
hermes skills load file-manager

# 在对话中使用
# 用户：搜索今天的 AI 新闻
# Hermes 会自动调用 web-search 技能
```

### 5.3 定时任务

```bash
# 每天早上 9 点发送日报
hermes cron create --name "morning-report" --schedule "0 9 * * *" --command "生成今日待办事项"

# 查看定时任务
hermes cron list
```

---

## 六、目录结构参考

迁移到 D 盘后的典型目录结构：

```
D:\hermes\
├── .env                    # 主配置文件
├── gateway_state.json      # 网关状态
├── logs\
│   ├── gateway.log         # 网关日志
│   └── agent.log           # Agent 日志
├── cache\
│   ├── terminal\            # 终端快照
│   └── models\             # 本地模型缓存（如有）
├── skills\                 # 自定义技能
└── cron\                   # 定时任务配置
```

---

## 七、总结

通过本文，你应该已经：

✅ 成功安装 Hermes Agent  
✅ 将数据目录迁移到非系统盘（如 D 盘）  
✅ 配置并接入了微信（clawBot/iLink AI）  
✅ 解决了常见的安装和连接问题  

**下一步建议：**
1. 探索更多平台接入（Telegram、Discord）
2. 编写自定义 Skills 扩展功能
3. 设置定时任务实现自动化
4. 加入 [Hermes 社区](https://github.com/NousResearch/hermes-agent/discussions) 交流

---

> 📌 **提示**：本文基于 Windows 11 + PowerShell/Git Bash 环境编写。如果你使用 PowerShell 或 WSL，部分命令可能需要调整。
> 🔒 **安全提醒**：生产环境务必配置白名单（`WEIXIN_ALLOWED_USERS`），不要长期开启 `GATEWAY_ALLOW_ALL_USERS=true`。







<br/><br/><br/><br/>
**到这里就结束了，后续还会更新 Vue 系列相关，还请持续关注！**
**感谢阅读，若有错误可以在下方评论区留言哦！！！**

![[../../../assets/images/pub/clw.webp#pic_center)]]

<br/><br/>