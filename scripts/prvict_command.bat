cd ..
git add .
echo version update:
set /p name=
git commit -m "%name%"
git push origin master