我的世界魔戒模组 翻译小帮手
====
Lord of the Rings Minecraft TransHelper
====
***
![maven](https://img.shields.io/badge/python-3.9%2B-blue)

本脚本用于简单检测两个不同版本的 我的世界魔戒模组：复兴版 的语言文件有何改动

This program is used to tell the difference between 2 versions of the language files of LotRMC-Renewed mods
## 声明
此项目仅用于学习交流，请勿用于非法用途

<details>
<summary>用法简介 中文</summary>

## 用法
 - 将两个不同版本的复兴版魔戒模组与本文件放到同一目录下
 - 运行本脚本：**`LotRTransHelper.py`**
 - 在控制台输出结果


 - 如果未出错，则结果会存放在 **`/diff`** 目录下：
   - **`additions.json`**: 新版本增加的键值对
   - **`deletions.json`**: 新版本删除的键值对
   - **`editions.json`**: 新版本修改的键值对
 - 如果出错，请根据控制台的错误提示检查
</details>

<details>
<summary><big> How to use (en) </big></summary>

## How to use
 - Put **`2`** different versions jar files of LotRMC-Renewed mod into the directory of this program
 - Run this program: **`LotRTransHelper.py`**
 - Output result to console


 - If no error during running, the result will be saved in **`./diff`** directory:
   - **`additions.json`**: key-values new version added
   - **`deletions.json`**: key-values new version deleted
   - **`editions.json`**: key-values new version edited
 - If error, please check the console output

</details>

## 更新
### 2022/05/07 \[v1.0.0\]
* 初始版本
* 添加了对比新旧复兴版魔戒模组语言文件差异的功能