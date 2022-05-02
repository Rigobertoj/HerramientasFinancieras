import copy as cp
import pandas as pd
import numpy as np
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

    cuentasDeBalance = {
        'ACTIVOS': '-------------',
        'Acitvos Circulantes': None,
        'Activos Fijos': None,
        'Activos Diferidos':None,
        ' ':'',
        'Total de Activos'
        ' ':'',
        'PASIVOS': '-------------',
        'Pasivos Circulantes':None,
        'Pasivos Fijos': None,
        ' ':'',
        'Total de Pasivos':None,
        ' ':'',
        'CAPITAL':'-------------',
        'Capital social': None,
        'Utilidad del ejer':None,
        'Utilidades anteriores':None,
        'Otras Reservas': None,
        ' ':'',
        'Total del capital': None
        
    }
    RazonesSimples = [Solvencia,Liquidez,Estabilidad]

    def __init__(self):
        pass

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
        self.cuentasDeBalance['Acitvos Circulantes'] = ActivoCirculante
        self.cuentasDeBalance['Pasivos Circulantes'] = PasivoCirculante
        
        self.capitalNeto(ActivoCirculante,PasivoCirculante)
        self.razonLiquidez(ActivoCirculante, PasivoCirculante)
        self.pruebaAcido(ActivoCirculante, PasivoCirculante, Inventario)
        pass

    def capitalNeto(self, ActCir, PasCir):
        self.cuentasDeBalance['Acitvos Circulantes'] = ActCir
        self.cuentasDeBalance['Pasivos Circulantes'] = PasCir
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
        series.round(decimals=5)
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
#Terminar la cuentas enlazar las cuentas de balance
    #!
class RazonesEstandar():
    
    def __init__(self) -> None:
        pass
    
    def ECapitalNetoTrabajo(*args):
        pass

class PorcientosIntegrales():
    def __init__(self) -> None:
        pass

class ControlPresupuestario():
    def __init__(self) -> None:
        pass

    def unidadesDeEquilibrio(name,ventasNetas, CostoDeVenta,GastosAdministrativos, listPdeCrecimineto = [], listPdeCostoAdministrativo = [], years = []):
        print("""
estado inicial antes de aplicar crecimiento a la empresa
                        {}
    ventas netas {}
(-)costo de venta {}

(=)utilidad bruta {}
(-)gastos administrativos {}

(=)utilidad neta 0
    """.format(name,ventasNetas, CostoDeVenta, GastosAdministrativos, GastosAdministrativos))
        for index in range(len(years)):
            year = years[index]
            ventasNetas *= listPdeCrecimineto[index]
            CostoDeVenta *= listPdeCrecimineto[index]
        
            utilidadBruta = ventasNetas -CostoDeVenta
            GastosAdministrativos *= listPdeCostoAdministrativo[index]
        
            utilidadNeta = utilidadBruta -GastosAdministrativos
            print("""
estado de resultados del año {}

    ventasNetas => {:10,.2f}
(-) costoDeVenta => {:10,.2f}

(=) utilidad bruta => {:10,.2f}
(-) gastosAdministrativos => {:10,.2f}

(-) utilidad neta => {:10,.2f}
___________________________________________""".format(year,ventasNetas,CostoDeVenta,utilidadBruta,GastosAdministrativos,utilidadNeta)
)