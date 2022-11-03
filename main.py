from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve
from Controladores.ControladorEstudiante import ControladorEstudiante
from Controladores.ControladorMateria import ControladorMateria
from Controladores.ControladorDepartamento import ControladorDepartamento
from Controladores.ControladorInscripcion import ControladorInscripcion

app = Flask(__name__)
cors = CORS(app)

miControladorEstudiante = ControladorEstudiante()
miControladorMateria = ControladorMateria()
miControladorDepartamento = ControladorDepartamento()
miControladorInscripcion = ControladorInscripcion()

@app.route("/",methods=['GET'])
def test():
    json = {}
    json["message"]="Server running ..."
    return jsonify(json)
#Carga el archivo json ,lo lee y lo resonator
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

#####################Servicios Estudiante#########################################################################
@app.route("/estudiantes",methods=['GET'])
def getEstudiantes():
    json = miControladorEstudiante.index()
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['GET'])
def getEstudiante(id):
    json = miControladorEstudiante.show(id)
    return jsonify(json)

@app.route("/estudiantes",methods=['POST'])
def crearEstudiante():
    data = request.get_json()
    json = miControladorEstudiante.create(data)
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['PUT'])
def modificarEstudiante(id):
    data = request.get_json()
    json = miControladorEstudiante.update(id,data)
    return jsonify(json)

@app.route("/estudiantes/<string:id>",methods=['DELETE'])
def eliminarEstudiante(id):
    json = miControladorEstudiante.delete(id)
    return jsonify(json)


#################################################################################################################

#####################Servicios Departamento######################################################################
@app.route("/departamentos",methods=['POST'])
def crearDepartamento():
    data = request.get_json()
    json = miControladorDepartamento.create(data)
    return jsonify(json)

@app.route("/departamentos",methods=['GET'])
def getDepartamentos():
    json = miControladorDepartamento.index()
    return jsonify(json)


#################################################################################################################



#####################Servicios Materias##########################################################################
@app.route("/materias",methods=['POST'])
def crearMateria():
    data = request.get_json()
    json = miControladorMateria.create(data)
    return jsonify(json)

#Endpoint para mostrar todas las materias
@app.route("/materias",methods=['GET'])
def getMaterias():
    json = miControladorMateria.index()
    return jsonify(json)

@app.route("/materias/<string:id>/departamento/<string:id_departamento>",methods=['PUT'])
def asignarDepartamento(id, id_departamento):
    json = miControladorMateria.asignarDepartamento(id, id_departamento)
    return jsonify(json)


#################################################################################################################

###################################Servicios Inscripcion#########################################################

@app.route("/inscripciones/estudiante/<string:id_estudiante>/materia/<string:id_materia>",methods=['POST'])
def crearInscripcion(id_estudiante, id_materia):
    data = request.get_json()
    json = miControladorInscripcion.create(data, id_estudiante, id_materia)
    return jsonify(json)

@app.route("/inscripciones",methods=['GET'])
def getInscripciones():
    json = miControladorInscripcion.index()
    return jsonify(json)

@app.route("/inscripciones/materia/<string:id_materia>",methods=['GET'])
def inscritosEnMateria(id_materia):
    json = miControladorInscripcion.listarInscritosEnMateria(id_materia)
    return jsonify(json)

#################################################################################################################


#Cuando el nombre sea igual a main dataconfig cargar el load despues hace un print donde muestra la url
if __name__=='__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app,host=dataConfig["url-backend"],port=dataConfig["port"])

#print("Felipe")
