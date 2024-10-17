from .persona import Persona
from .notificacion import Notificacion

class Paciente(Persona):
    def __init__(self, id, nom, cel, cor):
        super().__init__(id, nom, cel, cor)
        self.med_pref = None

    def asignar_medico_preferencia(self, med):
        self.med_pref = med
        print(f"Médico {med.nom} asignado como preferencia para {self.nom}")

    def recibir_notificacion(self, msg):
        notif = Notificacion(self)
        notif.enviar_notificacion(msg)
