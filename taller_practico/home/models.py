from django.db import models


# Create your models here.

"""
create table categorias(
    id int not null auto_increment primary key,
    nombre varchar(100),
    slug varchar(100)
)
"""


class Categorias(models.Model):
    
    nombre = models.CharField(max_length=100, null=True, default='vacio')
    slug = models.CharField(max_length=100, null=True, default='vacio')
    
    
    class Meta:
        managed = True
        db_table = 'categorias'


class Post(models.Model):
    categorias = models.ForeignKey(Categorias, models.DO_NOTHING, null=True)
    nombre = models.CharField(max_length=100, null=True, default='vacio')
    slug = models.CharField(max_length=100, null=True, default='vacio')
    detalle = models.TextField(null=True)
    fecha  = models.DateTimeField()
    
    class Meta:
        managed = True
        db_table = 'post'
    



    