from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST

# Create your views here.

@login_required
def index(request):
    return render(request, 'account/layout.html')

@require_POST
def sign_in(request):
    '''Processes information sent by the user from the log-in page.
    
    This view accepts only 'POST' method requests.
    '''
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home:index'))
    
    