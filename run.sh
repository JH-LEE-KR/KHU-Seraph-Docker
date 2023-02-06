cd KHU_Seraph_django && docker build -t test/django . && cd ../
cd KHU_Seraph_nginx && docker build -t test/nginx . && cd ../
docker-compose up --build -d
