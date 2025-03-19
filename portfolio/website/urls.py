from django.urls import path
from website.views import home, about, projects, contact_form
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about_us'),
    path('projects/', projects, name='projects'),
    path('contact/', contact_form, name='contact'),
]
