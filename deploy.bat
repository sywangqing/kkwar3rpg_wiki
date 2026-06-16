@echo off
chcp 65001 >nul
cd /d "f:\AI\AI-superpower\war3-wiki"

echo.
echo ============================================
echo  KK 作者中心 · 一键部署到 durontar.com
echo ============================================
echo.

echo [1/3] 验证构建产物...
if not exist "docs\.vitepress\dist\index.html" (
    echo ❌ 缺少构建产物，正在重新构建...
    call npx vitepress build docs
    if errorlevel 1 (
        echo ❌ 构建失败，请检查错误
        pause
        exit /b 1
    )
)
echo ✅ 构建产物就绪

echo.
echo [2/3] 部署到 Vercel...
echo.
echo 接下来会弹出浏览器，请点击 "Continue with GitHub" 授权 Vercel
echo 如果已经授权过，会自动跳过
echo.
pause

npx vercel deploy --prod --yes

if errorlevel 1 (
    echo.
    echo ❌ 部署失败。可能需要先登录。
    echo 请在浏览器打开 https://vercel.com/new 导入 s
    echo 仓库：sywangqing/kkwar3rpg_wiki
    echo.
    pause
    exit /b 1
)

echo.
echo [3/3] ✅ 部署完成！
echo.
echo 访问 https://durontar.com/author/ 查看效果
echo.
pause
