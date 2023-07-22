from django.contrib import admin
from django.urls import path, include
from home.views import *
from register.views import *
from eventos.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', home, name='home'),
    path('register/', register, name='register'),
    path('eventos', my_eventos, name='evento')

]
