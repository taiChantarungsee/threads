from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('main/', include('reports.urls')),
    path('admin/', admin.site.urls),
]
