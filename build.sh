rm citrix.zip | echo ""
zip -r citrix.zip citrix/
scp -i ~/.ssh/rob_id_rsa citrix.zip rob@172.28.183.9:/home/rob/automation3/