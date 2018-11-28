from django.shortcuts import render

# Create your views here.
def inicio(request):
	return render(request, 'webApp/index.html')

def datos(request):
	return render(request, 'webApp/blog.html')

def contacto(request):
	return render(request, 'webApp/contact.html')

def elementos(request):
	return render(request, 'webApp/elements.html')

def servicio(request):
	return render(request, 'webApp/services.html')

def detalle(request):
	return render(request, 'webApp/about.html')


