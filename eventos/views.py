from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def eventos(request):
    return render(request, 'my_events.html')
    
    
