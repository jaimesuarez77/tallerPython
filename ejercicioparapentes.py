edad=0
eps=''
consentimiento="si"
generomasculino="m"
generofemenino="f"

contadorgenerofemino=0
contadorgeneromasculino=0
contadoredad=0

porcentajemujeres=0
porcontajehombres=0
participantes=0
contadorgenero=0

consentimiento=input('este es el consentimiento para poder volar en el parapente')
while (consentimiento=='si'):
    participantes=float(input('nemero de participantes para volar como gallinas'))
    contador=0
    while (contador<participantes):
        edad=float(input('cuantos anos tiene  : '))
        genero=float(input('genero m = masculino f = femenino '))
        eps=input('que eps esta afiliado')
        if (edad>15 and edad<=60):
            contador+=1
            contadoredad+=1
        elif  (genero=="m"):
            contadorgeneromasculino+=1
        elif  (genero=="f"):
            contadorgenerofemino+=1
        print('promedio de mayores  ', contadoredad)
        print('promedio de hombres', contadorgeneromasculino)
        print('promedio de de mujeres  ', contadorgenerofemino)



