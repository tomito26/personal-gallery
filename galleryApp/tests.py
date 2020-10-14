from django.test import TestCase
from .models import Location, Image, Category

# Create your tests here.
class ImageTestClass(TestCase):
    def setUp(self):

        self.location = Location(location='newyork')
        self.location.save_location()

        self.category = Category(category='art')
        self.category.save_category()

        self.pic = Image(id=1, image_name='image', image_description='paint work',
                             location=self.location, category=self.category)

    def test_instance(self):
        self.assertTrue(isinstance(self.coolpic, Image))

    def test_save_image(self):
        self.pic.save_image()
        pics = Image.objects.all()
        self.assertTrue(len(pics) > 0)

    def test_delete_image(self):
        self.pic.delete_image()
        pics = Image.objects.all()
        self.assertTrue(len(pics) == 0)

class CategoryTestClass(TestCase):
    def setUp(self):
        '''
        Method to be run in every beginning of the test
        '''
        self.sports = Category(category='sport')

    def test_instance(self):
        self.assertTrue(isinstance(self.sports, Category))

    def tearDown(self):
        '''
        Method to clear the test that has been done on category
        '''
        Category.objects.all().delete()

    def test_save_method(self):
        '''
        Method to save category
        
        '''
        self.sports.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        '''
        Method to delete the category
        '''
        self.sports.delete_category('sports')
        category = Category.objects.all()
        self.assertTrue(len(category) == 0)


class LocationTestClass(TestCase):

    #set up method
    def setUp(self):
        '''
        Method to be run in every beginning of the test
        '''
        self.nairobi = Location(location='nairobi')

    def test_instance(self):
        self.assertTrue(isinstance(self.nairobi, Location))

    def tearDown(self):
        '''
        Method to clear the test that has been done on location
        '''
        Location.objects.all().delete()

    def test_save_method(self):
        '''
        Method to save the location
        
        '''
        self.nairobi.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_method(self):
        '''
        Method to delete the location
        
        '''
        self.nairobi.delete_location('nairobi')
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)
