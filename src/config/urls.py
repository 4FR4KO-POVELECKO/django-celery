from django.conf.urls import url
from django.contrib import admin
 
from publish.views import view_post
from main.views import home, verify
 
urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^verify/(?P<uuid>[a-z0-9\-]+)/', verify, name='verify'),
    url(r'^(?P<slug>[a-zA-Z0-9\-]+)', view_post, name='view_post')
]