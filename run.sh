cd django && docker build -t seraph/django . && cd ../
cd nginx && docker build -t seraph/nginx . && cd ../
docker-compose up --build -d
