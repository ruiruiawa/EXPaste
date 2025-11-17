# EXPaste - 文本自动输入工具

<div align="center">

**✨ 告别禁止粘贴，拥抱智能输入 ✨**

![Version](https://img.shields.io/badge/版本-0.1.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3.6+-green.svg)
![PyQt5](https://img.shields.io/badge/GUI-PyQt5-orange.svg)
![License](https://img.shields.io/badge/许可证-MIT-lightgrey.svg)

[项目简介](#项目简介) • [使用指南](#使用指南) • [~~技术架构~~](#-技术架构) • [注意事项](#注意事项)


### 🎨 界面展示
<img src="./res/img000.png" alt="EXPaste演示" width="500"/>
</div>

## 项目简介

在某些情况下，我们难免会遇到禁止使用快捷键`ctrl+v`粘贴的情况。为解决这个问题，EXPaste 应运而生，让文本输入变得简单、快速、准确！

EXPaste 通过巧妙地将文件读取与实时文本编辑相结合，在一些特定情况下能显著提升粘贴效率

> 💡 **灵感来源**：
> 在一些软件或网页中，虽然快捷键和宏定义不能粘贴，但是只要像手机输入法一样模拟键盘输入，也能达到绕过禁止粘贴的目的
> 
> <img src="./res/Forbidden.png" alt="禁止录入粘贴" width="250"/>


### 🌟 功能特色
- **双模式输入**：支持文件读取和实时编辑两种输入方式
- **零依赖兼容**：支持所有桌面应用，支持全部UTF-8字符
- **智能统计**：实时显示字符数和行数统计，可提供预览

### 🛡️ 安全可靠
- **本地处理**：所有数据在本地处理，绝不上传
- **随时中断**：随时开始/停止，完全掌控输入过程
- **错误处理**：完善的异常处理机制，稳定运行

## 快速开始

### 系统要求
- **操作系统**: Windows 7/8/10/11, macOS, Linux通用 `目前只试验过Windows`
- **内存**: 至少 512MB RAM
- **磁盘空间**: 至少 50MB 可用空间
- **Python版本**: 3.6 或更高版本

        PyQt5>=5.15.0, keyboard>=0.13.5
   windows , macOS

        pip install PyQt5 keyboard
   Linux (Ubuntu/Debian)

        sudo apt update
        sudo apt install python3-pip
        sudo apt install python3-tk
        pip3 install PyQt5 keyboard
    Linux (CentOS/RHEL)
 
        sudo yum install python3-pip
        sudo yum install python3-tkinter
        pip3 install PyQt5 keyboard

### 安装步骤

**方法1. 克隆项目**

确保PC上安装了git
```bash
    git clone https://github.com/2ffjc/EXPaste.git
```

**方法2. 直接使用exe**

在旁边或者下方的[release](https://github.com/2ffjc/EXPaste/releases/latest)获取Windows平台的单文件打包版

## 使用指南

### 方法一：🗂️ 文件输入模式 
- 点击`选择文件`选择您的文本文件
- 或点击`创建示例文件`快速开始
-  预览文件内容确认无误后点击`开始粘贴`
### 方法二：✏️ 实时编辑模式
- 直接在编辑器中输入或粘贴文本
-  预览文件内容确认无误后点击`开始粘贴`

**在3秒倒计时内将光标移动到目标输入框**

## 注意事项
目前经过测试的设备极少，不确定其通用性
### ⚠️ 目前不完美支持的应用！

会自动缩进的编译器，记事本等等

### 常见问题

> Q: 程序无法输入文本？
> 
> A: 请检查目标应用程序是否接受文本输入，以及是否有权限访问系统键盘。

> Q: 倒计时结束后没有反应？
> 
> A: 确保在倒计时期间将光标移动到目标输入框。

> Q: 中文输入出现乱码？
> 
> A: 确保文本文件使用UTF-8编码保存。


## 🤝 贡献指南

我们欢迎各种形式的贡献！

报告问题：在Issues中提交bug报告

功能建议：提出新功能想法和改进建议

代码贡献：提交Pull Request帮助改进项目
