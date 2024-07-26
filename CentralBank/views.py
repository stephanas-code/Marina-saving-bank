from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def markets(request):
    return render(request, "markets.html")

def about(request):
    return render(request, "about.html")

def blog(request):
    return render(request, "blog.html")

def contact(request):
    return render(request, "contact.html")

def partners(request):
    return render(request, "partners.html")

def legal(request):
    return render(request, "legal-docs.html")