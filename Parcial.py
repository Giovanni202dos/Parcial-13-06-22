
from jurassic_park import dinosaurs
from lista import Lista
from cola import Cola

class Dinosaurios:

    def __init__(self, name, type, number,period, named_by):
        self.name = name
        self.type = type
        self.number = number
        self.period = period
        self.named_by = named_by
    
    def __str__(self):
        return f"{self.name},{self.type},{self.number},{self.period}, {self.named_by}"

class Alertt:

    def __init__(self, time, zone_code, dino_number,alert_level, nombre_dino=None):
        self.time = time
        self.zone_code = zone_code
        self.dino_number = dino_number
        self.alert_level = alert_level
        self.nombre_dino = nombre_dino
    
    def __str__(self):
        return f"{self.time},{self.zone_code},{self.dino_number},{self.alert_level},{self.nombre_dino}"

lista_de_alertas_por_fecha=Lista()
lista_de_alertas_nombre_de_dino= Lista()
monitor_de_informes= Lista()

file=open('alerts.txt')
lineas=file.readlines()

#funcion
def tomar_nombre_segun_numero(num):
    i=0
    while i<len(dinosaurs):
        k=dinosaurs[i].get('number')
        if k==num:
            dato=dinosaurs[i]
            nombre=dato.get('name')
            return nombre
        else:
            #print('no')
            i+=1
#CARGO 
lineas.pop(0)   #le quito la cabezera q solo mostrabrab como estaba organizado el archivo
for i in lineas:
    dato=i.split(';')                       #tengo el vector creado con las separcaion de ";"
    nombre=tomar_nombre_segun_numero(int(dato[2]))
    #print(dato)
    #dato.pop(-1)
    k=dato[3][0:-1]
    lista_de_alertas_por_fecha.insertar(Alertt(dato[0],dato[1],dato[2],k,nombre),'time')

i=0
for i in lineas:
    dato=i.split(';')
    nombre=tomar_nombre_segun_numero(int(dato[2]))
    k=dato[3][0:-1]
    #print('nnnnnnn',nombre)
    lista_de_alertas_nombre_de_dino.insertar(Alertt(dato[0],dato[1],int(dato[2]),k,nombre),'nombre_dino') 


#le cargo los datos a los dinosaurios y los agrego a la lista
for i in dinosaurs:
    monitor_de_informes.insertar(Dinosaurios(i['name'],i['type'],i['number'],i['period'],i['named_by'].split(',')),'name')

#monitor_de_informes.barrido()

#funcion para mostrar el ultimo dinosaruiroi en ser descubierto y quien lo hizo
def mostrar_los_ultimo_dino_descubierto_y_quien_lo_hizo(lista):
    i=0
    anio_reciente=0
    while i<lista.tamanio():
        dato=lista.obtener_elemento(i)
        if int(dato.named_by[1])>anio_reciente: 
            anio_reciente= int(dato.named_by[1])
            ultimo_dino_descu=dato       
        i+=1    #aca si aumento i para q apunte al otro dato
    print(' el ultimo dino descubierto fue: ',ultimo_dino_descu.name)
    print('fue descubierto por: ',ultimo_dino_descu.named_by[0])

  
#-------------------------------
print()
print('mostrar el ultimo dino descubierto')
mostrar_los_ultimo_dino_descubierto_y_quien_lo_hizo(monitor_de_informes)
#-------------------------------

#-----------------------------
#ARCHIVO DE ALERTAS
#lista ordenada por fecha
print('lista  de alertas ordenada por fecha')
lista_de_alertas_por_fecha.barrido()

#lista ordenada por NOMBRE de dino
print()
print('lista de alertas ordenada por NOMBRE de dino')
lista_de_alertas_nombre_de_dino.barrido()
#----------------------------

#-----------------------------
#Elimino las zonas indicadas
print()
print('Elimino las zonas indicadas')
lista_de_alertas_nombre_de_dino.eliminar('WYG075','zone_code')
lista_de_alertas_nombre_de_dino.eliminar('SXH966','zone_code')
lista_de_alertas_nombre_de_dino.eliminar('LYF010','zone_code')

lista_de_alertas_por_fecha.eliminar('WYG075','zone_code')
lista_de_alertas_por_fecha.eliminar('SXH966','zone_code')
lista_de_alertas_por_fecha.eliminar('LYF010','zone_code')


#modifico el nombre de dino de la zona de la lista de lista_de_alertas_nombre_de_dino
print('modifico el nombre de dino de la zona de la lista de lista_de_alertas_nombre_de_dino')
dato=lista_de_alertas_nombre_de_dino.busqueda('HYD195','zone_code')
dato.info.nombre_dino='Mosasaurus.'
lista_de_alertas_nombre_de_dino.barrido()
#--------------------------------

#-----------------------------
#listado de dinosurios con cierto level de alerta
print()
print('listado de dinosurios con cierto level de alerta')
listado_de_emergencias=Lista()
i=0
dic=('Tyrannosaurus Rex', 'Spinosaurus', 'Giganotosaurus')
level=('critical','high')
while i<lista_de_alertas_nombre_de_dino.tamanio():
    dato=lista_de_alertas_nombre_de_dino.obtener_elemento(i)

    if dato.nombre_dino in dic:
        if dato.alert_level in level:
            listado_de_emergencias.insertar(dato,'alert_level')
    i+=1
listado_de_emergencias.barrido()
#-----------------------------
#mostrar cola
def mostrar_cola(cola):
    for i in range(0,cola.tamanio()):
        print(cola.mover_al_final())


#----------------------------
cola_de_alertas=Cola()
cola_de_dino_carnivoros=Cola()
cola_de_dino_herbivoros= Cola()
i=0
level_no_gargar=('low','medium')
while i<lista_de_alertas_nombre_de_dino.tamanio():  #cargo las alertas importante
    dato=lista_de_alertas_nombre_de_dino.obtener_elemento(i)
    #print(dato.alert_level)
    if not dato.alert_level in level_no_gargar:
        cola_de_alertas.arribo(dato)
    i+=1
#print(cola_de_alertas.tamanio())
#mostrar_cola(cola_de_alertas)

vec_carnivoros=[]   #les voy a guardar los numeros de los dino carnivoros o herbivoros
vec_herbivoros=[]
i=0
while i<monitor_de_informes.tamanio():
    dato=monitor_de_informes.obtener_elemento(i)
    if dato.type[0:-1] =='carnívoro':
        vec_carnivoros.append(int(dato.number))
    else:
        vec_herbivoros.append(int(dato.number))
    i+=1

i=0

for i in range(0,cola_de_alertas.tamanio()):
    dato=cola_de_alertas.atencion()
    if int(dato.dino_number) in vec_carnivoros:
        cola_de_dino_carnivoros.arribo(dato)
    else:
        cola_de_dino_herbivoros.arribo(dato)
print()
#colas de dino herbivoros y carnivors con cierto level de alerta
print('colas de carnivoros con determinadas alertas')
mostrar_cola(cola_de_dino_carnivoros)
print()
print('colas de herbivoros con determinadas alertas')
mostrar_cola(cola_de_dino_herbivoros)
#---------------------------------------
print()
print('atencion de las alertas de la cola de carnivoros y no mostrar EPC944')
i=0
for i in range(0,cola_de_dino_carnivoros.tamanio()):
    dato=cola_de_dino_carnivoros.atencion()
    if dato.zone_code!='EPC944':
        print(dato)
#-----------------------------------------                                              

#-----------------------------------------
listado_de_dino_a_pedido_del_cliente=Lista()
print()
#funcion para buscar dino x
def buscar_dino(lista,dino):
    i=0
    while i<lista.tamanio():
        dato=lista.obtener_elemento(i)
        if dino in dato.name:
            return dato
        i+=1
#guardamos info de  dino x a pedido del cliente
print('guardamos info de  dino x a pedido del cliente')
dato=buscar_dino(monitor_de_informes,'Raptors')
if dato!=None:
    listado_de_dino_a_pedido_del_cliente.insertar(dato,'name')
else:
    print('dino no encontrado')

dato=buscar_dino(monitor_de_informes,'Carnotaurus')
if dato!=None:
    listado_de_dino_a_pedido_del_cliente.insertar(dato,'name')
else:
    print('dino no encontrado')

listado_de_dino_a_pedido_del_cliente.barrido()
print()
#----
#guardar las zonas donde se pueden encontrar un dino x
print('guardar las zonas donde se pueden encontrar un dino x')
lista_de_las_zonas_de_dino_x=Lista()
def barrido_buscar_y_guardar_las_zonas_de_dino_x(lista,dino,lista_a_guardar):
    i=0
    while i<lista.tamanio():
        dato=lista.obtener_elemento(i)
        if dino in dato.nombre_dino:
            zonas=dato.zone_code
            lista_a_guardar.insertar(zonas)
        i+=1
    if lista_a_guardar.tamanio()==0:
        print('dino no existe')
barrido_buscar_y_guardar_las_zonas_de_dino_x(lista_de_alertas_por_fecha,'Compsognathus',lista_de_las_zonas_de_dino_x)
lista_de_las_zonas_de_dino_x.barrido()
#-----------------------------------------

