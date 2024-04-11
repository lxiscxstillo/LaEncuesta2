from RangoEncuesta import RangoEncuesta

class Encuesta:
    def __init__(self):
        self.rangoEncuesta = RangoEncuesta()
        self.rango1 = RangoEncuesta.getRangoEdad[0]
        self.rango2 = RangoEncuesta.getRangoEdad[1]
        self.rango3 = RangoEncuesta.getRangoEdad[2]
        self.calificacionCasados = [0, 10]
        self.calificacionSolteros = [0, 10]

    def agregarOpinionRango1Casado(self, opinionEncuestado):
        if self.rango1 != self.rango2 and self.rango1 != self.rango3:
            self.rangoEncuesta.agregarOpinionCasado(opinionEncuestado)

    def agregarOpinionRango2Soltero(self, opinionEncuestado, estadoCivil):
        if self.rango2 != self.rango1 and self.rango2 != self.rango3:
            self.rangoEncuesta.agregarOpinionSoltero(opinionEncuestado, estadoCivil)

    def darPromedio(self):
        self.rangoEncuesta.darPromedio()

    def darPromedioCasados(self):
        self.rangoEncuesta.darPromedioCasados()
    