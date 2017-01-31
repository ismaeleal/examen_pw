from django.shortcuts import render
from .forms import iniForm
from .forms import CircuscricionesForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.views.generic.list import ListView
from .models import Circuscricion
from .models import Mesa

# Create your views here.

def iniView(request):
	form = iniForm(request.POST or None)
	if form.is_valid():
		form_data = form.cleaned_data
		
		abc3 = form_data.get("usuario")
		acb4 = form_data.get("contraseña")
		
		obj = authenticate( username=abc3, password=acb4)
		if obj is not None:
			if obj.is_active:
				login(request, obj)
				return HttpResponseRedirect("/")
			
		else:
			return HttpResponseRedirect("/no_valido")

	context = {
		"el_form1":form,

	}

	return render(request, "inicio.html",context,)

class PostList(ListView):
    model = Circuscricion
    template_name = 'Circuscriciones.html'
    paginate_by = 6
    context_object_name = "circuscricion"

def circuscricionView(request):
	form = CircuscricionesForm(request.POST or None)
	if form.is_valid():
		form_data = form.cleaned_data
		abc = form_data.get("nombre")
		abc2 = form_data.get("numero")
		
		obj = Circuscricion.objects.create(nombre=abc, numero=abc2)
	context = {
		"el_form":form,
	}

	return render(request, "Circuscriciones_registro.html",context)
def mesalView(request, nombre):
	mensaje = Circuscricion.objects.get(nombre=nombre)
	comentario = Mesa.objects.filter(circuscricion=mensaje)
       
	return render(request, "mesa.html", { 'circuscricion':comentario})




   



