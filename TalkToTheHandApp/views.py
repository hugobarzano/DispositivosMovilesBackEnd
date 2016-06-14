from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from django.http import HttpResponse
from django.views.generic.base import View
from forms import *
from sala import *
from django.views.decorators.csrf import csrf_exempt
gestorSala= SalaDriver()

def index(request):
    cursor=gestorSala.database.salas.find()
    salas=[]
    for i in cursor:
        print i
        objeto_sala=Sala.build_from_json(i)
        salas.append(objeto_sala)

    return render(request, 'TalkToTheHandApp/index.html', {'salas': salas})


def salaCreator(request):
    if request.method=='GET':
        form = SalaForm()
        #print request.GET['organizacion']
        #form = ItemForm3(organizacion=request.GET['organizacion'])
        return render(request, 'TalkToTheHandApp/nueva_sala.html', {'form': form})
    else:
        mydic=dict(request.POST)
        form = SalaForm(request.POST)
        if form.is_valid():
            sala = Sala.build_from_json({"nombre_sala":form.data['nombre'],
                "fecha_sala": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "descripcion_sala": form.data['descripcion'],
                "usuario":"usuario",
                "datos_sala":[]})
            gestorSala.createSala(sala)
            return render(request, 'TalkToTheHandApp/index.html')
        else:
            return render(request, 'TalkToTheHandApp/nueva_sala.html', {'form': form})

@csrf_exempt
def salaCreatorAndroid(request):
    if request.method=='POST':
        mydic=dict(request.POST)
        print mydic["username"][0]
        print mydic["nombre"][0]
        print mydic["descripcion"][0]

        sala = Sala.build_from_json({"nombre_sala":mydic["nombre"][0],
            "fecha_sala": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "descripcion_sala": mydic["descripcion"][0],
            "usuario": mydic["username"][0],
            "datos_sala":[]})
        gestorSala.createSala(sala)
        return HttpResponse("OK")
    else:
        mydic=dict(request.GET)
        print mydic["username"][0]
        print mydic["nombre"][0]
        print mydic["descripcion"][0]

        sala = Sala.build_from_json({"nombre_sala":mydic["nombre"][0],
            "fecha_sala": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "descripcion_sala": mydic["descripcion"][0],
            "usuario": mydic["username"][0],
            "datos_sala":[]})
        gestorSala.createSala(sala)
        return HttpResponse("OK")
@csrf_exempt
def sala(request,id_sala):
    sala_object=Sala()
    cursor=gestorSala.database.salas.find({"_id":ObjectId(id_sala)})
    for i in cursor:
        sala_object = Sala.build_from_json(i)

    return render(request, 'TalkToTheHandApp/sala.html',{"sala_object":sala_object,"id":str(sala_object._id)})

@csrf_exempt
def enviar(request):
    if request.method=='GET':
        mydic=dict(request.GET)
        print mydic["sala"][0]

        mensaje= mydic["username"][0]+" -- "+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+": \n"+ mydic["mensaje"][0]
        print mensaje
        gestorSala.database.salas.update({"_id":ObjectId(mydic["sala"][0])},{"$addToSet": {"datos_sala" : str(mensaje),}})
        return HttpResponse("OK")
    else:
        mydic=dict(request.POST)
        mensaje= mydic["username"][0]+" -- "+datetime.now().strftime('%Y-%m-%d %H:%M:%S')+": \n"+ mydic["mensaje"][0]
        gestorSala.database.salas.update({"_id":ObjectId(mydic["sala"][0])},{"$addToSet": {"datos_sala" : str(mensaje),}})
        return HttpResponse("OK")

def updateSala(request):
    if request.method=='GET':
        mydic=dict(request.GET)
        print mydic
        print mydic["id_sala"][0]
        cursor = gestorSala.database.salas.find({"_id":ObjectId(mydic["id_sala"][0])})
        response='<div class="actualizame">'
        for i in cursor:
            objeto=Sala.build_from_json(i)

        for j in objeto.datos_sala:
            response=response+'<h5><strong>#</strong><p style="overflow-wrap:break-word;">'+str(j)+'</p></h5><hr></div>'

        return HttpResponse(response)





@csrf_exempt
def salasJson(request):
    if request.method == 'GET':
        default={"_id":"ID","nombre":"Nombre","descripcion":"Descripcion","fecha":"Fecha"}
        aux7=[]
        aux7.append(default)
        respuesta={"salas":aux7}
        aux=[]
        aux3=[]
        try:
            lista_salas=gestorSala.database.salas.find({}).sort([("fecha_sala", -1)]).limit(150)
            for i in lista_salas:
                aux = Sala.build_from_json(i)
                aux2=aux.get_as_json()
                aux2["_id"]=str(aux2["_id"])
                aux4={"_id":aux2["_id"],"nombre":aux2["nombre_sala"],"descripcion":aux2["descripcion_sala"],"fecha":aux2["fecha_sala"]}
                aux3.append(aux4)
            respuesta={"salas":aux3}
        except KeyError as e:
            raise Exception("No tienes objetos asociados : {}".format(e.message))
        return JsonResponse(respuesta,safe=False)
    else:
        default={"_id":"ID","nombre":"Nombre","descripcion":"Descripcion","fecha":"Fecha"}
        aux7=[]
        aux7.append(default)
        respuesta={"salas":aux7}
        aux=[]
        aux3=[]
        try:
            lista_salas=gestorSala.database.salas.find({}).sort([("fecha_sala", -1)]).limit(150)
            for i in lista_salas:
                aux = Sala.build_from_json(i)
                aux2=aux.get_as_json()
                aux2["_id"]=str(aux2["_id"])
                aux4={"_id":aux2["_id"],"nombre":aux2["nombre_sala"],"descripcion":aux2["descripcion_sala"],"fecha":aux2["fecha_sala"]}
                aux3.append(aux4)
            respuesta={"salas":aux3}
        except KeyError as e:
            raise Exception("No tienes objetos asociados : {}".format(e.message))
        return JsonResponse(respuesta,safe=False)
