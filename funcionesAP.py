import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from generarderivacion import genera_arbol_derivacion

class AutomatasDePila:
    def __init__(self, nombre, alfabeto, simbolos, s_inicial, aceptacion, transiciones ):
        self.nombre = nombre
        self.alfabeto = alfabeto
        self.simbolos = simbolos
        self.s_inicial = s_inicial
        self.aceptacion = aceptacion
        self.transiciones = transiciones

Apila = []
archivoentrada=""
def cargar_archivo_pila(): # Permite cargar N Automatas de Pila

    archivoentrada=filedialog.askopenfilename(initialdir = "/LFP_P2_9516098",title = "Archivo de Entrada",filetypes = (('Archivos de Automatas de Pila ', '*.ap'),("Todos los Archivos","*.*")))
    if archivoentrada:
        carga=True
        
    # Leer el archivo de texto línea por línea
    with open(archivoentrada, "r") as archivo:
        # Variables para almacenar los datos de la AP actual
        nombre = ""
        alfabeto = ""
        simbolos = ""
        s_inicial = ""
        aceptacion = ""
        transiciones = []
    

        i=0
        existe = False
    
        for linea in archivo:
            nom = linea.split("\n")
            if Apila:
                for AP in Apila:                                    
                    if AP.nombre==nom[0].rstrip("'") :                    
                        messagebox.showinfo("Validacion de Automata de Pila", " El nombre de la AP "+AP.nombre+" ya existe, no se cargara")
                        existe=True                    
                        break       
                            
           
            i+=1
            # Verificar si se encontró el símbolo de finalización (%)
         
            if "%" in linea:
                if existe==False:
                # Crear una instancia de GramaticaLibredeContexto y apilarla en la pila
                    AP = AutomatasDePila(nombre,alfabeto,simbolos,s_inicial,aceptacion,transiciones)
                    Apila.append(AP)

                # Reiniciar las variables para la próxima gramatica
                nombre = ""
                alfabeto = ""
                simbolos = ""
                s_inicial = ""
                aceptacion = ""
                transiciones = []
            
                i=0
                existe = False
                         
            else:
                # Leer los datos de la línea y asignarlos a las variables correspondientes
                datos = linea.split("\n")
                if i ==1 and existe==False:    # para separar el nombre del archivo de entrada y guardarlo en la pila
                    nombre = datos[0].rstrip("'")
                                         

                if i ==2 and existe==False: # para separar el no_terminal del archivo de entrada y guardarlo en la pila
                    no_terminal = datos[0].rstrip("'")
                    

                if i ==3 and existe==False: # para separar el terminal del archivo de entrada y guardarlo en la pila
                    terminal = datos[0].rstrip("'")
                    

                if i ==4 and existe==False: # para separar el s_inicial del archivo de entrada y guardarlo en la pila
                    s_inicial  = datos[0].rstrip("'")
                    

                if i > 4 and existe==False: # para separar las n producciones del archivo de entrada y guardarlo en la pila
                        # Guardar las producciones
                    transiciones.append(datos[0].rstrip("'")) 
    if carga:
        messagebox.showinfo("Carga de Archivo", " El archivo de entrada se cargó correctamente")            

    if not Apila:
        messagebox.showinfo("Validación de AP", "La pila está vacía")


    
def informacion_pila():
    pass
def validar_cadena_pila():
    pass
def ruta_validacion_cadena():
    pass
def recorido_paso_paso():
    pass
 

"""
Cargar archivo
Mostrar información del autómata
Validar cadena
Ruta de validación
Recorrido paso a paso

""" 