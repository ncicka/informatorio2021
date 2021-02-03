#Hola Magui, aqui estoy agregando codigo a tu programa
#lo modifico espero aceptes mi modificacion


#aui Magui  Brollo
from datetime import datetime, date, time, timedelta
FormatoFechaHora= "%d-%m-%Y %H:%M"

# el tipo de la pizza(a la piedra, a la parrilla, de molde)
class TipoPizza:
    def __init__(self, xCodTipo,xNombreTipo):
        self.codigoTipo = xCodTipo
        self.nombreTipo = xNombreTipo
    
    def __str__(self):
        return f'CodTipo: {self.codigoTipo} - NombreTipo: {self.nombreTipo}'


# tamaños (8, 10 y 12 porciones)
class TamaniosPizza:
    def __init__(self, xCodTamanio,xNombreTamanio, xPorciones):
        self.codigoTamanio = xCodTamanio
        self.nombreTamanio = xNombreTamanio
        self.porciones = xPorciones

    def __str__(self):
        return f'Cod: {self.codigoTamanio} - Nombre: {self.nombreTamanio} - {self.porciones} porciones'

# Variedades
# 'Napolitana',["salsa tomate", "mozzarella", "anchoas", "orégano", "alcaparras", "aceite oliva"]
class VariedadPizza:
    def __init__(self, xCodVariedad,xNombreVariedad, xListaIngredientes):
        self.codigoVariedad = xCodVariedad
        self.nombreVariedad = xNombreVariedad
        self.listaIngredientes = xListaIngredientes

    def __str__(self):
        return f'Cod: {self.codigoVariedad} - {self.nombreVariedad} - {self.listaIngredientes}'



class Pizza:
    def __init__(self,xCodPizza, xVariedad, xTipo, xTamanio, xPrecio):
        self.codigPizza = xCodPizza
        self.variedadPizza = xVariedad
        self.tipoPizza = xTipo
        self.porciones = xTamanio
        self.precioPizza = xPrecio

    def __str__(self):
        return f'{self.codigPizza} - {self.variedadPizza.nombreVariedad.upper()}  - {self.tipoPizza.nombreTipo.upper()}, \
    de {self.porciones.porciones} porciones, ${self.precioPizza}.'



# Pedido, para instanciar UN pedido. Cada instacia de Pedido, se guardará en "LIstaPedido"
class Pedido:
    numPedido = 0
    def __init__(self, xCliente, xFechaHoraPedido, xDemora, xListaDetallePedido):
        Pedido.numPedido += 1
        self.numPedido = Pedido.numPedido
        self.cliente = xCliente
        self.fechaHoraPedido = xFechaHoraPedido.strftime(FormatoFechaHora)
        self.demoraMinutos = xDemora
        self.fechaHoraEntrega = (xFechaHoraPedido + timedelta(minutes=xDemora)).strftime(FormatoFechaHora)
        self.listaDetallePedidos = xListaDetallePedido
        self.totalPagar = 0               # se calcula en base a el "Detalle Pedido"
        self.estado = False
        
    def __str__(self):
        return f'{self.numPedido} - {self.cliente.upper()} | Pidió: {self.fechaHoraPedido} | Retira: {self.fechaHoraEntrega.strftime(FormatoFechaHora)} | ${self.totalPagar}' 
 


class DetallePedido:
    def __init__(self, xCantidadPizza, xPizza):
        #self.numPedido = ?? DEBERIA TENER
        self.cantidadPizza = xCantidadPizza
        self.pizza = xPizza    #es el OBJ pizza
        self.precioPizza = self.pizza.precioPizza  #del OBJ pizza obtengo el Precio Unitario
    
    def __str__(self):
        return f'{self.cantidadPizza} - {self.pizza.variedadPizza.nombreVariedad}-  {self.pizza.tipoPizza.nombreTipo} - ${self.precioPizza}'




# La Pizzeria, administra Lista menu, los Pedidos
class Pizzeria:
    def __init__(self, xNombrePizzeria):
        self.nombrePizzeria = xNombrePizzeria
        self.listaMenuPizzas = list()  ## es una LISTA
        self.listaPedidos = list()

    def agregarMenuPizza(self, xPizza):
        self.listaMenuPizzas.append(xPizza)
    
    def mostrarMenuPizza(self):
        print('\nListado de Pizzas en el Menú: ')
        for xMen in self.listaMenuPizzas:
            print(xMen)


    def agregarPedido(self, xPedido):
        self.listaPedidos.append(xPedido)

    def mostrarPedidos(self):
        print('\nLista de Pedidos de Pizzas: ')
        for xPed in self.listaPedidos:
            totalPagar=0
            print(f'{xPed.numPedido} {xPed.cliente.upper()} | Pidió: {xPed.fechaHoraPedido} | Retira: {xPed.fechaHoraEntrega} | ${xPed.totalPagar}')
            for xDet in xPed.listaDetallePedidos:
                print ('    ', xDet)
                totalPagar += (xDet.cantidadPizza * xDet.precioPizza)
            print(' TOTAL A PAGAR : $', totalPagar)
            print('\n')
       
    def variedadMasPedida(self):
        dic_Variedad=dict()
        for xPed in self.listaPedidos:
            for xDet in xPed.listaDetallePedidos:
                if dic_Variedad.get(xDet.pizza.variedadPizza.nombreVariedad,'no') == 'no':                # sino esta
                    dic_Variedad[xDet.pizza.variedadPizza.nombreVariedad] = xDet.cantidadPizza    #se agrega al diccionario, con la cantidad
                else:
                    dic_Variedad[xDet.pizza.variedadPizza.nombreVariedad] += xDet.cantidadPizza
        
        # hay que importar operator para utilizar y ordenar por una clave o valor
        #d_ordenado = sorted(d.items(), key=operator.itemgetter(1), reverse=True) tambien se puede utilizar la funcion lambda
        dic_ordenado = sorted(dic_Variedad.items(), key=lambda x: x[1], reverse=True)
        return dict(dic_ordenado)


    def tipoMasPedido(self):
        dic=dict()
        for xPed in self.listaPedidos:
            for xDet in xPed.listaDetallePedidos:
                if dic.get(xDet.pizza.tipoPizza.nombreTipo,'no') == 'no':                # sino esta
                    dic[xDet.pizza.tipoPizza.nombreTipo] = xDet.cantidadPizza    #se agrega al diccionario, con la cantidad
                else:
                    dic[xDet.pizza.tipoPizza.nombreTipo] += xDet.cantidadPizza
        
        dic_ordenado = sorted(dic.items(), key=lambda x: x[1], reverse=True)
        return dict(dic_ordenado)


    def racaudacion(self):
        totalPagar=0
        for xPed in self.listaPedidos:
            for xDet in xPed.listaDetallePedidos:
                totalPagar += (xDet.cantidadPizza * xDet.precioPizza)
        return totalPagar
        

    def canti_Monto(self):
        listaCanti_Monto=list()
        for xPed in self.listaPedidos:
            for xDet in xPed.listaDetallePedidos:
                rec = xDet.precioPizza * xDet.cantidadPizza
                clave= xDet.pizza.variedadPizza.nombreVariedad+'- '+xDet.pizza.tipoPizza.nombreTipo
                listaCanti_Monto.append( [clave, xDet.precioPizza, xDet.cantidadPizza, rec] )
        return listaCanti_Monto

    
    

#-----------prog principal ----------------------------------

palmita1= Pizzeria('Palmita')

# el tipo de la pizza(a la piedra, a la parrilla, de molde)
tipo1=TipoPizza('PD','Piedra')
tipo2=TipoPizza('PR','Parrilla')
tipo3=TipoPizza('ML','Molde')

# tamaños (8, 10 y 12 porciones)
tam1=TamaniosPizza('CH','Chica',8)
tam2=TamaniosPizza('ME','Mediana',10)
tam3=TamaniosPizza('GR','Grande',12)

# Variedades
var1=VariedadPizza('NP','Napolitana',["salsa tomate", "mozzarella", "anchoas", "orégano", "alcaparras", "aceite oliva"])
var2=VariedadPizza('MR','Margarita', ["salsa de tomate", "mozzarella", "albahaca", "orégano", "aceite de oliva"])
var3=VariedadPizza('MZ', 'Muzzarela',[ "salsa de tomate", "mozzarella", "orégano"])

#Pizzas, que se agregaran al Menu de  Pizzeria
pizza1=Pizza(1,var1,tipo1,tam1, 100)
pizza2=Pizza(2,var2,tipo2,tam2, 200)
pizza3=Pizza(3,var3,tipo3,tam3, 300)

palmita1.agregarMenuPizza(pizza1)
palmita1.agregarMenuPizza(pizza2)
palmita1.agregarMenuPizza(pizza3)

palmita1.mostrarMenuPizza()


# El "Pedido" contiene los datos de Encabezado. Luego tiene una LISTA con los detalles del Pedido 
#Luego "DdetallePedido"  es la lista de los detalles, que se crean junto al pedido.
hoy=datetime.now()  #toma la fecha-hora del sitema (sería el momento en que se registró el pedido)

#PEDIDO= cliente, hoy-hora, demora en minutos, ListaDetallePedido
                                #se crean los OBJ "DetallePedido"  junto al "Pedido"
ped1=Pedido('Magui ', hoy, 10, [DetallePedido(1,pizza1), DetallePedido(1,pizza2) ])
ped2=Pedido('Miguel', hoy, 15, [DetallePedido(2,pizza2)])                            
ped3=Pedido('Liliana', hoy, 20,[DetallePedido(1,pizza1),DetallePedido(1,pizza2),DetallePedido(1,pizza3)])

palmita1.agregarPedido(ped1)
palmita1.agregarPedido(ped2)
palmita1.agregarPedido(ped3)

palmita1.mostrarPedidos()


#	Variedades y tipos de pizzas más pedidas por los clientes. 
dic=palmita1.variedadMasPedida()
print('\n--------------------------')
print('VARIEDADES MAS PEDIDAS')
print('--------------------------')
print('Variedad       Cantidad')
print('--------------------------')
for k,v in dic.items():
    print(k.ljust(15),'    ' , v)
print('--------------------------')


dic=palmita1.tipoMasPedido()
print('\n--------------------------')
print('TIPO     MAS   PEDIDOS')
print('--------------------------')
print('Tipos           Cantidad')
print('--------------------------')
for k,v in dic.items():
    print(k.ljust(15),'    ' , v)
print('-'*30)


#	Ingresos (recaudaciones) por períodos de tiempo. 
rec=palmita1.racaudacion()
print('\n--------------------------')
print(f'RECAUDACIÓN: ${rec}')
print('--------------------------')


#	Pedidos (cantidad y monto) por períodos de tiempo. 
lista_Cant_Monto=palmita1.canti_Monto()
print('\n--------------------------')
print('PEDIDOS (CANTIDAD Y MONTO):' )
print('--------------------------')
for k in lista_Cant_Monto:
    print(f' {k[0].ljust(25)} -   ${k[1]} * {k[2]} = {k[3]} ')
    

print('\n')
