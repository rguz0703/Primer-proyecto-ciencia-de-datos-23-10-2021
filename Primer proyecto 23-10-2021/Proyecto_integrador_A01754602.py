# Autor: Raúl Emiliano Guzmán Acevedo
#La finalidad de este programa es un analisis de datos usando archivos csv
#El analisis se hizo con una lista de top canciones en Spotify

#Importando librerias necesarias para leer los archivos y graficar
import csv
import matplotlib.pyplot as plot


#Funcion para graficar bailabilidad de las canciones dependiendo el año que el usuario elija   
def graficar_danceability():
    archivo = open ("retoss.csv") #Abre el archivo csv
    entrada = csv.reader(archivo) #Lee archivos csv
    musica = list(entrada)[1:] #Ignora los titulos del archivo
    
    fecha = input("Teclea el año que quieres ver (2010-2019): ")  #El usuario elije la fecha que desea ver
    ejeX = []   #Canciones
    ejeY = []   #Danceability 
    
    for renglon in musica:
        if (renglon[4].startswith(fecha)):       #Condiciones para solo graficar una fecha en especifico
            ejeX.append(renglon[1])
        if (renglon[4].startswith(fecha)):
            ejeY.append(int(renglon[7]))
            
    plot.bar(ejeX,ejeY)                                #Grafica de barras
    plot.title("Dansabilidad de las canciones")         #Título de la grafica
    plot.xticks(rotation=90)       
    plot.xlabel("Canciones")
    plot.ylabel("Danceability")
    plot.show()


#Funcion para graficar la energia de las canciones
def graficar_energia():
    archivo = open ("retoss.csv") #Abre el archivo csv
    entrada = csv.reader(archivo) #Lee archivos csv
    musica = list(entrada)[1:] #Ignora los titulos
    
    fecha = input("Teclea el año que quieres ver (2010-2019): ")
    ejeX = []  #Canciones
    ejeY = []  #Energia
    
    for renglon in musica:
        if(renglon[4].startswith(fecha)):     #Condiciones para solo graficar una fecha en especifico
            ejeX.append(renglon[1])
        if(renglon[4].startswith(fecha)):
            ejeY.append(renglon[6])
         
    plot.bar(ejeX,ejeY)           #Grafica de barras
    plot.title("Energia de las canciones")
    plot.xticks(rotation=90)
    plot.xlabel("Canciones")
    plot.ylabel("Energia")
    plot.show()
    

#Funcion para graficar las pulsaciones por minuto
def graficar_bpm():
    archivo = open ("retoss.csv") #Abre el archivo csv
    entrada = csv.reader(archivo) #Lee archivos csv
    musica = list(entrada)[1:] #Ignora los titulos
    
    fecha = input("Teclea el año que quieres ver (2010-2019): ")
    ejeX = []    #Canciones
    ejeY = []    #Pulsaciones
    
    for renglon in musica: 
        if(renglon[4].startswith(fecha)):       #Condiciones para solo graficar una fecha en especifico
            ejeX.append(renglon[1])
        if(renglon[4].startswith(fecha)):
            ejeY.append(renglon[5])
         
    plot.bar(ejeX,ejeY)
    plot.title("Pulsaciones por minuto")
    plot.xticks(rotation=90)
    plot.xlabel("Canciones")
    plot.ylabel("BPN")
    plot.show() 
    
    
#Funcion para graficar sonoridad    
def graficar_loudnes():
    archivo = open ("retoss.csv") #Abre el archivo csv
    entrada = csv.reader(archivo) #Lee archivos csv
    musica = list(entrada)[1:] #Ignora los titulos
    
    fecha = input("Teclea el año que quieres ver (2010-2019): ")
    ejeX = []  #Canciones
    ejeY = []  #Sonoridad
    
    for renglon in musica:
        if(renglon[4].startswith(fecha)):       #Condiciones para solo graficar una fecha en especifico
            ejeX.append(renglon[1])
        if(renglon[4].startswith(fecha)):
            ejeY.append(renglon[8])
         
    plot.bar(ejeX,ejeY)
    plot.title("Sonoridad")
    plot.xticks(rotation=90)
    plot.xlabel("Canciones")
    plot.ylabel("Sonoridad")
    plot.show()
    
    
def estadisticas_bailabilidad():
    archivo = open ("retoss.csv") #Abre el archivo csv
    entrada = csv.reader(archivo) #Lee archivos csv
    musica = list(entrada)[1:] #Ignora los titulos
    
    fecha = input("Teclea el año que quieres ver (2010-2019): ")
    ejeX = []  #Canciones
    ejeY = []  #Bailabilidad
    
    for renglon in musica:
        if(renglon[4].startswith(fecha)):       #Condiciones para solo graficar una fecha en especifico
            ejeX.append(renglon[1])
        if(renglon[4].startswith(fecha)):
            ejeY.append(renglon[7])
    
    print("La cancion que menos se puede bailar es: " , min(ejeY))
    print("La cancion que más se puede bailar es: ", max(ejeY))


def estadisticas_energia():
    archivo = open ("retoss.csv") #Abre el archivo csv
    entrada = csv.reader(archivo) #Lee archivos csv
    musica = list(entrada)[1:] #Ignora los titulos
    
    fecha = input("Teclea el año que quieres ver (2010-2019): ")
    ejeX = []  #Canciones
    ejeY = []  #Energia
    
    for renglon in musica:
        if(renglon[4].startswith(fecha)):     #Condiciones para solo graficar una fecha en especifico
            ejeX.append(renglon[1])
        if(renglon[4].startswith(fecha)):
            ejeY.append(renglon[6])
    
    print("La cancion con menos energía es: " , min(ejeY))
    print("La cancion con más energía es: ", max(ejeY))
    
    
def estadisticas_bpn():
    archivo = open ("retoss.csv") #Abre el archivo csv
    entrada = csv.reader(archivo) #Lee archivos csv
    musica = list(entrada)[1:] #Ignora los titulos
    
    fecha = input("Teclea el año que quieres ver (2010-2019): ")
    ejeX = []    #Canciones
    ejeY = []    #Pulsaciones
    
    for renglon in musica: 
        if(renglon[4].startswith(fecha)):       #Condiciones para solo graficar una fecha en especifico
            ejeX.append(renglon[1])
        if(renglon[4].startswith(fecha)):
            ejeY.append(renglon[5])
            
    print("La cancion con menos pulsaciones por minuto es: " , min(ejeY))
    print("La cancion con más pulsaciones por minuto es: ", max(ejeY))
    


def estadisticas_sonoridad():
    archivo = open ("retoss.csv") #Abre el archivo csv
    entrada = csv.reader(archivo) #Lee archivos csv
    musica = list(entrada)[1:] #Ignora los titulos
    
    fecha = input("Teclea el año que quieres ver (2010-2019): ")
    ejeX = []  #Canciones
    ejeY = []  #Sonoridad
    
    for renglon in musica:
        if(renglon[4].startswith(fecha)):       #Condiciones para solo graficar una fecha en especifico
            ejeX.append(renglon[1])
        if(renglon[4].startswith(fecha)):
            ejeY.append(renglon[8])
    
    print("La cancion con menos ruidosa es: " , min(ejeY))
    print("La cancion con más ruidosa es: ", max(ejeY))
    
    
    
#Funcion que crea un menú que el usuario pueda usar para seleccionar las grtaficas   
def menu():
    opcion = int(input("Menu Principal \n"+
                         "1. Gráficas de bailabilidad \n"+
                         "2. Gráficas de energia \n"+
                         "3. Gráficas de pulsaciones por minuto \n"+
                         "4. Gráficas de sonoridad \n"+
                         "5. Estadisticas bailabilidad \n"+
                         "6. Estadisticas energía \n"+
                         "7. Estadisticas pulsaciones por minuto \n"+
                         "8. Estadisticas sonoridad \n"+
                       
                         "9. Finalizar programa: \n"+
                         "Seleccione el numero de la opcion que desea: \n"))
    return(opcion)




def main():
    '''La funcuion main llama a la funcion menu para asi poder desplegar y usar el menu'''
    opcion = 0
    while opcion != 9:
        opcion = menu()
        
        
        if opcion == 1:
            graficar_danceability()
            
        if opcion == 2:
            graficar_energia()
            
        if opcion == 3:
            graficar_bpm()
            
        if opcion == 4:
            graficar_loudnes()
        
        if opcion == 5:
            estadisticas_bailabilidad()
            
        if opcion == 6:
            estadisticas_energia()
        
        if opcion == 7:
            estadisticas_bpn()
        
        if opcion == 8:
            estadisticas_sonoridad()
            
        if opcion == 9:
            print("Programa finalizado")
        
        
        
main()