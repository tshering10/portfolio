from django.shortcuts import render,redirect
from django.contrib import messages
from website.form import ContactForm
# Create your views here.
def home(request):
    return render(request, 'website/home.html')

def about(request):
    return render(request, 'website/about.html')

def projects(request):
    return render(request, 'website/projects.html')

def contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your message has been sent successfully.')
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})