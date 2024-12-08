sudo docker ps -a -q --filter ancestor=tomok_acc | xargs -r sudo docker stop
sudo docker ps -a -q --filter ancestor=tomok_acc | xargs -r sudo docker rm
sudo docker rmi tomok_acc

sudo docker build -t tomok_acc .

sudo docker run --network host \
  -e PORT=51076 \
  -e SPECIFICATION_DIR=/usr/src/app/acc_server/openapi \
  -e API_FILE=tomok-demo.yaml \
  tomok_acc