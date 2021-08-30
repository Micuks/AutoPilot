cd ./Build
sh rebuild_release.sh
cd ..
echo Successfully rebuild.
rm Controller.zip
zip -j Controller.zip ./bin/AEB
zip -j Controller.zip ./bin/AVP
zip -j Controller.zip ./bin/PredefinedRoute
zip -j Controller.zip ./bin/LKA
zip -j Controller.zip ./lib/Linux64/*
echo -e "\a"
echo Success!!!
date
