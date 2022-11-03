from Repositorios.DepartamentoRepositorio import DepartamentoRepositorio
from Modelos.Departamento import Departamento

class ControladorDepartamento():

    def __init__(self):
        self.departamentoRepositorio = DepartamentoRepositorio()

    def index(self):
        return self.departamentoRepositorio.findAll()

    def create(self, infoDepartamento):
        nuevoDepartamento = Departamento(infoDepartamento)
        return self.departamentoRepositorio.save(nuevoDepartamento)

    def show(self, id):
        elDepartamento = Departamento(self.departamentoRepositorio.findById(id))
        return elDepartamento.__dict__

    def update(self, id, infoDepartamento):
        DepartamentoActual = Departamento(self.departamentoRepositorio.findById(id))
        DepartamentoActual.nombre = infoDepartamento["nombre"]
        DepartamentoActual.descripcion = infoDepartamento["descripcion"]
        return self.departamentoRepositorio.save(DepartamentoActual)

    def delete(self, id):
        return self.departamentoRepositorio.delete(id)