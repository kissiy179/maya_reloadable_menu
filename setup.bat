@echo off

REM ライブラリインストールパスを取得
set LIB_PATH=%1

if "%LIB_PATH%"=="" (
    set LIB_PATH=.\Lib\site-packages
)

REM 遅延環境変数有効
setlocal EnableDelayedExpansion

REM MAYA_MODULE_PATHにカレントディレクトリを追加
cd /d %~dp0
Set MAYA_MODULE_PATH=%cd%;%MAYA_MODULE_PATH%

REM ------- レジストリからMayaインストールフォルダ検索 -------------------------
set MAYA_APP_PATH=null

for /l %%v in (2030, -1, 2015) do (
    FOR /F "TOKENS=1,2,*" %%I IN ('REG QUERY "HKEY_LOCAL_MACHINE\SOFTWARE\Autodesk\Maya\%%v\Setup\InstallPath" /v "MAYA_INSTALL_LOCATION"') DO IF "%%I"=="MAYA_INSTALL_LOCATION" SET MAYA_APP_PATH=%%K

    if not !MAYA_APP_PATH!==null goto install_pip
)

REM Mayaが見つからなければそのまま終了
goto except

REM ------- pipインストール -------------------------
:install_pip
REM mayapyのパスを取得
set MAYAPY_PATH="%MAYA_APP_PATH%bin\mayapy.exe"

REM pipがインストールされているか確認
call %MAYAPY_PATH% -m pip

REM インストールされてなければインストール
if not %errorlevel%==0 (
    curl https://bootstrap.pypa.io/get-pip.py | %MAYAPY_PATH%
)

REM pipアップデート
call %MAYAPY_PATH% -m pip install -U pip

REM ------- パッケージインストール -------------------------
call %MAYAPY_PATH% -m pip install -r requirements.txt -t %LIB_PATH%

goto end

REM インストールされてない場合終了
:except
echo Maya is not installed.
pause

:end
