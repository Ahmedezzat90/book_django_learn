from django.db import models

# Create your models here.

class publishing_house(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name

class book(models.Model):
    name = models.CharField(max_length=100)
    publish_date = models.DateField()
    isbn = models.CharField(max_length=13)
    image = models.ImageField(upload_to='images/%y/%m/%d',null=True,blank=True)
    publishing_house = models.ForeignKey(publishing_house,on_delete=models.PROTECT,null=True)
    
    def __str__(self):
        return self.name

