from .persona import Persona
from .agenda import Agenda

class Medico(Persona):
    def __init__(self, id, nom, cel, cor, esp):
        super().__init__(id, nom, cel, cor)
        self.esp = esp
        self.agenda = Agenda()

    def verificar_disponibilidad(self, fecha):
        return self.agenda.verificar_disponibilidad(fecha)

