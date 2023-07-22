from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET
from register.models import ticket

@login_required
@require_GET
def my_eventos(request):

    my_even = ticket.objects.filter(user=request.user)

    context = {
        'evento':my_even
    }
    
    return render(request, 'my_events.html', context)
    
    
