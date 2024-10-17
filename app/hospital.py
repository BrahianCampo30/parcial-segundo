from .medico import Medico
from .paciente import Paciente
from .cita import Cita
from .agenda import Agenda
from datetime import datetime

class Hospital:
    def __init__(self):
        self.pacientes, self.medicos = [], []
        self.agenda = Agenda()

    def agregar_paciente(self, id, nom, cel, cor):
        pac = Paciente(id, nom, cel, cor)
        self.pacientes.append(pac)
        print(f"Paciente {nom} agregado.")

    def agregar_medico(self, id, nom, cel, cor, esp):
        med = Medico(id, nom, cel, cor, esp)
        self.medicos.append(med)
        print(f"Médico {nom} agregado.")

    def buscar_paciente(self, id):
        return next((p for p in self.pacientes if p.identificacion == id), None)

    def buscar_medico(self, id):
        return next((m for m in self.medicos if m.identificacion == id), None)

    def obtener_medicos_por_especialidad(self, esp):
        return [m for m in self.medicos if m.especialidad.lower() == esp.lower()]

    def agendar_cita(self, pac, med, fecha_str, motivo):
        fecha = datetime.strptime(fecha_str, "%Y-%m-%d %H:%M")
        if med.verificar_disponibilidad(fecha):
            cita = Cita(pac, med, fecha, motivo)
            med.agenda.agregar_cita(cita)
            self.agenda.agregar_cita(cita)
            print(f"Cita agendada: {pac.nombre} con {med.nombre} el {fecha}")
            pac.recibir_notificacion(f"Cita con {med.nombre} el {fecha}")
        else:
            print(f"Sin disponibilidad para {med.nombre} el {fecha}")

    def cancelar_cita(self, cita):
        cita.cancelar_cita("Cancelada")
        cita.medico.agenda.cancelar_cita(cita)
        self.agenda.cancelar_cita(cita)
        print(f"Cita cancelada: {cita}")

    def obtener_citas_paciente(self, pac):
        return [c for c in self.agenda.citas_pendientes if c.paciente == pac]
