from Repositorios.MateriaRepositorio import MateriaRepositorio
from Repositorios.DepartamentoRepositorio import DepartamentoRepositorio
from Modelos.Materia import Materia
from Modelos.Departamento import Departamento

class ControladorMateria():

    def __init__(self):
        self.materiaRepositorio = MateriaRepositorio()
        self.departamentoRepositorio = DepartamentoRepositorio()

    def index(self):
        return self.materiaRepositorio.findAll()

    def create(self, infoMateria):
        nuevoMateria = Materia(infoMateria)
        return self.materiaRepositorio.save(nuevoMateria)

    def show(self, id):
        elMateria = Materia(self.materiaRepositorio.findById(id))
        return elMateria.__dict__

    def update(self, id, infoMateria):
        MateriaActual = Materia(self.materiaRepositorio.findById(id))
        MateriaActual.nombre = infoMateria["nombre"]
        MateriaActual.creditos = infoMateria["creditos"]
        return self.materiaRepositorio.save(MateriaActual)

    def delete(self, id):
        return self.materiaRepositorio.delete(id)

    #relacion dep y mat

    def asignarDepartamento(self, id, id_Departamento):
        materiaActual = Materia(self.materiaRepositorio.findById(id))
        departamentoActual = Departamento(self.departamentoRepositorio.findById(id_Departamento))
        materiaActual.departamento = departamentoActual
        return self.materiaRepositorio.save(materiaActual)

