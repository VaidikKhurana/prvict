cd ..
git add .
echo specify version update:
set /p name=
git commit -m "%name%"
git push origin master