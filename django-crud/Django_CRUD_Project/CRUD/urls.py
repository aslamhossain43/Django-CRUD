from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('create/', views.create, name='create'),
    path('add_book/', views.add_book, name='add_book'),
    path('edit/<id>/', views.edit, name='edit'),
    path('delete/<id>/', views.delete, name='delete'),
    path('update/<id>/', views.update, name='update'),
    path('upload/', views.upload, name='upload'),

]
if settings.DEBUG: # remember to set 'DEBUG = True' in settings.py
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)