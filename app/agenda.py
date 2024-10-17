class Agenda:
    def __init__(self):
        self.pend = []
        self.real = []
        self.cancel = []

    def agregar_cita(self, cita):
        self.pend.append(cita)

    def cancelar_cita(self, cita):
        if cita in self.pend:
            self.pend.remove(cita)
            self.cancel.append(cita)

    def verificar_disponibilidad(self, fecha):
        return all(c.fecha != fecha for c in self.pend)
