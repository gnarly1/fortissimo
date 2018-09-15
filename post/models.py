from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    
    title=models.CharField(max_length=250)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    pic=models.ImageField(default='default.png')
    author=models.ForeignKey(User,default=None,on_delete=models.PROTECT)
    
    
    
    #class Student(models.Model):
    Rock ='Rock'
    Indie='Indie'
    Metal='Metal'
    Other='Other'
    GENRE_CHOICES = (
        (Rock, 'Rock'),
        (Indie, 'Indie'),
        (Metal, 'Metal'),
        (Other, 'Other'),
    )
    genre = models.CharField(max_length=5,
                                      choices=GENRE_CHOICES,
                                      default=Other)

    #def is_upperclass(self):
     #   return self.year_in_school in (self.JUNIOR, self.SENIOR)
    def __str__self(self):
        return(self.title)
     
    def snippet(self):
        return self.body[:75]+'.......'
        
    def clean(self):
        if self.slug=='Rock':
            raise ValidationError('Start date is after end date')
