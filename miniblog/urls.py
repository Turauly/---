from django.contrib import admin
from django.urls import path, include
from blog.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls')),  # 👈 blog қосымшасының барлық маршруты api/ арқылы
    path('', home),  # Басты бет
]
