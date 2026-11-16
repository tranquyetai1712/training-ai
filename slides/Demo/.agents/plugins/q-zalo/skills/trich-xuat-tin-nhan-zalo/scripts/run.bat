@echo off
chcp 65001 >nul
node "%~dp0zalo_engine.cjs" %*
