import uuid
from django.db import models

# Create your models here.


class basic(models.Model):
    uid = models.UUIDField(primary_key=True, editable=False , default=uuid.uuid4())
    created_on = models.DateField(auto_now=True)
    updated_on = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Todo(basic):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    cheek = models.BooleanField(default=False)

