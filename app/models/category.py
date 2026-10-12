from peewee import CharField, DateTimeField
from datetime import datetime
from app.models import db
from app.models.user import BaseModel

class Category(BaseModel):
    name = CharField(max_length= 100, unique= True)
    created_at = DateTimeField(default= datetime.now) 

    def __str__(self):
        return self.name