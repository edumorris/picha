from django.db import models

# Create your models here.
class Location(models.Model):
    location = models.CharField(max_length = 50)

    def __str__(self):
        return self.location_name

class Category(models.Model):
    category = models.CharField(max_length = 30)

    def __str__(self):
        return self.cat_name

class Images(models.Model):
    image = models.ImageField(upload_to = 'pictorials/')
    img_name = models.CharField(max_length = 150)
    img_description = models.CharField(max_length = 1000)
    location = models.ForeignKey(Location , on_delete=models.CASCADE, blank = True)
    category = models.ManyToManyField(Category)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.img_name
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def update_image(self):
        pass
    
    def get_image_by_id(self):
        pass
    
    def search_image(self, category):
        pass
    
    def filter_by_location(self, location):
        pass

class Subs(models.Model):
    user_name = models.CharField(max_length = 15)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phonenumber = models.IntegerField(blank = True)

    def __str__(self):
        return self.user_name