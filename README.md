# python_mongodb_test
python_mongodb_test

## Create a .env file with the following example ENV variables for docker compose.

```
MONGO_INITDB_ROOT_USERNAME=root
MONGO_INITDB_ROOT_PASSWORD=example
ME_CONFIG_MONGODB_ADMINUSERNAME=root
ME_CONFIG_MONGODB_ADMINPASSWORD=example
ME_CONFIG_MONGODB_URL=mongodb://root:example@mongo:27017/
ME_CONFIG_BASICAUTH_USERNAME=admin
ME_CONFIG_BASICAUTH_PASSWORD=pass
```

# See Docker Network(s)

```
docker network ls
```

# Create User
## Connect to Mongo
```
docker run -it --rm --network python_mongodb_test_mongo-database  mongo mongosh --host mongo -u $USERNAME -p $PASSWORD --authenticationDatabase admin $DATABASE
```
## Create User
```
db.createUser ( { user: "accountAdmin01", pwd: passwordPrompt(), roles: [ "readWrite", "dbAdmin" ]  } )
```

# Connect to Mongo Express
```
http://127.0.0.1:8081/
```
