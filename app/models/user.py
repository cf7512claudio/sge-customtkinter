from peewee import Model, CharField, DateTimeField
from datetime import datetime
from app.models import db
from passlib.hash import sha256_crypt

class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    full_name = CharField(max_length=50)
    username = CharField(max_length=30)
    email = CharField(max_length=255, unique=True)
    contact = CharField(max_length=20, null=False)
    position = CharField(max_length=50, null=True)
    password_hash = CharField(max_length=255)
    role = CharField(default="user", max_length=20)
    created_at = DateTimeField(default= datetime.now)

    def set_password(self, password: str):
        self.password_hash = sha256_crypt.hash(password)

    def verify_password(self, password: str) -> bool:
        return sha256_crypt.verify(password, self.password_hash)

    def __str__(self):
        return f"{self.username} | {self.role}"