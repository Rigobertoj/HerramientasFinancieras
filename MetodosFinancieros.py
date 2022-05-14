import pandas as pd
import numpy as np
class RazonesSimples():
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
        ' ':' ',
        'Total de Activos'
        ' ':' ',
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

    equilibrio = {
        'Costo Fijo': None,
        'Precio de venta': None,
        'Coste Variable': None,
    }
    def __init__(self) -> None:
        pass
    def unidadesDeequilibrio(self,gastosFijos, PresioDeVenta, CostoDeVenta):
        Q = gastosFijos / (PresioDeVenta - CostoDeVenta)
        return Q

    def PuntoDeEquilibrio(self, CostoFijo, PrecioDeVenta, CostoVariable):
        NQ = CostoFijo/ (PrecioDeVenta - CostoVariable)
        VentasNetas = NQ * PrecioDeVenta
        CostoDeVenta = NQ * CostoVariable
        utilidadBruta = VentasNetas - CostoDeVenta
        utiliadNeta = utilidadBruta - CostoFijo
        self.equilibrio['Costo Fijo'] = CostoFijo
        self.equilibrio['Precio de venta'] = PrecioDeVenta
        self.equilibrio['Coste Variable'] = CostoVariable
        return print("""
unidades de equilibrio  {:3,.2f}
gi
\t\t Estado de resultados 

Ventas Netas        \t{:10,.4f}
Costo de venta      \t{:10,.4f}

Utilidad Bruta         \t{:10,.4f}
Gastos administrativos  {:6,.4f} 

UtilidadNeta => {}
        """.format(NQ, VentasNetas, CostoDeVenta, utilidadBruta, CostoFijo, utiliadNeta))

#metodo el cual nos permite recibir varios argumentos que nos permitan optener un pequeño estado de resultados donde nos devuelva el crecimineto de la empresa en uns años posteriores
    def creciminetoEmpresarialEsperado(self, name,ventasNetas, CostoDeVenta,GastosAdministrativos, listPdeCrecimineto = [], listPdeCostoAdministrativo = [], years = []):
        print("""
estado inicial antes de aplicar crecimiento a la empresa
                        {}
    ventas netas {:10,.2f}
(-)costo de venta {:10,.2f}

(=)utilidad bruta {:10,.2f}
(-)gastos administrativos {:10,.2f}

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
___________________________________________""".format(year,ventasNetas,CostoDeVenta,utilidadBruta,GastosAdministrativos,utilidadNeta))
# funcion for examen de resultados
    def volumenDeVentas1(self, ventas,costoDeVenta,gastosFijos):
        utilidad_Bruta = ventas - costoDeVenta
        
        CV = utilidad_Bruta/ventas
        y = gastosFijos/CV
        MC = (1 - CV)
        z = y * (1 - CV)
        utilidad_Bruta = y - z
        utilidad_neta = utilidad_Bruta - gastosFijos
    
        return print(f"""
__________________________________________________________
utilidad bruta {utilidad_Bruta:10,.2f}/ Ventas {ventas:10,.2f} = CV {CV:1,.6f}
gastos fijos {gastosFijos:10,.2f} /{CV:1,.6f} CV = {y:10,.2f}(ventas)
(ventas) {y:10,.2f} X {MC:1,.6f} MC = {z:1,.2f}

( )ventas {y:10,.2f}
(-)Costo Variable {z:10,.2f}

(=)utilidad bruta {utilidad_Bruta:10,.2f}
(-)Gastos Fijos {gastosFijos:10,.2f}

(=)utilidad Neta {utilidad_neta}
""")


    def EspeculatorioVolumenDeVentas( self,precioDeVenta, costoVariable, ventas = [],costoDeVenta = [],gastosFijos = [],):
        for i in range(len(ventas)):
    
            utilidadBruta = ventas[i] - costoDeVenta[i]
            
            CV = utilidadBruta/ventas[i]
            y= gastosFijos[i]/CV
            MC = (1 - CV)
            z = y * MC
            utilidad_Bruta = y - z
            utilidad_neta = utilidad_Bruta - gastosFijos[i]
            Gf = gastosFijos[i]
            # costo_variable = y * MC
            # print("x => ",X, "y => ",y ,"z => ",z)
            Q = self.unidadesDe_equilibrio(Gf,precioDeVenta,costoVariable)
            return print(f"""
___________________________________________________________
utilidad bruta {utilidadBruta:10,.2f}/ Ventas {ventas[i]:10,.2f} = CV {CV:1,.6f}
gastos fijos {gastosFijos[i]:10,.2f} /{CV:1,.6f} CV = {y:10,.2f}(ventas)
(ventas) {y:10,.2f} X {MC:1,.6f} MC = {z:1,.2f}

( )ventas {y:10,.2f}
(-)Costo Variable {z:10,.2f}

(=)utilidad bruta {utilidad_Bruta:10,.2f}
(-)Gastos Fijos {gastosFijos[i]:10,.2f}

(=)utilidad Neta {utilidad_neta}

unidades de equilibrio = Gf {Gf:10,.2f} / (Pv {precioDeVenta:5,.2f} - Cv{costoVariable:5,.2f}) = Q {Q:5,.2f}""")

class MetodosFinancieros():
    def __init__(self) -> None:
        pass



# collanaVolumenDeVentas = ControlPresupuestario()
# collanaVolumenDeVentas.volumenDeVentas2(30000,15003.4,[400000,800000,900000],[200000,400000,450000],[75000,200000,250000])
dreams = ControlPresupuestario()
# dreams.volumenDeVentas2(35,26,[933332,1866664,2099997],[693332,1386664, 1559997],[ 90000,240000,300000])

dreams.volumenDeVentas1(933332,693332,90000)