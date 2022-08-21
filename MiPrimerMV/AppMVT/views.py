from multiprocessing import context
from urllib import request
from django.http import HttpRequest
from django.http import HttpResponse
import datetime
from AppMVT.models import Familiar
from django.template import loader

# Create your views here.
def familiares(self):
    fam1= Familiar(nombre="Leonardo",apellido="Palacios",dni="37988455",fechaDeNacimiento="1994-01-22",trabajo="Preceptor")
    fam1.save()
    fam2= Familiar(nombre="Melina",apellido="Palacios",dni="34986555",fechaDeNacimiento="1984-02-03",trabajo="Docente")
    fam2.save()
    fam3= Familiar(nombre="Sandra",apellido="Lopez",dni="13277858",fechaDeNacimiento="1994-07-14",trabajo="Recepcionista")
    fam3.save()
    diccionario={"familia1":fam1,"familia2":fam2,"familia3":fam3}
    plantilla=loader.get_template("template1.html")
    fin=plantilla.render(diccionario)
    return HttpResponse(fin)

