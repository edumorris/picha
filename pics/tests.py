from django.test import TestCase
from .models import Location, Category, Images, Subs

# Create your tests here.
class ImagesTestClass(TestCase):
    # Set up
    def setUp(self):
        self.img = Images(image = 'img', img_name = 'img_name', img_description = 'img_description')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.img, Images))
    
    def tearDown(self):
        Images.objects.all().delete()

class CategoryTestClass(TestCase):
    def setUp(self):
        self.cat = Category(category = 'cat1')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.cat, Category))
    
    def tearDown(self):
        Category.objects.all().delete()

class LocationTestClass(TestCase):
    def setUp(self):
        self.locale = Location(location = 'locale')
    
    def test_instance(self):
        self.assertTrue(isinstance(self.locale, Location))
    
    def tearDown(self):
        Location.objects.all().delete()

class SubsTestClass(TestCase):
    def setUp(self):
        self.sub = Subs(user_name = 'IamGroot', first_name = 'Iam', last_name = 'Groot', email = 'iam@groot.com', phonenumber = 10368007)
    
    def test_isinstance(self):
        self.assertTrue(isinstance(self.sub, Subs))
    
    def tearDown(self):
        Subs.objects.all().delete()
