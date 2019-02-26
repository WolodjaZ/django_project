from django.shortcuts import render

def home(request):
    """Main page"""
    return render(request, 'forum/home.html')
