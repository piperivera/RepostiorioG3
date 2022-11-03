from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Inscripcion import Inscripcion
from bson import ObjectId

class InscripcionRepositorio(InterfaceRepositorio[Inscripcion]):

    def getListadoInscritosEnMateria(self, id_materia):
        theQuery = {"materia.$id": ObjectId(id_materia)}
        return self.query(theQuery)