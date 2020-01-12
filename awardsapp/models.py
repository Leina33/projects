from django.db import models

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
    
    def __str__(self):
        return self.title
    
    
    
    
    