from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contacts(request):
    return render(request, 'contacts.html')

def find_us(request):
    return render(request, 'find_us.html')

# Страницы по предметной области (Проектная организация)
def projects(request):
    return render(request, 'projects.html')

def services(request):
    return render(request, 'services.html')