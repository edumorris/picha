from django.db import models

# Create your models here.
class Images(models.Model):
    # image field
    img_name = models.CharField(max_length = 150)
    img_description = models.CharField()
    img_location = models.ManyToManyField(Location)
    img_category = models.ManyToManyField(Category)
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


class Location(models.Model):
    location_name = models.CharField(max_length = 50)

class Category(models.Model):
    cat_name = models.CharField(max_length = 30)

class Subs(models.Model):
    user_name = models.CharField(max_length = 15)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phonenumber = models.IntegerField(max_length = 20)