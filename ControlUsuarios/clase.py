from bson.objectid import ObjectId
from pymongo import *
import time
import os
import csv
import json
from datetime import datetime
from bson.json_util import dumps




class ClaseDriver(object):
    """ ItemsDriver implemeta las funcionalidades CRUD para administrar items """

    def __init__(self):

        self.client = MongoClient('mongodb://hugobarzano:hugobarzano@ds017173.mlab.com:17173/dispositivosmoviles')
        self.database=self.client.get_default_database()
        self.database['clase']
        self.database['sesion']

    def createSesion(self, clave_sesion):
        self.database.sesion.remove()
        sesion={"clave_sesion":clave_sesion,"fecha_sesion":datetime.now().strftime('%Y-%m-%d')}
        self.database.sesion.insert(sesion)




    def createClase(self, fichero):
        self.database.clase.remove()
        csvfile = open(fichero, 'r')
        fieldnames = ("Nombre","DNI")
        reader = csv.DictReader( csvfile, fieldnames)
        for row in reader:
            row["asistencia"]="False"
            self.database.clase.insert(row)

    def createClaseFromReader(self, reader):
        self.database.clase.remove()
        for row in reader:
            row["assitencia"]="False"
            self.database.clase.insert(row)

    def readClase(self):
        return self.database.clase.find()


    def destroyDriver(self,organizacion):
        self.database.clase.remove({'organizacion':organizacion})
