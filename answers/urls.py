from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'',views.video,name='video'),

]
