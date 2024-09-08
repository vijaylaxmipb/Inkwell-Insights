from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from .forms import ContactForm

# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "blog/post.html"

# Function-based view
# def my_blog(request):
#     posts = Post.objects.all()
#     return render(request, 'post.html', {'posts': posts})

class DevProfileView(TemplateView):
    template_name = "dev_profile.html"

class ContactFormView(FormView):
    template_name = 'contact_form.html'
    form_class = ContactForm
    success_url = '/success/' 

    def form_valid(self, form):
        # Handle the form submission
        return super().form_valid(form)

