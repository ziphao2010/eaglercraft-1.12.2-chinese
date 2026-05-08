
@echo off
chcp 65001 &gt;nul
title Eaglercraft 1.12.2 中文版
echo.
echo ==============================================
echo     Eaglercraft 1.12.2 中文版服务器
echo ==============================================
echo.
echo 正在启动...
echo.

cd /d "%~dp0"
python 启动中文服务器.py

if errorlevel 1 (
    echo.
    echo 未找到 Python！请先安装 Python 或用浏览器直接打开！
    echo.
    pause
)
