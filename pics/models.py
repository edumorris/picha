from django.db import models

# Create your models here.
class Location(models.Model):
    locale = models.CharField(max_length = 50)

    def __str__(self):
        return self.locale

class Category(models.Model):
    tag = models.CharField(max_length = 30)

    def __str__(self):
        return self.tag

class Images(models.Model):
    image = models.ImageField(upload_to = 'pictorials/')
    img_name = models.CharField(max_length = 150)
    img_description = models.CharField(max_length = 1000)
    location = models.ForeignKey(Location , on_delete=models.CASCADE, blank = True)
    category = models.ManyToManyField(Category, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.img_name
    
    def save_image(self):
        self.save()
    
    def delete_image(self):
        self.delete()
    
    def update_image(self):
        pass
    
    @classmethod
    def get_image_by_id(cls, img_id):
        picha = cls.objects.get(id = img_id)
        return picha
    
    @classmethod
    def search_image(cls, category_term):
        cats = cls.objects.filter(category__tag__icontains = category_term)
        return cats
    
    @classmethod
    def filter_by_location(cls, location_term):
        loca = cls.objects.filter(location__locale__icontains = location_term)
        return loca

class Subs(models.Model):
    user_name = models.CharField(max_length = 15)
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    phonenumber = models.IntegerField(blank = True)

    def __str__(self):
        return self.user_name