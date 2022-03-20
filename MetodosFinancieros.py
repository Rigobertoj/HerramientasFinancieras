import pandas as pd
class MetodosFinancieros():
    nombre = None 
    ubicacion = None 
    Periodo = None
    
    Liquidez = {
    'capital neto':None, 
    'Razon de liquidez':None, 
    'Prubea de acido': None
    }

    Solvencia = {
        'Solvencia total': None,
        'Firmeza': None,
        'Independencia':None
    }

    Estabilidad = {
        'Origen de capital':None,
        'Inversion de capital':None,
        'Valor contable de capital':None
    }
    CicloEconomico = {
        'Utilidad del ejercicio':None,
        'Estudio de la utilidad':None,
        'Margen de ganacias por unidad':None
    }
    RazonesSimples = [Solvencia,Liquidez,Estabilidad]

    def __init__(self):
        pass
#medodo que nos permite recibir como argumentos alguno de los datos de la empresa
#pero primero comprubea si ya hay datos existentes y si los hay solo retorna esos valores para mostrarselos a
#los usuarios de no ser asi recibe los parametros y se los asigna 3 parametros que tiene como valor None 
#y en cuanto se le aplican los cambios o los datos los imprime por pantalla 

#falta realizar la logica que nos permita que si solo se quiere cambiar un parametro solo se cambie ese parametro 

    def Info(self, Name = None , Ubicasion = None, Periodo = None):
        if Name == None and Ubicasion == None and Periodo == None:
            if self.nombre != None and self.ubicacion != None and self.Periodo != None:
                print("""
El nombre de la empresa: {}\t
Ubicasion de la empresa: {}\t
Periodo del analisis:    {}\t
        """.format(self.nombre, self.ubicacion, self.Periodo))
        else:
            self.nombre = Name 
            self.ubicacion = Ubicasion
            self.Periodo = Periodo
            print("""
El nombre de la empresa: {}\t
Ubicasion de la empresa: {}\t
Periodo del analisis:    {}\t
        """.format(self.nombre, self.ubicacion, self.Periodo))

    #!metodos de Razones Simples
    #? metodos de liquidez

    def AnalisisLiquidez(self,ActivoCirculante = None, PasivoCirculante = None,Inventario = None):
        self.capitalNeto(ActivoCirculante,PasivoCirculante)
        self.razonLiquidez(ActivoCirculante, PasivoCirculante)
        self.pruebaAcido(ActivoCirculante, PasivoCirculante, Inventario)
        pass

    def capitalNeto(self, ActCir, PasCir):
        capitalNeto = ActCir - PasCir
        self.Liquidez['capital neto'] = capitalNeto
        print(capitalNeto)

    def razonLiquidez(self, ActCir, PasCir):
        RazonDeLiquidez = ActCir/PasCir
        self.Liquidez['Razon de liquidez'] = RazonDeLiquidez
        print(RazonDeLiquidez)

    def pruebaAcido(self, ActCir, PasCir,inventario):
        PruebaDeAcido = (ActCir - inventario)/PasCir
        self.Liquidez['Prubea de acido'] = PruebaDeAcido
        if PruebaDeAcido > 1:
            print('esta prueba de acido a sido superada ', PruebaDeAcido)
        else:
            print('la prueba de acido no ha sido superada ', PruebaDeAcido)
        
    def DateLiquidez(self):
        dataLiquidez = self.Liquidez
        series = pd.Series(dataLiquidez)
        return series

    #? metodos de solvencia 

    def AnalisisSolvencia(self, ANTR =None,DT=None,ANRF=None,PF=None,NP=None):
        self.solvenciaTotal(ANTR,DT)
        self.firmeza(ANRF,PF)
        self.independencia(NP,PF)

    def solvenciaTotal(sefl, ANTR, DT):
        solvenciaTotal = ANTR/DT
        sefl.Solvencia['Solvencia total'] = solvenciaTotal
        print('Solvencia total',solvenciaTotal)

    def firmeza(self,ANRF,PF):
        Firmeza = ANRF/PF
        self.Solvencia['Firmeza'] = Firmeza
        print(Firmeza)

    def independencia(self, NP,PF):
        Independencia = NP/PF 
        self.Solvencia['Independencia'] = Independencia
        print(Independencia)
    
    def DateSolvencia(self):
        dataSolvencia = self.Solvencia
        series = pd.Series(dataSolvencia)
        return series

    #?Analisis de la estabilidad 

    def AnalisisEstabilidad(self, ActivoFijo,CapitalContable,CapitalSocial,PasivoTotal):
        self.origenDeCapital(PasivoTotal,CapitalContable)
        self.inversionDeCapital(ActivoFijo,CapitalContable)
        self.valorContableDelCapital(CapitalContable, CapitalSocial)

        
    def origenDeCapital(self, PasivoTotal,CapitalContable):
        OrigenDeCapital = PasivoTotal/CapitalContable
        self.Estabilidad['Origen de capital'] = OrigenDeCapital
        print(OrigenDeCapital)

    def inversionDeCapital(self, ActivoFijo, CapitalContable):
        InversionDeCapital = ActivoFijo/CapitalContable
        self.Estabilidad['Inversion de capital'] = InversionDeCapital
        print(InversionDeCapital)

    def valorContableDelCapital(self, CapitalContable, CapitalSocial):
        ValorContableDelCapital = CapitalContable/CapitalSocial
        self.Estabilidad['Valor contable de capital'] = ValorContableDelCapital
        print(ValorContableDelCapital)

    def DataEstabilidad(self):
        dataOrigenCapital = self.Estabilidad
        series = pd.Series(dataOrigenCapital)
        return series 
    #? Ciclo economico 

    def AnalsisiCicloEconomico(self,utilidadDeEjercicio = None,CapitalSocial = None,PT = None,VentasNetas = None):
        self.utilidadDelEjercicio(utilidadDeEjercicio,CapitalSocial)
        self.estudioUtilidad(utilidadDeEjercicio,CapitalSocial, PT)
        self.margenGanaciaUnidad(utilidadDeEjercicio,VentasNetas)

    def utilidadDelEjercicio(self, utilidadDeEjercicio, CapitalSocial):
        estudioiUtilidad = utilidadDeEjercicio/CapitalSocial
        self.CicloEconomico['Utilidad del ejercicio'] = estudioiUtilidad
        print(estudioiUtilidad)

    def estudioUtilidad(self, utilidadDeEjercicio, CapitalSocial, PT):
        EstudioDeUtilidad = utilidadDeEjercicio / (CapitalSocial + PT)
        self.CicloEconomico['Estudio de la utilidad'] = EstudioDeUtilidad
        print(EstudioDeUtilidad)

    def margenGanaciaUnidad(self, UtilidadDeEjercicio, VentasNetas):
        MargenGanaciaUnidad = UtilidadDeEjercicio / VentasNetas
        self.CicloEconomico['Margen de ganacias por unidad'] = MargenGanaciaUnidad
        print(MargenGanaciaUnidad)

    def DataCicloEconomico(self):
        CicloEconomico = self.CicloEconomico
        series = pd.Series(CicloEconomico)
        return series 



    def razonesSimples(self):
        rS = self.RazonesSimples
        series = pd.Series(rS)
        return series 

    
    
    #!
a = MetodosFinancieros()
# a.capitalNeto(1622119, 240038)
# a.razonLiquidez(1622119, 240038)
# a.pruebaAcido(1622119, 240038 ,950000)

# deudadTotales = 1109500 + 240038 
# a.solvenciaTotal(2417986, deudadTotales)
# a.firmeza(548907,1109500)

a.DateLiquidez
a.DateSolvencia