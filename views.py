from django.contrib import messages
from django.shortcuts import redirect, render
import bcrypt
from .decorators import login_required


@login_required
def index(request):

    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)
