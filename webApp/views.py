from django.shortcuts import render

# Create your views here.
def inicio(request):
	return render(request, 'webApp/index.html')

def liga(request):
	return render(request, 'webApp/about.html')

def resultados(request):
	return render(request, 'webApp/services.html')

def apuestas(request):
	return render(request, 'webApp/blog.html')

def contacto(request):
	return render(request, 'webApp/contact.html')



