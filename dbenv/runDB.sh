db_content=${1}
images_name=${2}
sudo docker stop dbforauth
sudo docker rm dbforauth
sudo docker run -itd --name dbforauth -p 3306:3306 -v ${db_content}:/var/lib/mysql ${images_name}