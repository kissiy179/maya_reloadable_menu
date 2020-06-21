@echo off

REM 遅延環境変数有効
setlocal EnableDelayedExpansion

REM MAYA_MODULE_PATHにカレントディレクトリを追加
cd /d %~dp0
Set MAYA_MODULE_PATH=%cd%;%MAYA_MODULE_PATH%

REM レジストリからMayaインストールフォルダ検索して見つけたら実行
set MAYA_APP_PATH=null

for /l %%v in (2030, -1, 2015) do (
    FOR /F "TOKENS=1,2,*" %%I IN ('REG QUERY "HKEY_LOCAL_MACHINE\SOFTWARE\Autodesk\Maya\%%v\Setup\InstallPath" /v "MAYA_INSTALL_LOCATION"') DO IF "%%I"=="MAYA_INSTALL_LOCATION" SET MAYA_APP_PATH=%%K

    if not !MAYA_APP_PATH!==null goto execute
)

goto except

REM Maya起動
:execute
start "" "%MAYA_APP_PATH%\bin\maya.exe"
goto end

REM インストールされてない場合修了
:except
echo Maya is not installed.
pause

:end
