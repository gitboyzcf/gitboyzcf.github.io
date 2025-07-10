---
author: boyzcf
pubDatetime: 2025-03-03 15:27:07
modDatetime: 2025-03-03 15:27:07
title: 你不知道的 JavaScript 工具管理器 Volta（禁止废话版）
slug: 
featured: false
draft: false
tags:
  - 拒绝废话
  - 常用代码块
  - 前端
  - JavaScript
description:
  Volta 是一个现代化的 JavaScript 工具管理器，提供了比传统 nvm 更好的性能和用户体验。通过使用 Volta 管理项目级别的 Node.js 版本，可以确保每个项目都有一个干净且独立的开发环境。
---

![禁止废话](../../../assets/images/pub/jjfh.webp)

# Volta

Volta 是一个现代化的 JavaScript 工具管理器，提供了**比传统 nvm 更好的性能和用户体验**。通过使用 Volta 管理**项目级别的 Node.js 版本**，可以确保每个项目都有一个**干净且独立的开发环境**。

官网：[https://volta.sh/）](https://volta.sh/)（英）

**Volta 是用 Rust 编写的 JavaScript 工具管理器，具有以下特点：**

- 快速且可靠：基于 Rust 实现，性能优异
- 项目智能：自动检测并切换到项目所需的 Node.js 版本
- 跨平台：支持 Windows、macOS 和 Linux
- 管理包管理器（npm、yarn、pnpm）的版本
- 支持管理全局工具的特定版本

总的来说，Volta 提供了更现代化、更自动化的 Node.js 版本管理体验，特别适合团队协作和需要频繁切换项目的场景。

```bash
# NVM 需要手动切换版本
nvm use 22

# Volta 自动检测项目版本
cd my-project  # 自动切换到项目指定的版本

# Volta 固定项目版本
volta pin node@22
```

## 安装步骤

- Unix-like 系统（macOS、Linux）：

 ```bash
 curl https://get.volta.sh | bash
 ```

- Windows：
下载并运行 [Windows 安装器](https://github.com/volta-cli/volta/releases)

### 基本使用

```bash
# 安装 Node.js
volta install node@lts

# 设置项目 Node.js 版本, 将项目的运行时或包管理器设置为指定的版本
volta pin node@lts

# 安装包管理器
volta install npm@lts
volta install yarn@lts

# 查看当前工具版本
volta list

# 仅下载 node 到本地不安装
volta fetch node@lts

# 查看已经安装的 node 版本列表
volta list node

# 查看 node 安装路径
volta which node


```

```bash

volta -h
The JavaScript Launcher ⚡

Usage: volta [OPTIONS] [COMMAND]

Commands:
  fetch        Fetches a tool to the local machine
  install      Installs a tool in your toolchain
  uninstall    Uninstalls a tool from your toolchain
  pin          Pins your project's runtime or package manager
  list         Displays the current toolchain
  completions  Generates Volta completions
  which        Locates the actual binary that will be called by Volta
  setup        Enables Volta for the current user / shell
  run          Run a command with custom Node, npm, pnpm, and/or Yarn versions
  help         Print this message or the help of the given subcommand(s)

Options:
      --verbose       Enables verbose diagnostics
      --very-verbose  Enables trace-level diagnostics
      --quiet         Prevents unnecessary output
  -v, --version       Prints the current version of Volta
  -h, --help          Print help (see more with '--help')


```
