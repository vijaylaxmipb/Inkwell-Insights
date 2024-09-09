
from django.urls import path
from .views import PostList  # Assuming you are using the PostList class view
from . import views

urlpatterns = [
   path('', PostList.as_view(), name='home'),  # Use the class-based view
]






