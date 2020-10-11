from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Image,Location

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def image_galler(request):
    photo_gallery = Image.objects.all()
    image_location = Location.objects.all()
    image_category = Category.object.all()
    
    context = {
        'photo_gallery':photo_gallery,
        'image_location':image_location,
        'image_category':image_category
    }
    return render(request,'gallery.html',context)
    
    
    
