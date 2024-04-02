class Cliente:
    def __init__(self, nombre, correo_electronico, nit):
        self.nombre = nombre
        self.correo_electronico = correo_electronico
        self.nit = nit

    def serializar(self):
        return {
            'nombre': self.nombre,
            'correo_electronico': self.correo_electronico,
            'nit': self.nit
        }
