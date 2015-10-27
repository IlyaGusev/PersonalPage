from ubuntu:14.04

run echo "deb http://us.archive.ubuntu.com/ubuntu precise main universe" >> /etc/apt/sources.list

run apt-get update
run apt-get install -y build-essential
run apt-get install -y python3-software-properties python-software-properties 
run apt-get install -y python3 python3-dev python3-setuptools python3-pip
run apt-get install -y --force-yes git-core nginx supervisor
run apt-get install -y python-software-properties
run apt-get install -y sqlite3

run pip3 install uwsgi

add . /home/docker/code/
ADD ./conf/run.sh /opt/run.sh

run echo "daemon off;" >> /etc/nginx/nginx.conf
run rm /etc/nginx/sites-enabled/default
run ln -s /home/docker/code/conf/nginx-app.conf /etc/nginx/sites-enabled/
run ln -s /home/docker/code/conf/supervisor-app.conf /etc/supervisor/conf.d/

run pip3 install -r /home/docker/code/requirements.txt

VOLUME  ["/home/docker/code/db"]
expose 80
CMD ["/bin/bash", "/opt/run.sh"]

