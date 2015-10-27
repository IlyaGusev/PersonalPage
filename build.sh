sudo docker stop $(sudo docker ps -a -q)
rm PersonalPage/settings.py
cp prod_settings.py PersonalPage/settings.py
chmod 777 PersonalPage/settings.py
sudo docker build -t pp .
sudo docker run -d -p 80:80 -v /data/pp/db:/home/docker/code/db pp
