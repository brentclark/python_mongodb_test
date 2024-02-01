from mongoengine import connect, Document, StringField, IntField, EmailField

class Person(Document):
    name = StringField(required=True, max_length=50)
    surname = StringField(required=True, max_length=50)
    email = EmailField()
    age = IntField()