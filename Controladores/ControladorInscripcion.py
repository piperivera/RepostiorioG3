from Repositorios.InscripcionRepositorio import InscripcionRepositorio
from Repositorios.MateriaRepositorio import MateriaRepositorio
from Repositorios.EstudianteRepositorio import EstudianteRepositorio
from Modelos.Materia import Materia
from Modelos.Estudiante import Estudiante
from Modelos.Inscripcion import Inscripcion

class ControladorInscripcion():

    def __init__(self):
        self.inscripcionRepositorio = InscripcionRepositorio()
        self.estudianteRepositorio = EstudianteRepositorio()
        self.materiasRepositorio = MateriaRepositorio()

    def index(self):
        return self.inscripcionRepositorio.findAll()

#Asignacion estudiante y materia
    def create(self, infoInscripcion, id_estudiante, id_materia):
        nuevaInscripcion = Inscripcion(infoInscripcion)
        elEstudiante = Estudiante(self.estudianteRepositorio.findById(id_estudiante))
        laMateria = Materia(self.materiasRepositorio.findById(id_materia))
        nuevaInscripcion.estudiante = elEstudiante
        nuevaInscripcion.materia = laMateria
        return self.inscripcionRepositorio.save(nuevaInscripcion)

    def show(self, id):
        elInscripcion = Inscripcion(self.inscripcionRepositorio.findById(id))
        return elInscripcion.__dict__

#Modificacion de inscripcion(estudiante y materia)
    def update(self, id, infoInscripcion, id_estudiante, id_materia):
        laInscripcion = Inscripcion(self.inscripcionRepositorio.findById(id))
        laInscripcion.año = infoInscripcion["año"]
        laInscripcion.semestre = infoInscripcion["semestre"]
        laInscripcion.notaFinal = infoInscripcion["nota_final"]
        elEstudiante = Estudiante(self.estudianteRepositorio.findById(id_estudiante))
        laMateria = Materia(self.materiasRepositorio.findById(id_materia))
        laInscripcion.estudiante = elEstudiante
        laInscripcion.materia = laMateria
        return self.inscripcionRepositorio.save(laInscripcion)

    def delete(self, id):
        return self.inscripcionRepositorio.delete(id)

    def listarInscritosEnMateria(self, id_materia):
        return self.inscripcionRepositorio.getListadoInscritosEnMateria(id_materia)