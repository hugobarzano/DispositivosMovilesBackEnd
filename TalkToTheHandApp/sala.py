# coding=utf8
# -*- coding: utf8 -*-
# vim: set fileencoding=utf8 :
import unicodedata
from bson.objectid import ObjectId
from pymongo import *
import time
import os
from datetime import datetime

class Sala(object):
    """Clase para almacenar informacion de los Salas"""

    def __init__(self, sala_id=None,nombre_sala=None,fecha_sala=None, descripcion_sala=None,usuario=None,datos_sala=None):

        if sala_id is None:
            self._id = ObjectId()
        else:
            self._id = sala_id
        self.nombre_sala=nombre_sala
        self.fecha_sala = fecha_sala
        self.descripcion_sala = descripcion_sala
        self.usuario=usuario
        self.datos_sala=datos_sala

    def get_as_json(self):
        """ Metodo que devuelve el objeto en formato Json, para almacenar en MongoDB """
        return self.__dict__


    @staticmethod
    def build_from_json(json_data):
        """ Metodo usado para contruir objetos sala apartir de Json"""
        if json_data is not None:
            try:
                #print"Jsonnnn"
                #print json_data
                return Sala(json_data.get('_id', None),
                    json_data['nombre_sala'],
                    json_data['fecha_sala'],
                    json_data['descripcion_sala'],
                    json_data['usuario'],
                    json_data['datos_sala'])
            except KeyError as e:
                raise Exception("Clave no encontrada en json: {}".format(e.message))
        else:
            raise Exception("No hay datos para crear una sala!")


class SalaDriver(object):
    """ ItemsDriver implemeta las funcionalidades CRUD para administrar items """

    def __init__(self):

        self.client = MongoClient('mongodb://hugobarzano:hugobarzano@ds017173.mlab.com:17173/dispositivosmoviles')
        self.database=self.client.get_default_database()
        self.database['salas']


    def createSala(self, sala):
        if sala is not None:
            self.database.salas.save(sala.get_as_json())
        else:
            raise Exception("Imposible crear sala")


    def destroyDriver(self):
        self.database.items.remove()
