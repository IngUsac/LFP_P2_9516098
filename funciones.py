import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox


class GramaticaLibredeContexto:
    def __init__(self, nombre, no_terminal, terminal, s_inicial, producciones ):
        self.nombre = nombre
        self.no_terminal = no_terminal
        self.terminal = terminal
        self.s_inicial = s_inicial
        self.producciones = producciones

pila = []
def cargar_archivo_glc(): # Permite cargar N gramaticas libres del contexto

    archivoentrada=filedialog.askopenfilename(initialdir = "/LFP_P2_9516098",title = "Archivo de Entrada",filetypes = (('Archivos de Gramaticas Libres de Contexto', '*.glc'),("Todos los Archivos","*.*")))
    if archivoentrada:
        messagebox.showinfo("Carga de Archivo", " El archivo de entrada se cargó correctamente")

    # Crear una lista vacía para representar la pila
    #pila = []

    #C:\Users\WINDOWS 10\Desktop\Repositorio\LFP\LFP_P2_9516098

    # Leer el archivo de texto línea por línea
    with open(archivoentrada, "r") as archivo:
        # Variables para almacenar los datos de la gramatica actual
        nombre = ""
        no_terminal = ""
        terminal = ""
        s_inicial = ""
        producciones = []

        i=0
        existe = False
    
        for linea in archivo:
            nom = linea.split("\n")
            if pila:
                for gramatica in pila:                                    
                    if gramatica.nombre==nom[0].rstrip("'") :                    
                        messagebox.showinfo("Validacion de Gramatica", " El nombre de la gramatica "+gramatica.nombre+" ya existe, no se cargara")
                        existe=True                    
                        break       
                            
           
            i+=1
            # Verificar si se encontró el símbolo de finalización (%)
         
            if "%" in linea:
                if existe==False:
                # Crear una instancia de GramaticaLibredeContexto y apilarla en la pila
                    gramatica = GramaticaLibredeContexto(nombre, no_terminal, terminal, s_inicial, producciones )
                    pila.append(gramatica)

                # Reiniciar las variables para la próxima gramatica
                nombre = ""
                no_terminal = ""
                terminal = ""
                s_inicial = ""
                producciones = []
            
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
                    producciones.append(datos[0].rstrip("'")) 

        
    # Imprimir las instancias de GramaticaLibredeContexto en la pila
    #for gramatica in pila:
        #print("GLC --> ",gramatica.nombre)
        #print("Producciones --> ",gramatica.producciones)

    # Verificar si la pila está vacía
    if not pila:
        messagebox.showinfo("Validación de Gramática", "La pila está vacía")


  


def informacion_glc(): # Muestra todos los nombres de las gramaticas que se encuentran cargados en el sistema

    def seleccionar_elemento():
        indice = int(entry.get()) - 1
        if 0 <= indice < len(pila):
            glc_seleccionada = pila[indice]
            label_glc1.config(text=f" -Nombre de la Gramatica: {glc_seleccionada.nombre}"+f"  -No Terminales: {glc_seleccionada.no_terminal} "+f"  -Terminales: {glc_seleccionada.terminal} "+f"  -Estado Inicial: {glc_seleccionada.s_inicial} ")
            label_glc1.place(x=150,y=100)
          
          
        
            texto_cuadro.delete("1.0", tk.END)  # Borrar contenido previo del cuadro de texto
            texto_cuadro.insert(tk.END, glc_seleccionada.producciones)  # Insertar el contenido del elemento en el cuadro de texto

        
            

        else:
            messagebox.showinfo("Seleccionar de Gramática", "Numero de Gramatica invalido")
            texto_cuadro.delete("1.0", tk.END)  # Borrar contenido previo del cuadro de texto
          
    
            label_glc1.config(text=" ")
            label_glc1.place(x=150,y=100)

    if not pila:
        messagebox.showinfo("Validación de Gramática", "La pila está vacía")
    else:


    # Crear una nueva ventana
        ventana = tk.Toplevel()
        ventana.title("Gramaticas Válidas")
        ventana.geometry("800x600")

        tk.Label(ventana, text="Listado de Gramaticas disponibles").place(x=25,y=20)

        for i, gramatica in enumerate(pila):
            tk.Label(ventana, text=f"{i+1}: {gramatica.nombre}").place(x=25,y=(40+(20*i)))
            

        entry = tk.Entry(ventana)
        entry.place(x=600,y=20)

        tk.Label(ventana, text=" Ingrese el numero de la Gramatica que desea consultar ").place(x=300,y=20)
        tk.Button(ventana, text=" Consultar ", command=seleccionar_elemento).place(x=600,y=50)     
        tk.Label(ventana, text=" Informacion de la Gramatica: ").place(x=150,y=80)
        label_glc1=tk.Label(ventana, text="")
        label_glc1.place(x=150,y=100)
        tk.Label(ventana, text=" Producciones: ").place(x=150,y=120)
     

        texto_cuadro = tk.Text(ventana, height=20, width=75)
        texto_cuadro.place(x=150,y=150)
       

               # Función para cerrar la ventana
        def cerrar_ventana():
            ventana.destroy()

        # Crear un botón de cierre
        tk.Button(ventana, text=" Cerrar ", command=cerrar_ventana).place(x=675,y=50)
       





"""
        for gramatica in pila:
            print("GLC --> ",gramatica.nombre)
            print("Producciones --> ",gramatica.producciones)

        # Verificar si la pila está vacía



    cadena = ['B::=bBAab']

    # Obtener los valores separados de la cadena
    noTerminal, produce, produccion = cadena[0].partition("::=")
    produce=">"
    # Imprimir los valores extraídos
    print("noTerminal:--> ", noTerminal)
    print("produce:--> ", produce)
    print("produccion:--> ", produccion)
"""


def arbol_derivacion(): # Muestra arbol de derivacion previa solicitud del nombre de la gramatica 
    pass

def cargar_archivo_pila(): #permite cargar N autómatas de pila al sistema
    pass

def informacion_pila():  # Muestra informacion del automata almacenado previamente
    pass

def validar_cadena_pila(): # Valida una cadena con un automata previamente cargado por el usuario
    pass

def ruta_validacion_cadena(): #Muestra las transiciones hechas por una cadena ingresada por el usuario, a un automata previamente cargado
    pass

def recorido_paso_paso(): # Muestra paso a paso el comportamiento del automata al validar una cadena ingresada por el usuario, a un automata previamente cargado
    pass

