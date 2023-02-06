cd django && docker build -t test/django . && cd ../
cd nginx && docker build -t test/nginx . && cd ../
docker-compose up --build -d
