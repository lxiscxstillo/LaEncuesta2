from Encuesta import Encuesta

class RangoEncuesta:
    def __init__(self):
        self.opinionesCasados = []
        self.opinionesSolteros = []
        self.rangoEdad = [[1, 17], [18, 55], [56, None]]
        self.estadoCivil = ["casado", "soltero"]
        self.contadorCasados = 0
        self.contadorSolteros = 0
        self.encuesta = Encuesta()

    def darPromedioCasados(self):
        return sum(self.opinionesCasados) / len(self.opinionesCasados)
    
    def getRangoEdad(self):
        return self.rangoEdad
    
    def diferenciarEstadoCivil(self):
        if self.estadoCivil == self.estadoCivil[0]:
            self.contadorCasados += 1
            return self.contadorCasados
        else:
            self.contadorSolteros += 1
            return self.contadorSolteros
        
    def darTotalOpinionCasados(self):
        return sum(self.encuesta.calificacionCasados)
    
    def darTotalOpinionSolteros(self):
        return sum(self.encuesta.calificacionSolteros)
    
    def darPromedio(self):
        (self.darTotalOpinionCasados() + self.darTotalOpinionSolteros()) / (self.contadorCasados + self.contadorSolteros)

    def agregarOpinionCasado(self, opinionEncuestado):
        if self.estadoCivil == self.estadoCivil[0]:
            self.opinionesCasados.append(opinionEncuestado)

    def agregarOpinionSoltero(self, opinionEncuestado, estadoCivil):
        if estadoCivil == self.estadoCivil[1]:
            self.opinionesSolteros.append(opinionEncuestado)

    def darPromedioCasados(self):
        self.darTotalOpinionCasados() / self.contadorCasados