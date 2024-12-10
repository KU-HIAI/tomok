sudo docker ps -a -q --filter ancestor=acc_server | xargs -r sudo docker stop
sudo docker ps -a -q --filter ancestor=acc_server | xargs -r sudo docker rm
sudo docker ps -a -q --filter ancestor=api_server | xargs -r sudo docker stop
sudo docker ps -a -q --filter ancestor=api_server | xargs -r sudo docker rm

sudo docker rmi acc_server
sudo docker rmi api_server


# sudo docker build -t tomok_acc .

# sudo docker run --network host \
#   -e PORT=51076 \
#   -e SPECIFICATION_DIR=/usr/src/app/acc_server/openapi \
#   -e API_FILE=tomok-demo.yaml \
#   tomok_acc

sudo docker-compose up --build