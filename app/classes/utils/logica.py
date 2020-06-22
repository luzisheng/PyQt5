from classes.utils.logger import logger
from classes.objects.workSpace import workSpace,device, variable
from ..objects.usuario import usuario
import requests, json, os

class Logica():

    __program_files = "/opt"

    settings = { 
        "APISCADA":{
            "Host":"127.0.0.1",
            "Port":"8080"
        }
    }
    
    @staticmethod
    def IniciarSesion(**kwargs):
        _data = {"Usuario":kwargs["Usuario"],"Password":kwargs["Password"]}
        _response =  requests.post("http://%s:%s/Sesion/IniciarSesion" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"]), timeout = 45,json=_data)
        return json.loads(_response.content,object_hook=usuario)

    @staticmethod
    def ObtenerProyectos(**kwargs): # returns a list with all project in database
        _headers = {'Authorization': 'Bearer ' + kwargs["access_token"]}
        result  = requests.get("http://%s:%s/Controles/MostrarTodos" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"]), timeout = 45, headers=_headers)
        result.raise_for_status()
        _answer:workSpace = json.loads( result.content ,object_hook=workSpace)
        return _answer

    @staticmethod
    def ObtenerWorkspaces(**kwargs):
        _headers = {'Authorization': 'Bearer ' + kwargs["access_token"]}
        response  = requests.get("http://%s:%s/Controles/ObtenerTodos" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"]), timeout = 45, headers=_headers)
        response.raise_for_status()
        return list(Logica.jsonToList(response.json(),workSpace))

    @staticmethod
    def jsonToList(y:list,type):
        if y is None or len(y) == 0:
            return []
        for x in y:
            yield type(x)

    @staticmethod
    def ObtenerConfiguraciones(**kwargs):
        _headers = {'Authorization': 'Bearer ' + kwargs["access_token"]}
        result  = requests.get("http://%s:%s/Configuraciones/Obtener" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"]), timeout = 45, headers=_headers)
        result.raise_for_status()
        return result.json()

    @staticmethod
    def GuardarConfiguraciones(**kwargs):
        _headers = {'Authorization': 'Bearer ' + kwargs["access_token"]}
        result  = requests.post("http://%s:%s/Configuraciones/Actualizar" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"]), timeout = 45,json=kwargs["data"], headers=_headers)
        result.raise_for_status()
        return result.json()
        
    @staticmethod
    def AbrirProyectoBackup(**kwargs):
        _headers = {'Authorization': 'Bearer ' + kwargs["access_token"]}
        result  = requests.get("http://%s:%s/Controles/Abrir/%s" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"],kwargs["id"]), timeout = 45, headers=_headers)
        result.raise_for_status()
        drivers = []
        for x in result.json()["Drivers"]:
            dev = device(x)
            dev.variables = json.loads( json.dumps(x["Variables"]), object_hook=variable )
            drivers.append(dev)
        work = workSpace({"Id":result.json()["Id"],"Nombre":result.json()["Nombre"], "DriversCount": len(drivers) })
        work.devices = drivers
        return work

    @staticmethod
    def AbrirProyecto(**kwargs):
        _headers = {'Authorization': 'Bearer ' + kwargs["access_token"]}
        response  = requests.get("http://%s:%s/Controles/Abrir/%s" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"],kwargs["id"]), timeout = 45, headers=_headers)
        response.raise_for_status()
        if response.json() == []:
            raise Exception("¡Error! Proyecto no existe")
        return workSpace(response.json())

    @staticmethod
    def ObtenerVariablesFunciones(**kwargs):
        _headers = {'Authorization': 'Bearer ' + kwargs["access_token"]}
        result  = requests.get("http://%s:%s/Controles/ObtenerVariablesFunciones/%s/%s" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"],kwargs["ID"],kwargs["Token"]), timeout = 45, headers=_headers)
        result.raise_for_status()
        return result.json()

    @staticmethod
    def LeerSensor(**kwargs):
        _headers = {'Authorization': 'Bearer ' + kwargs["access_token"]}
        result  = requests.post("http://%s:%s/Controles/LeerSensor/%s/%s" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"],kwargs["ID"],kwargs["Token"]), timeout = 45,json=kwargs["data"],headers=_headers)
        result.raise_for_status()
        _answer:variable = json.loads(result.content, object_hook=variable)
        return _answer

    @staticmethod
    def ActualizarSensor(**kwargs):
        _headers = {'Authorization': 'Bearer ' + kwargs["access_token"]}
        result  = requests.post("http://%s:%s/Controles/ActualizarVariable/%s/%s" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"],kwargs["ID"],kwargs["Token"]), timeout = 45,json=kwargs["data"],headers=_headers)
        result.raise_for_status()
        return result.json()

    @staticmethod
    def Guardar(**kwargs):
        _headers = {'Authorization': 'Bearer ' + kwargs["access_token"]}
        result  = requests.post("http://%s:%s/Controles/Guardar" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"]), timeout = 45,json=kwargs["data"],headers=_headers)
        result.raise_for_status()
        return result.json()

    @staticmethod
    def EliminarProyecto(**kwargs):
        _headers = {'Authorization': 'Bearer ' + kwargs["access_token"]}
        result  = requests.get("http://%s:%s/Controles/Eliminar/%s" % (Logica.settings["APISCADA"]["Host"],Logica.settings["APISCADA"]["Port"],kwargs["id"]), timeout = 45, headers=_headers)
        result.raise_for_status()
        return result.json()

    @staticmethod
    def fileToJSON(fileName):
        Logger = logger()
        try:
            with open(fileName,'r') as f:
                file = json.loads(f.read())
            return file
        except Exception as e:
            Logger.log_error(e)
            return None

    @staticmethod
    def JSONToFile(fileName:str,jsonData):
        Logger = logger()
        try:
            import os
            with open(fileName,'w+') as f:
                f.write(json.dumps(jsonData))
                f.close()
            fileNameStr = os.path.splitext(fileName)[0]
            os.rename(fileName, fileNameStr + '.json')
            return True
        except Exception as e:
            Logger.log_error(e)
            return False

    @staticmethod
    def imageToByteArray(fileName):
        Logger = logger()
        from base64 import b64encode
        try:
            with open(fileName,'rb') as f:
                file = b64encode(f.read())
            return file.decode()
        except Exception as e:
            Logger.log_error(e)
            return None
        
    @staticmethod
    def byteArrayToImage(file):
        from base64 import b64encode, b64decode
        from PyQt5.QtGui import QPixmap, QImage
        from PyQt5.QtCore import QByteArray
        return QPixmap.fromImage(QImage.fromData(QByteArray.fromBase64 ( bytes(file,"utf-8") )))

    @staticmethod
    def LeerConfiguracion():
        Logger = logger()
        try:
            file =  open("%s/Sistema SCADA/setting.json" % Logica.__program_files,"r")
            return json.load(file)
            file.close()
        except: # Si no existe lo crea
            settings =  {"APISCADA":{
                "Host":"127.0.0.1",
                "Port":"8080"
            }}
            file =  open("%s/Sistema SCADA/setting.json" % Logica.__program_files,"w")
            Logger.log_error( Exception("¡Error! No pudo leerse el archivo de configuracion, Generando uno nuevo"))
            file.write(json.dumps(settings))
            file.close()
            return settings

Logica.settings = Logica.LeerConfiguracion()

    

