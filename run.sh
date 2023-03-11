cd KHU_Seraph_django && docker build -t seraph/django . && cd ../
cd KHU_Seraph_nginx && docker build -t seraph/nginx . && cd ../
docker-compose up --build -d
