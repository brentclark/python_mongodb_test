from mongoengine import connect
import os
import random
from models import Person
from faker import Faker

from dotenv import find_dotenv, load_dotenv
load_dotenv(find_dotenv(".env"))

MONGO_INITDB_ROOT_USERNAME = os.environ.get("MONGO_INITDB_ROOT_USERNAME")
MONGO_INITDB_ROOT_PASSWORD = os.environ.get("MONGO_INITDB_ROOT_PASSWORD")

fake = Faker()


#connect(host="mongodb://127.0.0.1:27017/testcaseDB")

connect(
    db='testcaseDB',
    username='accountAdmin01',
    password='accountAdmin01',
    host=f'mongodb://accountAdmin01:accountAdmin01@127.0.0.1/testcaseDB'
)


for _ in range(100):

    # Create an instance of the document class
    new_person = Person(
        name=fake.first_name(),
        surname=fake.last_name(),
        email=fake.email(),
        age=random.randint(20,90))

    # Save the document to the collection
    new_person.save()
