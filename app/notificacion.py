from .correo import Correo
from .celular import Celular
from .whatsapp import whatsapp


class Notificacion:
    def __init__(self, per):
        self.per = per
        self.mds = [Correo(), Celular(), whatsapp()]

    def enviar_notificacion(self, msg):
        for m in self.mds:
            m.enviar_notificacion(self.per, msg)

