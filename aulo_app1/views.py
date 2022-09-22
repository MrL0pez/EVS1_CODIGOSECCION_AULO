from django.http import HttpResponse
def vista111(request):
	return HttpResponse("<h1>Hola Mundo</h1>"+"<h2>profe no sea malo</h2>"+"<h3>y pongame una buena notita plz</h3>")

def vista112(request):
    return HttpResponse("<h1>Hola profe</h1>"+"<h2>reitero</h2>"+"<h3>por favor pongame buena nota</h3>")