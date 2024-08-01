from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import View
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.contrib.auth.decorators import user_passes_test, login_required
from main.models import UserProfile
from main.forms import NotaModelForm

# Vista abierta a todo público
def inicio(req):
  return render(req, 'index.html')

# ClassView abierta
class RegistroView(View):

  def get(self, req):
    return render(req, 'registration/registro.html')
  
  def post(self, req):
    # 1. Recuperamos los datos del formulario
    username = req.POST['username']
    email = req.POST['email']
    password = req.POST['password']
    pass_repeat = req.POST['pass_repeat']
    # 2. Validamos que contraseñas concidan
    if password != pass_repeat:
      messages.error(req, 'Contraseñas no coinciden')
      return redirect('/accounts/registro')
    # 3. Creamos al usuario
    user = User.objects.create_user(username=username, email=email, password=password)
    # 4. Creamos el user_profile
    UserProfile.objects.create(user=user, rol='empleado')
    # 5. Feedback y redirigimos
    messages.success(req, 'Usuario creado')
    return redirect('/')

# ClassView Cerrada
class NotaView(View):
  
  # el siguiente código protege tanto el GET como el POST
  @method_decorator(login_required)
  def dispatch(self, *args, **kwargs):
    return super().dispatch(*args, **kwargs)

  def get(self, req):
    form = NotaModelForm()
    context = {
      'form': form
    }
    return render(req, 'nueva_nota.html', context)
  
  def post(self, req):
    # 1. Recuperamos los datos del formulario
    form = NotaModelForm(req.POST)
    # 2. Guardamos en la BBDD
    form.save()
    # 3. Le damos feedback al usuario
    messages.success(req, 'Nota Creada!')
    # 4. Redirigimos
    return redirect('/')
  

  
