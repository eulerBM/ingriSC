from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from register.forms import forms_event

@login_required
def register(request):

    if request.method == 'POST':
        form = forms_event(request.POST)
               
        if form.is_valid(): 
            form.save()

            return redirect('register')
        
    else:
        return render (request, 'register.html', {'form': forms_event()})
    
    
        
