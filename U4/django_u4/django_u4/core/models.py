from django.db import models

# Create your models here.

class Foo(models.Model):
    CATEGORY_TYPES = ((1, 'type bar'), (2, 'type baz'))
    name = models.TextField()
    category = models.IntegerField(choices=CATEGORY_TYPES)

