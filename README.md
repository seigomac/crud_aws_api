# crud_aws_api


## AWS のサーバレスサービスを構築して CRUD システムを構築する。

<img width="774" alt="image" src="https://user-images.githubusercontent.com/72975333/188258130-581d32a4-c00a-4b6e-a620-841a39068ad3.png">

### ■API Gateway の URL

https://cdqugz6hod.execute-api.ap-northeast-1.amazonaws.com x8tz9v enabled 2022-09-03

### ■ リクエストコマンド

#### ・Put

curl -v -X "PUT" -H "Content-Type: application/json" -d "{"id": "{id}", "price": {price}, "name": "{name}"}" https://cdqugz6hod.execute-api.ap-northeast-1.amazonaws.com/items

#### ・Get

curl -v -X "GET" -H "Content-Type: application/json" https://cdqugz6hod.execute-api.ap-northeast-1.amazonaws.com/items

#### ・Delete

curl -v -X "DELETE" -H "Content-Type: application/json" https://cdqugz6hod.execute-api.ap-northeast-1.amazonaws.com/items/{id}
