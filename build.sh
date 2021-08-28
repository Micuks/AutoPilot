cd ./Build
sh rebuild_release.sh
cd ..
echo Successfully rebuild.
rm AEBCpp.zip
zip -j AEBCpp.zip ./bin/AEB
zip -j AEBCpp.zip ./lib/Linux64/*
echo -e "\a"
echo Success!!!
