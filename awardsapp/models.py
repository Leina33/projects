from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class tags(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_tags(self):
        self.save()

    def delete_tags(self):
        self.delete()
        
        
class Location(models.Model):
    name = models.CharField(max_length=30)


    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

    def __str__(self):
        return self.name
        
class Projects(models.Model):
    title = models.TextField(max_length=200, null=True, blank=True, default="title")
    project_image = models.ImageField(upload_to='picture/', null=True, blank=True)
    description = models.TextField()
    project_url=models.URLField(max_length=250)
    
    @classmethod
    def search_by_title(cls,search_term):
        news = cls.objects.filter(title__icontains=search_term)
        return awardsapp
    
    def __str__(self):
        return self.title
    
    
class Image(models.Model):
    image=models.ImageField(upload_to='picture/', )
    name = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, related_name="images")
    description=models.TextField()
    location=models.ForeignKey(Location, null=True)
    tags=models.ManyToManyField(tags, blank=True)
    likes = models.IntegerField(default=0)
    comments= models.TextField(blank=True)

    def __str__(self):
        return self.name
    
    
class Profile(models.Model):
    
    profile_pic = models.ImageField(upload_to='picture/', null=True, blank=True, default= 0)
    bio = models.TextField(max_length=200,null=True,blank=True,default="bio")
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True, related_name="profile")
    contact=models.IntegerField(default=0)
    
    
class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()
    
    