import numpy as np

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
    
    def average_design(self):
        design_ratings = list(map(lambda x: x.design_rating, self.reviews.all()))
        return np.mean(design_ratings)

    def average_usability(self):
        usability_ratings = list(map(lambda x: x.usability_rating, self.reviews.all()))
        return np.mean(usability_ratings)

    def average_content(self):
        content_ratings = list(map(lambda x: x.content_rating, self.reviews.all()))
        return np.mean(content_ratings)

    def save_project(self):
        self.save()

    @classmethod
    def delete_project_by_id(cls, id):
        projects = cls.objects.filter(pk=id)
        projects.delete()

    @classmethod
    def get_project_by_id(cls, id):
        projects = cls.objects.get(pk=id)
        return projects

    @classmethod
    def search_projects(cls, search_term):
        projects = cls.objects.filter(title__icontains=search_term)
        return projects

    @classmethod
    def update_project(cls, id):
        projects = cls.objects.filter(id=id).update(id=id)
        return projects

    @classmethod
    def update_description(cls, id):
        projects = cls.objects.filter(id=id).update(id=id)
        return projects

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
    
    
class Review(models.Model):
    
    project = models.ForeignKey(Project, null=True, blank=True, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='reviews')
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="reviews", null=True, blank=True)
    comment = models.TextField()
    design_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    usability_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    content_rating = models.IntegerField(choices=RATING_CHOICES, default=0)