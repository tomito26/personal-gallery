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
    def search_by_category(cls,search_term):
        
        results = cls.objects.filter(category__category__icontains=search_term)
    
    @classmethod
    def search_by_location(cls,search_term):
        results = cls.objects.filter(location__location__icontains=search_term)   
        
        
class Location(models.Model):
    location_name = models.CharField(max_length=60)

    
    def __str__(self):
        return self.location_name
    

class Category(models.Model):
    name = models.CharField(max_length=30)

    
    
    def __str__(self):
        return self.category_name
    
    
    