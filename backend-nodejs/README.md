# Webapp Boilerplate (backend)
This repository goes with [webapp-boilerplate-frontend](https://github.com/josephmfaulkner/webapp-boilerplate-frontend)

## Object Detection Model

The server runs on ImageAI using RetinaNet. For it to work, first follow the **[ImageAI setup instructions](https://github.com/OlafenwaMoses/ImageAI)**.
Then, download the RetinaNet object detection model **[here](https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/resnet50_coco_best_v2.1.0.h5)**.

Once you download the file, place it in the _models_ folder.


## Deploy to Heroku
```
heroku create
heroku addons:create heroku-postgresql:hobby-dev
git push heroku master
```

## Local DB Development
```
docker-compose up
```
In another terminal
```
npx sequelize-cli db:migrate
npx sequelize-cli db:seed:all
```
**Open PG Admin:** [localhost:8080](localhost:8080), **PW:** password

**Add DB to PG Admin:** Servers > Create > Server

### Connection: 
**Host name :** db; **Port :** 5432; **Username :** postgres; **Password :** postgres
