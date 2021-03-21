capurgana=1500000
nuqui=1200000
islamargarita=200
islagalapagos=400
mukura=1200000
islasanandres=1500000
# tasa
tasacapurgana=0.15
tasanuqui=0.09
tasamargarita=.016
tasagalapagos=0.08
tasamukura=0.09
tasasanandres=0.12
# impuestos
impuestoscapurgana=0.2
impuestosnuqui=0.19
impuestosmargarita=0.11
impuestosgalapagos=0.09
impuestosmukura=0.11
impuestossanandres=0.13
pasajeros=0
tarifatotal=0
contador=0
viajes=0

breakcentinela=input('desea salir de vaciones con covid-19 incluido si o no?  ')
while (breakcentinela=='si'):
    pasajeros=float(input('numero de pasajeros que desean viajar   '))  
    contador=0
    while (contador<pasajeros):

        print('eliga un numero para su destino ')
        print('"1" = capurgana ')
        print('"2" = nuqui  ')
        print('"3" = isla margarita  ')
        print('"4" = isla galapago  ')
        print('"5" = isla mukura  ')
        print('"6" = isla san andres  ')

        viajes=0
        viajes=float(input('eliga un numero para su destino\n'))  

        if (pasajeros==1):
            contador+=1
            pasajeros+=1
        elif (pasajeros==2):
            contador+1
            pasajeros+=1
        elif (pasajeros==3):
            contador+1
            pasajeros+=1
        elif (pasajeros==4):
            contador+1
            pasajeros+=1
        elif (pasajeros==5):
            contador+1
            pasajeros+=1
        elif (pasajeros==6):
            contador+1
            pasajeros+=1
            print('valor de la tarifa   ',tarifatotal,'\n')
            print('total de pasajeros  ',pasajeros,'\n')
    tarifatotal=contador+pasajeros+viajes
print('valor de la tarifa   ',tarifatotal,'\n')
print('total de pasajeros  ',pasajeros,'\n')


       
    


