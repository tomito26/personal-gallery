from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Image,Location

# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def galler(request):
    photo_gallery = Image.objects.all()
    image_location = Location.objects.all()
    image_category = Category.objects.all()
    
    context = {
        'photo_gallery':photo_gallery,
        'image_location':image_location,
        'image_category':image_category
    }
    return render(request,'image-gallery/gallery.html',context)
    
def search_by_image_category(request):
    if 'pic' in request.GET and request.GET["pic"]:
        search_term = request.GET.get('pic')
        searched_images = Image.search_by_image_category(search_term)
        message = f"{search_term}"
        
        return render(request,'image-gallery/search.html',{"message":message,"images":searched_images})
    
    else:
        message = "You haven't searched for any term"
        return render(request,'image-gallery/search.html',{"message":message})
    
