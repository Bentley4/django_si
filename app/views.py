# Create your views here.
import django.http
import django.template.loader
import django.template	

def page(request):
    return django.http.HttpResponse("hello!")

def page2(request):
    t = django.template.loader.get_template("pagina.html")
    c = django.template.Context()
    return django.http.HttpResponse(t.render(c))

