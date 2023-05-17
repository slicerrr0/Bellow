from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Create your views here.

@login_required
def index(request):
    return render(request, 'account/layout.html')

def sign_in(request):
    if request.method == 'GET':
        return render(request, 'account/index.html')
    
    