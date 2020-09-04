class fraccion:
    def __init__ (self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador
    def mostrar (self):
        print (self.numerador , "/"  , self.denominador)

    def sumar (self, fraccion2):
        resultado = fraccion(1,1)#inicializacion de la variable goo
        resultado.numerador = self.numerador*fraccion2.denominador + self.denominador*fraccion2.numerador
        resultado.denominador = self.denominador*fraccion2.denominador
        return resultado

    def restar (self, fraccion2):
        resultado = fraccion(1,1)
        resultado.numerador = self.numerador*fraccion2.denominador - self.denominador*fraccion2.numerador
        resultado.denominador = self.denominador*fraccion2.denominador
        return resultado

    def multiplicacion (self, fraccion2):
        resultado = fraccion(1,1)
        resultado.numerador = self.numerador*fraccion2.numerador
        resultado.denominador = self.denominador*fraccion2.denominador
        return resultado
        
        
        

        
        
        


        
