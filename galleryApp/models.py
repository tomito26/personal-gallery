from django.db import models

# Create your models here.
class Image(models.Model):
    photo  = models.ImageField(upload_to='images/')
    image_name = models.CharField(max_length=60)
    image_description = models.TextField()
    upload_date =models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category',on_delete=models.CASCADE)
    location = models.ForeignKey('Location',on_delete=models.CASCADE)
    
    def __str__(self):
        return self.image_name
    
    class Meta:
        ordering = ['upload_date']
        
    def save_image(self):
        self.save()
        
    def delete_image(self):
        self.delete()
        
    @classmethod
    def search_by_image_category(cls,search_term):
        galleryapp = cls.objects.filter(image_name__icontains=search_term)
        return galleryapp
    @classmethod
    def search_by_location(cls,search_term):
        results = cls.objects.filter(location__location__icontains=search_term)   
        return results
    @classmethod
    def filter_by_location(cls, location):
        image_location = Image.objects.filter(location__name=location).all()
        return image_location
class Location(models.Model):
    location_name = models.CharField(max_length=60)

    def save_location(self):
        self.save()
    @classmethod
    def delete_location(cls,location):
        cls.objects.filter(location=location).delete()
    
    @classmethod
    def get_all_locations(cls):
        locations = cls.objects.all()
        return locations
    
    def __str__(self):
        return self.location_name
    

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    
    @classmethod
    def get_all_categories(cls):
        categories = cls.objects.all()
        return categories
    @classmethod
    def search_by_category(cls,search_term):
        results = cls.objects.filter(category_name__icontains=search_term)
    
    def save_category(self):
        self.save()
        
    @classmethod
    def delete_category(cls,category):
        cls.objects.filter(category=category).delete()
    
    def __str__(self):
        return self.category_name
    
    
    