from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


def register(request):
    """Register a new user."""

    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()

            # Auto login after register
            login(request, new_user)

            return redirect('blogs:home')

    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})
