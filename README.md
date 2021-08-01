# Python WA Website

## Installing / Running - Frontend

``` sh
# install node (tested on version 16)... then
cd frontend
npm install
npm run dev
# go to http://localhost:3000 in your browser
```

## Installing / Running - Backend

``` sh
# if you don't already have it
# pip install pipenv
pipenv install
pipenv run uvicorn main:app --reload
```

## Deploying

``` sh
cd frontend
npm run build
git add dist
git commit -m 'my awesome change'
git push heroku master
```
