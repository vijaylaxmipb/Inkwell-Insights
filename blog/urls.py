from . import views
from django.urls import path
# from .views import my_blog

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    # path('my_blog/', my_blog, name='my_blog'),
]