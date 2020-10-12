from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$', views.galler, name='galler'),
    url(r'^search/', views.search_by_image_category, name='search_category'),
    url(r'picture/(?P<image_id>\d+)', views.picture, name="picture")
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)