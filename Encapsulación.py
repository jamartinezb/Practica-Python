class IngresoOficina:

    def __init__(self,identificador, ciudad):
        self.__identificador = identificador
        self.__ciudad = ciudad
        self.__oficina = None
        
    @property
    def oficina(self):
        return self.__oficina
            
    @oficina.setter
    def oficina(self, oficina):
        if oficina in self.__ciudad:
            self.__oficina = oficina
        else:
            raise ValueError(f'La oficina {oficina} no esta en directorio del {self.__ciudad}')
            
            
        ingreso = IngresoOficina(123,['Ibague','centro'])
        print(ingreso.oficina)
        ingreso.oficina = 'Ibague'
        print(ingreso.oficina)