from Repositorios.EstudianteRepositorio import EstudianteRepositorio
from Modelos.Estudiante import Estudiante

class ControladorEstudiante():

    def __init__(self):
        self.estudianteRepositorio = EstudianteRepositorio()

    def index(self):
        return self.estudianteRepositorio.findAll()

    def create(self, infoEstudiante):
        nuevoEstudiante = Estudiante(infoEstudiante)
        return self.estudianteRepositorio.save(nuevoEstudiante)

    def show(self, id):
        elEstudiante = Estudiante(self.estudianteRepositorio.findById(id))
        return elEstudiante.__dict__

    def update(self, id, infoEstudiante):
        estudianteActual = Estudiante(self.estudianteRepositorio.findById(id))
        estudianteActual.cedula = infoEstudiante["cedula"]
        estudianteActual.nombre = infoEstudiante["nombre"]
        estudianteActual.apellido = infoEstudiante["apellido"]
        estudianteActual.direccion = infoEstudiante["direccion"]
        return self.estudianteRepositorio.save(estudianteActual)

    def delete(self, id):
        return self.estudianteRepositorio.delete(id)
