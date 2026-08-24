---
author: boyzcf
pubDatetime: 2026-07-07 18:00:00
modDatetime: 2026-08-24 14:35:54
title: 初识LangChain 02：从零搭建 LangChain 开发环境（Miniconda + Windows 详细版）
slug:
featured: false
draft: false
tags:
  - LangChain
  - AI智能体
  - 环境搭建
  - Python
  - Miniconda
  - 零基础入门
description: 从零搭建 LangChain 开发环境：安装 Miniconda、创建虚拟环境、安装 LangChain 1.2、跑通第一行代码。Windows 版小白也能跟着做。
---

![[../../../assets/images/pub/rzyd.webp]]

## 目录

# 初识 LangChain 02：从零搭建开发环境（Miniconda + Windows 详细版）

> 本文整理自 [尚硅谷 LangChain 1.2 概述课程](https://www.atguigu.com/) 与 [尚硅谷 conda 使用指南](https://www.atguigu.com/)，是「初识 LangChain」系列连载第 2 篇。
> 
> 📌 上一篇回顾：[初识 LangChain：给 AI 小白的第一本说明书](../../../data/blog/2026/%E6%9C%AA%E5%91%BD%E5%90%8D.md)

---

## 🤔 先打个底：这件事其实不难

上一篇我们聊了 LangChain 是什么、能做什么。从今天开始，我们就要**真正动手**了。

我知道很多小白一听"开发环境"四个字就头大：

- Python 怎么装？
- Miniconda 是什么？和 Anaconda 有什么区别？
- 环境变量怎么配？
- 安装失败一堆红字怎么办？

别怕，这篇文章就是来解决这些问题的。**你不用懂原理，跟着点下一步就行。**

**我们要达成的目标**：

```
✅ 装好 Python 和 Miniconda
✅ 创建一个干净的虚拟环境
✅ 在环境里装好 LangChain 1.2
✅ 在 PyCharm 里跑通你的第一行 LangChain 代码
```

---

## 一、工欲善其事：先认识三个工具

在动手之前，我们先搞清楚三个概念。你可以把它们当成三个角色：

| 工具 | 角色 | 作用 |
|------|------|------|
| **Python** | 编程语言 | LangChain 是用 Python 写的，所以必须先装 Python |
| **Miniconda** | 管家 | 帮你管理多个 Python 版本、安装包、管理环境 |
| **PyCharm** | 编辑器 | 专门写 Python 的 IDE，功能强大，小白友好 |

**三者的关系**：

```
Miniconda（管家）
   ├── 给你安装 Python 3.13
   ├── 创建虚拟环境 langchain1.2
   └── 在环境里安装 LangChain 包
         ↑
    PyCharm（编辑器）连接这个环境
         ↓
    你在这里写代码、运行代码
```

![[../../../assets/images/2026/langchain-diagrams/setup-workflow.svg]]

> 📌 **图1 解读**：这张图展示了我们今天要完成的四个步骤：安装 Miniconda → 创建虚拟环境 → 安装 LangChain → 在 PyCharm 里跑通第一行代码。每一步都是环环相扣的，只要按顺序做，就能成功。

---

## 二、安装 Python + Miniconda（Windows 版）

### 2.1 为什么要用 Miniconda 而不是直接装 Python？

你可能听说过"去 Python 官网下载安装包"这种方式。对于只写一个 Hello World 的小脚本，没问题。但学 LangChain 会涉及到很多第三方库，直接用系统 Python 很容易出现这种麻烦：

- 这个库需要 Python 3.10，你装的是 3.9 ❌
- 这个库和那个库版本冲突 ❌
- 装太多东西把系统环境搞乱了 ❌

Miniconda 的**核心作用**就是：

> 在你的电脑里创建一个个"独立的房间"（虚拟环境），每个房间里有自己的 Python 和依赖，互不干扰。

LangChain 项目住一个房间，其他项目住另一个房间，大家井水不犯河水。

### 2.2 Miniconda vs Anaconda：选哪个？

| 对比项 | Miniconda | Anaconda |
|--------|-----------|----------|
| 体积 | 小（约 400MB） | 大（约 3GB+） |
| 预装包 | 极少，只包含 conda、Python 和基础依赖 | 很多，包含大量科学计算包 |
| 安装速度 | 快 | 慢 |
| 灵活性 | 高，按需安装 | 开箱即用，但可能装很多用不到的 |
| 适合人群 | 知道自己需要什么的人、小白入门 | 数据科学全家桶用户 |

> 💡 **为什么推荐 Miniconda？**> 
> 对于学 LangChain 来说，你不需要 Anaconda 里那一大堆科学计算包。Miniconda 体积小、安装快、按需安装，**更适合我们现在的需求**。

### 2.3 下载 Miniconda

**步骤一：访问官网**

打开浏览器，访问 Miniconda 官方下载地址：

[https://www.anaconda.com/download/success](https://docs.conda.io/projects/conda/en/stable/)

![[../../../assets/images/2026/Pasted image 20260722164947.png]]

**步骤二：选择 Windows 版本下载**

> ⚠️ **注意**：如果你的电脑是 Windows 32 位或者特别老旧的系统，可能无法安装最新版。绝大多数现代电脑都是 64 位。

### 2.3 安装 Miniconda

**步骤三：运行安装程序**

双击下载好的 `.exe` 文件，你会看到安装向导

安装过程中注意以下几点：

1. **安装路径**：
   - 默认是 `C:\Users\你的用户名\miniconda3`
   - 如果 C 盘紧张，可以改成 `D:\miniconda3`
   - **路径里不要有中文和空格** ⚠️

![[../../../assets/images/2026/miniconda/p04_img1.png]]

> 📌 **图3解读**：这里选择 Miniconda 的安装路径。建议使用默认路径，或者改到 D 盘根目录下。记住这个路径，后面配置环境变量会用到。

2. **推荐选项**：
   - 勾选 **"Create shortcuts"**（创建快捷方式）
   - 勾选 **"Register Miniconda3 as the system Python 3.12"**（把 Miniconda 注册为系统 Python）
   - 勾选 **"Add Miniconda3 to my PATH environment variable"**（添加到环境变量，非常重要！）

![[../../../assets/images/2026/miniconda/p05_img1.png]]

> 📌 **图4解读**：这一步非常关键。建议勾选 **"Add Miniconda3 to my PATH environment variable"**，这样你就可以在普通的 CMD 或 PowerShell 中直接使用 `conda` 命令。如果安装时没勾选，不用担心，后面我会教你手动配置环境变量。

3. **一路 Next，最后点击 Install**

安装过程可能需要 3-5 分钟，耐心等待，不要关闭窗口。

![[../../../assets/images/2026/miniconda/p06_img1.png]]

> 📌 **图5解读**：看到这个界面表示 Miniconda 安装完成。取消勾选"Anaconda 教程"等无关选项，然后点击 **Finish**。

### 2.4 验证安装成功

**方法一：打开 Anaconda Powershell Prompt**

安装 Miniconda 后，会附带一个 **Anaconda Powershell Prompt**。按 `Win + S`，搜索它并点击打开：

![[../../../assets/images/2026/miniconda/p07_img1.png]]

> 📌 **图6解读**：这就是 Miniconda 自带的终端。注意命令行前面有 `(base)`，这表示当前在 conda 的 base 基础环境中。

打开后输入：

```bash
conda --version
python --version
```

![[../../../assets/images/2026/miniconda/p07_img2.png]]

> 📌 **图7 解读**：如果看到 `conda` 和 `python` 的版本号，说明 Miniconda 安装成功。图中显示的是 Miniconda 自带的 Python 版本，这个版本后面我们会通过创建虚拟环境来管理。

**方法二：用普通 CMD 验证（如果配置了 PATH）**

如果你安装时勾选了"Add to PATH"，可以按 `Win + R`，输入 `cmd`，打开普通命令提示符：

```bash
conda --version
```

![[../../../assets/images/2026/miniconda/p11_img1.png]]

> 📌 **图8解读**：在普通 CMD 中也能运行 `conda --version`，说明环境变量配置正确。如果这里提示"conda 不是内部命令"，则需要检查或手动配置环境变量（见下一节）。

---

## 三、环境变量配置（如果没勾选 PATH）

### 3.1 什么情况下需要手动配置？

如果你安装 Miniconda 时**没有勾选** "Add Miniconda3 to my PATH environment variable"，那么普通 CMD 里输入 `conda` 会提示找不到命令。这时需要手动配置环境变量。

### 3.2 配置步骤

**步骤一：打开环境变量设置**

1. 右键"此电脑" → 选择"属性"
2. 点击"高级系统设置"
3. 点击"环境变量"

![[../../../assets/images/2026/miniconda/p09_img1.png]]

> 📌 **图9 解读**：这是 Windows 系统属性界面。点击"环境变量"按钮后，会弹出环境变量编辑窗口。

**步骤二：编辑 PATH 环境变量**

1. 在"系统变量"或"用户变量"中找到 **Path**
2. 点击"编辑"
3. 点击"新建"，依次添加以下三个路径（根据你的实际安装路径调整）：

```
D:\miniconda3
D:\miniconda3\Scripts
D:\miniconda3\Library\bin
```

![[../../../assets/images/2026/miniconda/p09_img2.png]]

![[../../../assets/images/2026/miniconda/p10_img1.png]]

> 📌 **图10 解读**：这张图展示了如何把 Miniconda 的三个关键路径添加到 PATH 中。注意：如果你安装到了 C 盘，路径就是 `C:\Users\你的用户名\miniconda3`，要改成你自己的实际路径。

**步骤三：验证**

配置完成后，**重新打开一个 CMD 窗口**（注意：必须重新打开，之前的窗口不会生效），输入：

```bash
conda --version
```

如果显示版本号，说明配置成功 ✅

---

## 四、创建 LangChain 专属虚拟环境

### 4.1 为什么要创建虚拟环境？

前面说过，虚拟环境就像一个个独立的房间。我们给 LangChain 专门创建一个房间，里面只装 LangChain 需要的东西：

![[../../../assets/images/2026/langchain-diagrams/virtual-env.svg]]

> 📌 **图11 解读**：这张图把虚拟环境比喻成电脑里的独立房间。每个环境（A、B、C）都有自己的 Python 版本和依赖包，互不干扰。LangChain 项目住在"环境 B"里，即使其他环境出问题了，也不会影响它。这就是 Miniconda 的核心价值——**环境隔离**。

- Python 3.13（LangChain 1.2 要求 Python 3.10+）
- LangChain 1.2 包
- 后续学习中用到的其他依赖

这样做的好处：
- 不会污染你电脑里的其他 Python 环境
- 想删就删，干净利落
- 项目迁移方便，换电脑把环境一导出就能复现

### 4.2 创建环境

**步骤一：打开 Anaconda Powershell Prompt**

按 `Win + S`，搜索 **Anaconda Powershell Prompt**，右键选择"以管理员身份运行"（可选，但推荐）。

**步骤二：创建环境**

在窗口中输入以下命令，然后按回车：

```bash
conda create --name langchain1.2 python=3.13.12
```

这条命令的意思是：
- `conda create`：创建环境
- `--name langchain1.2`：环境名字叫 `langchain1.2`
- `python=3.13.12`：安装 Python 3.13.12 版本

输入后，终端会询问你是否继续：

```
Proceed ([y]/n)?
```

输入 `y`，按回车。

📷 【截图位置：终端显示创建环境过程，以及输入 y 确认的画面】

等待片刻，环境就创建好了。完成后会显示：

```
# To activate this environment, use
#
#     $ conda activate langchain1.2
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```


### 4.3 激活环境

**激活环境**就是"进入这个房间"。输入：

```bash
conda activate langchain1.2
```

如果成功，命令行前面会出现 `(langchain1.2)`：

```bash
(langchain1.2) C:\Users\你的用户名>
```


### 4.4 验证 Python 版本

在激活环境中输入：

```bash
python --version
```

或者：

```bash
python -V
```

如果显示 `Python 3.13.12`，说明环境正确 ✅


### 4.5 常用环境管理命令（建议收藏）

![[../../../assets/images/2026/miniconda/p12_img1.png]]

> 📌 **图12 解读**：这张图列出了 conda 的常用命令，包括环境管理和包管理。建议收藏，学 LangChain 过程中会经常用到。

```bash
# 查看所有环境
conda env list

# 激活某个环境
conda activate langchain1.2

# 退出当前环境
conda deactivate

# 删除某个环境
conda remove --name langchain1.2 --all
```


---

## 五、安装 LangChain 1.2

### 5.1 选择安装方式

在激活的 `langchain1.2` 环境中，我们可以用两种方式安装 LangChain：

**方式一：conda 安装（推荐）**

```bash
conda install langchain==1.2.12
```

如果找不到包，可以指定 conda-forge 源：

```bash
conda install -c conda-forge langchain==1.2.12
```

**方式二：pip 安装（备选）**

如果 conda 安装失败，或者你想用国内的镜像源加速下载，可以用 pip：

```bash
pip install langchain==1.2.12
```

国内镜像加速（推荐）：

```bash
pip install langchain==1.2.12 -i https://pypi.tuna.tsinghua.edu.cn/simple
```


### 5.2 为什么要指定版本？

LangChain 版本变化非常频繁，不同版本之间 API 差异很大。上一篇我们讲过，**v1.x 是稳定版本，推荐学习和使用**。

所以我们直接安装 `1.2.12`（版本号可以根据课程要求调整），而不是安装最新的：`pip install langchain`（可能装到不稳定版本，不推荐）。

### 5.3 验证安装成功

安装完成后，在终端中输入：

```bash
python -c "import langchain; print(langchain.__version__)"
```

如果输出 `1.2.12`，说明安装成功 ✅


### 5.4 安装常用伙伴包

LangChain 通常会和一些"伙伴包"一起使用，比如：

```bash
# 安装 OpenAI 接口（如果要调用 GPT 系列）
pip install langchain-openai

# 安装 DeepSeek 接口（国产模型，性价比高）
pip install langchain-deepseek

# 安装社区集成（各种第三方工具和数据源）
pip install langchain-community
```

这些是后续课程会用到的东西，现在先安装也可以，等用到再安装也行。

---

## 六、安装 PyCharm：你的代码编辑器

### 6.1 为什么推荐 PyCharm？

写 Python 代码，你可以用记事本、VS Code、Jupyter Notebook，但 **PyCharm 是专业写 Python 的 IDE**，最适合新手：

- 代码自动补全：你输入一半，它帮你补全
- 错误提示：写错了会实时红字提示
- 一键运行：写完代码点一下就能跑
- 调试方便：代码出问题可以一步步看

### 6.2 下载 PyCharm

访问官网：[https://www.jetbrains.com/pycharm/download/](https://www.jetbrains.com/pycharm/download/)

选择 **PyCharm Community Edition**（社区版，免费够用）：

> 打开 [PyCharm 官网下载页](https://www.jetbrains.com/pycharm/download/)，选择免费的 **Community Edition** 下载即可。

### 6.3 安装 PyCharm

1. 双击下载的 `.exe` 文件
2. 选择安装路径（默认即可）
3. 勾选以下选项：
   - 64-bit launcher（根据你的系统）
   - Add "Open Folder as Project"（推荐勾选）
   - Add to PATH（推荐勾选）

> 安装过程中勾选 **64-bit launcher**、**Add "Open Folder as Project"** 和 **Add to PATH** 即可。

4. 一路 Next，完成安装

### 6.4 创建第一个 LangChain 项目

**步骤一：打开 PyCharm**

双击桌面 PyCharm 图标，启动后选择 **New Project**：

> 打开 PyCharm 后，点击 **New Project** 创建新项目。

**步骤二：配置项目位置**

- Location：项目保存路径，比如 `D:\projects\langchain-learning`
- 命名：可以叫 `langchain-learning`

> 在 **New Project** 窗口中，填写项目保存路径（如 `D:\projects\langchain-learning`），项目名称设为 `langchain-learning`。

**步骤三：配置 Python 解释器（关键！）**

这是最关键的一步！

1. 在 **Interpreter** 区域，选择 **Add Interpreter** → **Add Local Interpreter**

2. 在弹出的窗口中，左侧选择 **Conda Environment**

3. 选择 **Use existing environment**

4. 在下拉菜单中，选择你刚才创建的 `langchain1.2`

> 配置解释器：左侧选择 **Conda Environment**，右侧选择 **Use existing environment**，然后在下拉框里找到 `langchain1.2`。这样 PyCharm 就会使用这个环境里安装的 Python 和 LangChain。

5. 点击 **OK**，然后点击 **Create**

> 配置完成后，可以在 PyCharm 的设置中查看当前项目使用的解释器，确认这里显示的是 `langchain1.2` 环境。

### 6.5 验证解释器配置正确

创建项目后，看右下角状态栏：

- 应该显示 `langchain1.2`（或者类似 Python 3.13 的标识）

> 创建项目后，看 PyCharm 右下角状态栏，应显示 `langchain1.2` 或 `Python 3.13`。

如果不正确，可以手动修改：

1. 点击右下角解释器名称
2. 选择 **Add New Interpreter** → **Add Local Interpreter**
3. 重新选择 `langchain1.2`

---

## 七、跑通你的第一行 LangChain 代码

### 7.1 新建一个 Python 文件

在 PyCharm 左侧项目目录中：

1. 右键项目名 `langchain-learning`
2. 选择 **New** → **Python File**
3. 输入文件名：`hello_langchain.py`

> 在 PyCharm 左侧项目目录中，右键项目名 → **New** → **Python File**，输入文件名 `hello_langchain.py`。

### 7.2 写第一行代码

在文件中输入以下代码：

```python
import langchain

print(langchain.__version__)
```

> 在 `hello_langchain.py` 文件中输入上述代码。

### 7.3 运行代码

在代码编辑区，右键点击空白处，选择 **Run 'hello_langchain'**：

> 右键点击代码编辑区空白处，选择 **Run 'hello_langchain'**，或点击代码左侧的绿色小三角运行按钮。

或者在代码里点击左侧的绿色小三角运行按钮。

**成功标志**：底部运行窗口显示 `1.2.12` ✅

> 运行成功后，PyCharm 底部运行窗口应显示 `1.2.12`。

### 7.5 环境配置的小结

到这里，你的电脑上已经有：

```
✅ Miniconda 管家
✅ Python 3.13
✅ langchain1.2 虚拟环境
✅ PyCharm 编辑器
✅ 能运行的第一行 LangChain 代码
```

**你已经迈出了最重要的一步！**

---

## 八、环境方案对比：conda、uv、venv 怎么选？

PDF 里提到了三种环境管理工具，这里也简单对比一下，帮你理解：

| 工具 | 管理 Python 版本 | 管理 Python 包 | 管理非 Python 依赖 | 适合场景 |
|------|-----------------|----------------|------------------|---------|
| **conda** | ✅ | ✅ | ✅ | AI/深度学习、复杂环境、推荐 |
| **uv** | ✅ | ✅ | ❌ | 纯 Python 项目、速度快 |
| **venv** | ❌ | ✅ | ❌ | 简单教学、轻量隔离 |

### 三者的区别（大白话版）

- **conda**：全能管家，能装 Python、装包、装 CUDA 等底层库，最稳妥
- **uv**：只管 Python 生态，但速度很快，适合纯 Python 项目
- **venv**：Python 自带的"小隔间"，最简单，但功能也最基础

### 为什么选 conda（Miniconda）？

LangChain 虽然主要是 Python 项目，但后续学习中可能会用到：
- 向量数据库（如 FAISS）
- 文档解析库（如 PyMuPDF）
- 多模态模型（如图像识别）

这些有时候需要一些底层依赖，**conda 能帮你更好地处理**。

---

## 九、常见问题排查（Windows + Miniconda 版）

### 问题一：安装时提示"无法连接到服务器"

```
检查你的网络是否正常
尝试关闭 VPN / 代理
换用手机热点重新下载
```

### 问题二：conda 命令找不到

```
① 检查是否配置了 PATH 环境变量
② 确认 Miniconda 安装路径正确
③ 重新打开 CMD / PowerShell 再试
```

### 问题三：创建环境时下载很慢

**原因**：默认源在国外，网络不稳定。

**解决方法**：换国内镜像源

```bash
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --set show_channel_urls yes
```

然后重新创建环境。

### 问题四：安装 LangChain 时报错

**常见原因**：
- 环境没激活，装到了系统 Python 里
- 版本号写错了
- 网络不稳定，下载中断

**解决方法**：

```bash
# 确认环境已激活
conda activate langchain1.2

# 先更新 pip
python -m pip install --upgrade pip

# 再安装
pip install langchain==1.2.12 -i https://pypi.tuna.tsinghua.edu.cn/simple
```

### 问题五：PyCharm 里找不到 langchain1.2 环境

**原因**：PyCharm 没有自动识别到 Conda 环境。

**解决方法**：

1. 在 PyCharm 中选择 **Add Interpreter** → **Add Local Interpreter**
2. 选择 **Conda Environment**
3. 在 **Interpreter** 路径中，手动找到：
   ```
   C:\Users\你的用户名\miniconda3\envs\langchain1.2\python.exe
   ```

> 手动选择解释器路径：`C:\Users\你的用户名\miniconda3\envs\langchain1.2\python.exe`。

### 问题六：运行代码提示 `ModuleNotFoundError`

**原因**：Python 环境里没有安装这个包，或者 PyCharm 解释器选错了。

**解决方法**：

1. 检查 PyCharm 右下角是不是 `langchain1.2`
2. 在 Anaconda Powershell Prompt 中激活环境，安装缺失的包：
   ```bash
   conda activate langchain1.2
   pip install 包名
   ```

---

## 十、给新手的学习建议

### 10.1 环境不稳定时怎么办？

如果你按照步骤做，但某一步总是报错，不要慌：

1. **先复制错误信息到搜索引擎**（Bing、Google、百度）
2. **确认 conda 环境已激活**（命令行前面有环境名）
3. **确认 PyCharm 解释器选对**（右下角显示环境名）
4. **如果搞不定，直接删掉环境重来**：
   ```bash
   conda remove --name langchain1.2 --all
   conda create --name langchain1.2 python=3.13.12
   ```

### 10.2 下一步学什么？

环境搭好了，下一篇我们将开始真正用 LangChain 写代码：

> 🎯 **预告**：LangChain 核心三件套——**模型（Model）、提示词（Prompt）、链（Chain）**
> 
> 我们会学习：
> - 如何调用不同的大模型（OpenAI、DeepSeek、Kimi）
> - 如何写一个好的 Prompt
> - 如何组合成一条简单的链

---

## 📝 本节课总结

| 步骤 | 完成了什么 | 验证方式 |
|------|----------|---------|
| 1 | 安装 Miniconda | `conda --version` 有版本号 |
| 2 | 创建虚拟环境 | `conda activate langchain1.2` 成功 |
| 3 | 安装 LangChain | `python -c "import langchain; print(langchain.__version__)"` 输出 1.2.12 |
| 4 | 配置 PyCharm | 右下角显示 `langchain1.2` |
| 5 | 跑通第一行代码 | 运行 `hello_langchain.py` 成功 |

**记住这个核心流程**：

```bash
# 1. 打开 Anaconda Powershell Prompt
# 2. 激活环境
conda activate langchain1.2

# 3. 安装需要的包
pip install langchain==1.2.12

# 4. 在 PyCharm 里写代码、运行
```

---

<br/><br/><br/><br/>

**到这里就结束了，后续还会更新 LangChain 系列相关，还请持续关注！**
**感谢阅读，若有错误可以在下方评论区留言哦！！！**

![[../../../assets/images/pub/clw.webp#pic_center)]]

<br/><br/>
