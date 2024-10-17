class Cita:
    def __init__(self, pac, med, fecha, mot):
        self.pac = pac
        self.med = med
        self.fecha = fecha
        self.mot = mot
        self.estado = "Pendiente"

    def cancelar_cita(self, mot_cancel):
        self.estado = "Cancelada"
        self.mot_cancel = mot_cancel

    def __repr__(self):
        return f"Cita de {self.pac.nom} con {self.med.nom} el {self.fecha}"