from mongoengine import *
from datetime import datetime

class Authors(Document):
    email = EmailField(max_length=50, required=True, unique=True)
    username = StringField(max_length=50, required=True, unique=True)
    password = StringField(max_length=50, required=True)
    images = ListField()
    bio = StringField(max_length=200)
    written_stories = ListField()
    saved_stories = ListField()
    superuser = BooleanField(default=False)
    date_created = DateField(default=datetime.now())

class Comments(Document):
    author = ReferenceField(Authors)
    comment = StringField(max_length=500, required=True)
    likes = IntField()

class Stories(Document):
    title = StringField(max_length=100, required=True)
    story = StringField(max_length=20000, required=True)
    story_image = StringField(required=True)
    author = StringField(required=True)
    tags = ListField()
    short_description = StringField(max_length=100)
    comments = ListField(ReferenceField(Comments))
    saved_by = ListField(ReferenceField(Authors))
    likes = IntField()
    date_created = StringField(default=datetime.now().strftime("%d/%m/%Y, %H:%M:%S"))


