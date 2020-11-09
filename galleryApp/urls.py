from django.conf.urls import url
from . import views
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('', views.galler, name='galler'),
    path('search/', views.search_by_image_category, name='search_category'),
    path('picture/<int:image_id>/', views.picture, name="picture")
]

