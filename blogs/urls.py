from . import views
from django.urls import path
from .views import DevProfileView, ContactFormView

# from .views import my_blog

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', DevProfileView.as_view(), name='about'),
    # path('my_blog/', my_blog, name='my_blog'),
]

