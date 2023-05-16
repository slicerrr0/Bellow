from django.shortcuts import render

# Create your views here.

def index(request):
    '''
    Renders the main page of the website (located at ~templates/home/index.html).
    '''
    return render(request, 'home/index.html')