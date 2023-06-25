import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from generarderivacion import genera_arbol_derivacion

class GramaticaLibredeContexto:
    def __init__(self, nombre, no_terminal, terminal, s_inicial, producciones ):
        self.nombre = nombre
        self.no_terminal = no_terminal
        self.terminal = terminal
        self.s_inicial = s_inicial
        self.producciones = producciones

pila = []
archivoentrada=""
def cargar_archivo_glc(): # Permite cargar N gramaticas libres del contexto

    archivoentrada=filedialog.askopenfilename(initialdir = "/LFP_P2_9516098",title = "Archivo de Entrada",filetypes = (('Archivos de Gramaticas Libres de Contexto', '*.glc'),("Todos los Archivos","*.*")))
    if archivoentrada:
        carga=True
        
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
    if carga:
        messagebox.showinfo("Carga de Archivo", " El archivo de entrada se cargó correctamente")            

    if not pila:
        messagebox.showinfo("Validación de Gramática", "La pila está vacía")

 
def informacion_glc(): # Muestra todos los nombres de las gramaticas que se encuentran cargados en el sistema

    def seleccionar_elemento():
        indice = int(entry.get()) - 1
        if 0 <= indice < len(pila):
            glc_seleccionada = pila[indice]
            label_glc1.config(text=f" -Nombre: {glc_seleccionada.nombre}"+f"  -No Terminales: {glc_seleccionada.no_terminal} "+f"  -Terminales: {glc_seleccionada.terminal} "+f"  -Estado Inicial: {glc_seleccionada.s_inicial} ")
            label_glc1.place(x=150,y=100)
          
          
            tk.Label(ventana, text=" Producciones: ").place(x=150,y=120)
            texto_cuadro.delete("1.0", tk.END)  # Borrar contenido previo del cuadro de texto
            estado_anterior = ""
            for cadena in glc_seleccionada.producciones:
                noTerminal, produce, produccion = cadena.partition("::=")
                if noTerminal == estado_anterior:
                    noTerminal = "  "
                    produce ="|"
                    texto_cuadro.insert(tk.END, "\n"+noTerminal+" "+produce+" "+produccion)  # Insertar el contenido del elemento en el cuadro de texto
                else:
                    # Obtener los valores separados de la cadena                   
                    produce=">"
                    # Imprimir los valores extraídos
                    texto_cuadro.insert(tk.END, "\n"+noTerminal+" "+produce+" "+produccion)  # Insertar el contenido del elemento en el cuadro de texto
                    estado_anterior = noTerminal 

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
        
     

        texto_cuadro = tk.Text(ventana, height=20, width=75)
        texto_cuadro.place(x=150,y=150)
       

               # Función para cerrar la ventana
        def cerrar_ventana():
            ventana.destroy()

        # Crear un botón de cierre
        tk.Button(ventana, text=" Cerrar ", command=cerrar_ventana).place(x=675,y=50)


def arbol_derivacion(): # Muestra arbol de derivacion previa solicitud del nombre de la gramatica 
    def seleccionar_elemento():
        indice = int(entry.get()) - 1
        if 0 <= indice < len(pila):
            glc_seleccionada = pila[indice]
            label_glc1.config(text=f"-Nombre: {glc_seleccionada.nombre}"+f"  -No Terminales: {glc_seleccionada.no_terminal} "+f"  -Terminales: {glc_seleccionada.terminal} "+f"  -Estado Inicial: {glc_seleccionada.s_inicial} ")
            label_glc1.place(x=160,y=100)
          
            label_glc2.config(text=f"Producciones:  {glc_seleccionada.producciones}")
            label_glc2.place(x=160,y=120)
            
            #----------------------------------------------------------------
            # llamar funcion para crear arbol de derivacion
           
            genera_arbol_derivacion(glc_seleccionada.nombre,glc_seleccionada.no_terminal,glc_seleccionada.terminal,glc_seleccionada.s_inicial, glc_seleccionada.producciones)

            #----------------------------------------------------------------    

        else:
            messagebox.showinfo("Seleccionar de Gramática", "Numero de Gramatica invalido")
            
            label_glc1.config(text="") # limpia info de la gramatica
            label_glc1.place(x=160,y=100)
            label_glc2.config(text="")  # limpia producciones
            label_glc2.place(x=160,y=120)
          

    if not pila:
        messagebox.showinfo("Arbol de validación", "La pila está vacía")
    else:


    # Crear una nueva ventana para ver las gramaticas disponibles
        ventana = tk.Toplevel()
        ventana.title("Arbol de derivación")
        ventana.geometry("800x300")

        tk.Label(ventana, text="Listado de Gramaticas disponibles").place(x=25,y=30)
        for i, gramatica in enumerate(pila):
            tk.Label(ventana, text=f"{i+1}: {gramatica.nombre}").place(x=25,y=(60+(20*i)))  # para sacar el listado de gramaticas
       

        entry = tk.Entry(ventana)
        entry.place(x=600,y=30)

        tk.Label(ventana, text=" Ingrese el numero de la Gramatica para desplegar el arbol  ").place(x=250,y=30)  # Solicitar numero de gramatica a consultar
        tk.Button(ventana, text=" Consultar GLC y ver Arbol ", command=seleccionar_elemento).place(x=600,y=60)     

        # labels de la ventana
        tk.Label(ventana, text="Informacion de la Gramatica: ").place(x=160,y=80)
        label_glc1=tk.Label(ventana, text="")
        label_glc1.place(x=160,y=100)

        tk.Label(ventana, text="Producciones:").place(x=160,y=120)
        label_glc2=tk.Label(ventana, text="")
        label_glc2.place(x=160,y=120)
     

        # Función para cerrar la ventana
        def cerrar_ventana():
            ventana.destroy()

        # Crear un botón de cierre
        tk.Button(ventana, text=" Cerrar ", command=cerrar_ventana).place(x=600,y=100)


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

