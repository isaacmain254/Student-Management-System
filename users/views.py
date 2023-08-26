from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    # register a new user
    if request.method != 'POST':
        # Display a blank registration form
        form = UserCreationForm()
    
    else:
        # process complete form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # login and redirect user to dashboard
            login(request, new_user)
            return redirect('students:dashboard' )
        
    # Display a blank or invlid page
    context = {'form': form}
    return render(request, 'registration/register.html', context)







# def logout_view(request):
#     logout(request)
#     # Redirect to a success page.
#     return redirect('students:index')
