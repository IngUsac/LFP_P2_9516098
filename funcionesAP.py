import tkinter as tk
import graphviz
from tkinter import filedialog
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from generarderivacion import genera_arbol_derivacion
from manejaAP import validar_cadena

class AutomatasDePila:
    def __init__(self, nombre, alfabeto, simbolos, estados, s_inicial, aceptacion, transiciones ):
        self.nombre = nombre
        self.alfabeto = alfabeto
        self.simbolos = simbolos
        self.estados = estados
        self.s_inicial = s_inicial
        self.aceptacion = aceptacion
        self.transiciones = transiciones


archivoentradaAP=""
global AP_seleccionado
global Apila
Apila = []

def cargar_archivo_pila(): # Permite cargar N Automatas de Pila

    archivoentradaAP=filedialog.askopenfilename(initialdir = "/LFP_P2_9516098",title = "Archivo de Entrada",filetypes = (('Archivos de Automatas de Pila ', '*.ap'),("Todos los Archivos","*.*")))
    if archivoentradaAP:
        carga=True
        
    # Leer el archivo de texto línea por línea
    with open(archivoentradaAP, "r") as archivoAP:
        # Variables para almacenar los datos de la AP actual
        nombre = ""
        alfabeto = ""
        simbolos = ""
        estados = ""
        s_inicial = ""
        aceptacion = ""
        transiciones = []
    

        i=0
        existe = False
    
        for linea in archivoAP:
            nom = linea.split("\n")     #validar que el nombre del AP no exista
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
                    AP = AutomatasDePila(nombre,alfabeto,simbolos,estados,s_inicial,aceptacion,transiciones)
                    Apila.append(AP)

                # Reiniciar las variables para la próxima gramatica
                nombre = ""
                alfabeto = ""
                simbolos = ""
                estados = ""
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
                                         

                if i ==2 and existe==False: # para separar el alfabeto del archivo de entrada y guardarlo en la pila
                    alfabeto = datos[0].rstrip("'")
                    

                if i ==3 and existe==False: # para separar simbolos del archivo de entrada y guardarlo en la pila
                    simbolos = datos[0].rstrip("'")
                    
                if i ==4 and existe==False: # para separar los estados del archivo de entrada y guardarlo en la pila
                    estados = datos[0].rstrip("'")

                if i ==5 and existe==False: # para separar el s_inicial del archivo de entrada y guardarlo en la pila
                    s_inicial  = datos[0].rstrip("'")
                    
                if i ==6 and existe==False: # para separar el s_inicial del archivo de entrada y guardarlo en la pila
                    aceptacion  = datos[0].rstrip("'")
                    

                if i > 6 and existe==False: # para separar las n producciones del archivo de entrada y guardarlo en la pila
                        # Guardar las producciones
                    datos[0]= datos[0].replace(" ","").rstrip()  # elimina espacios en blanco de las producciones    
                    datos[0]= datos[0].replace("$","ε").rstrip()  # elimina espacios en blanco de las producciones    
                    transiciones.append(datos[0].rstrip("'")) 
    if carga:
        messagebox.showinfo("Carga de Archivo", " El archivo de entrada se cargó correctamente")            

    if not Apila:
        messagebox.showinfo("Validación de AP", "La pila está vacía")

    
def informacion_pila():     #Permite mostrar la informacionde los Automatas de pila y genera pdf y grafo
    def seleccionar_elemento():
        indice = int(entry.get()) - 1
        if 0 <= indice < len(Apila):
            AP_seleccionado = Apila[indice]

            label_glc1.config(text=f" -Nombre: {AP_seleccionado.nombre}"+f"  -Alfabeto: {AP_seleccionado.alfabeto} "+f"  -Simbolos: {AP_seleccionado.simbolos} "+f"  -Estado Inicial: {AP_seleccionado.s_inicial} "+f"  -Estado de Aceptacion: {AP_seleccionado.aceptacion} ")
            label_glc1.place(x=150,y=100)          
          
            tk.Label(ventana, text=" Transiciones: ").place(x=150,y=120)
            texto_cuadro.delete("1.0", tk.END)  # Borrar contenido previo del cuadro de texto
            for cadena in AP_seleccionado.transiciones:
                texto_cuadro.insert(tk.END, "\n"+cadena)  # Insertar el contenido del elemento en el cuadro de texto     
            def generar_grafo_AP():
                grafo = graphviz.Digraph()                  # Crear un objeto de gráfico dirigido   
                grafo.attr(rankdir='LR')  
                for cadena in AP_seleccionado.transiciones:
                    print("transiciones para grafoAP",cadena)


                grafo.node('A')                             # Agregar nodos
                grafo.node('B')           
                grafo.edge('A', 'B', label='S0,ε,ε;S1,#')    # Agregar una flecha de transición con etiqueta          
                grafo.render('grafoAP', format='png')       # Renderizar y guardar el gráfico en un archivo
                
                      
            def generar_pdf():
                # Crear un documento PDF
                pdf_filename = "reporteAP.pdf"
                c = canvas.Canvas(pdf_filename, pagesize=letter)               
                c.setFont("Helvetica", 12)

                # Escribir la información en el PDF
                c.drawString(100, 800, " Reporte del Automata de Pila")
                c.drawString(100, 750, f" -Nombre: {AP_seleccionado.nombre}")
                c.drawString(100, 730, f" -Alfabeto: {AP_seleccionado.alfabeto}")
                c.drawString(100, 710, f" -Simbolos: {AP_seleccionado.simbolos}")
                c.drawString(100, 690, f" -Estado Inicial: {AP_seleccionado.s_inicial}")
                c.drawString(100, 670, f" -Estado de Aceptacion: {AP_seleccionado.aceptacion}")
                c.drawString(100, 650, f" -Transiciones:")
                i=110
                for cadena in AP_seleccionado.transiciones:
                    i-=20
                    c.drawString(150, 530+i, cadena)
                
                imagen_filename = "Logo_Ingenieria.jpg"
                c.drawImage(imagen_filename, 25, 725, width=50, height=50)
                generar_grafo_AP()
                c.drawImage('grafoAP.png', 100, 400,width=200, height=100)        # grabar en el pdf la imagen creada en el paso anterior
 
                c.save()                       # Guardar y cerrar el PDF

                messagebox.showinfo("Generación de Reporte PDF", "El Reporte PDF se ha generado exitosamente.")
      

        else:
            messagebox.showinfo("Seleccionar de Gramática", "Numero de Gramatica invalido")
            texto_cuadro.delete("1.0", tk.END)  # Borrar contenido previo del cuadro de texto
            
    
            label_glc1.config(text=" ")
            label_glc1.place(x=150,y=100)
            

        tk.Button(ventana, text="Generar PDF", command=generar_pdf).place(x=675,y=80)

    if not Apila:
        messagebox.showinfo("Validación de Gramática", "La pila está vacía")
    else:
        



    # Crear una nueva ventana
        ventana = tk.Toplevel()
        ventana.title("AP Válidos")
        ventana.geometry("800x600")

        tk.Label(ventana, text="Listado de Automatas de Pila disponibles").place(x=25,y=20)

        for i, gramatica in enumerate(Apila):
            tk.Label(ventana, text=f"{i+1}: {gramatica.nombre}").place(x=25,y=(40+(20*i)))
            

        entry = tk.Entry(ventana)
        entry.place(x=600,y=20)

        tk.Label(ventana, text=" Ingrese el numero del Automata de Pila que desea consultar ").place(x=250,y=20)
        tk.Button(ventana, text=" Consultar ", command=seleccionar_elemento).place(x=600,y=50)     
        tk.Label(ventana, text=" Informacion del Automata de Pila: ").place(x=150,y=80)
        label_glc1=tk.Label(ventana, text="")
        label_glc1.place(x=150,y=100)
        
     

        texto_cuadro = tk.Text(ventana, height=20, width=75)
        texto_cuadro.place(x=150,y=150)
       

               # Función para cerrar la ventana
        def cerrar_ventana():
            ventana.destroy()

        # Crear un botón de cierre
        tk.Button(ventana, text="  Cerrar   ", command=cerrar_ventana).place(x=675,y=50)
        
   
def validar_cadena_pila():  #Permite validar si una cadena ingresada es aceptada o rechazada por el AP seleccionado
    #validar_cadena(AP_seleccionado)
    def seleccionar_elemento():
        indice = int(entry.get()) - 1
        if 0 <= indice < len(Apila):
            AP_seleccionado = Apila[indice]

            label_glc1.config(text=f" -Nombre: {AP_seleccionado.nombre}"+f"  -Alfabeto: {AP_seleccionado.alfabeto} "+f"  -Simbolos: {AP_seleccionado.simbolos} "+f"  -Estado Inicial: {AP_seleccionado.s_inicial} "+f"  -Estado de Aceptacion: {AP_seleccionado.aceptacion} ")
            label_glc1.place(x=150,y=140)          
          
            tk.Label(ventana, text=" Transiciones: ").place(x=150,y=170)
            texto_cuadro.delete("1.0", tk.END)  # Borrar contenido previo del cuadro de texto
            for tansc in AP_seleccionado.transiciones:
                texto_cuadro.insert(tk.END, "\n"+tansc)  # Insertar el contenido del elemento en el cuadro de texto     
            def validaC():
                cadena = str(entry2.get())
                validar_cadena(AP_seleccionado,cadena)

            entry2 = tk.Entry(ventana)
            entry2.place(x=450,y=80)
            
            for tansc in AP_seleccionado.transiciones:
                #print(tansc)
                pass
            
            tk.Label(ventana, text=" Ingrese la cadena a Validar ").place(x=300,y=80)
            tk.Button(ventana, text="Validar Cadena", command=validaC).place(x=600,y=80)
          
            
            
      

        else:
            messagebox.showinfo("Seleccionar de Gramática", "Numero de Gramatica invalido")
            texto_cuadro.delete("1.0", tk.END)  # Borrar contenido previo del cuadro de texto
            
    
            label_glc1.config(text=" ")
            label_glc1.place(x=150,y=140)
            

        

    if not Apila:
        messagebox.showinfo("Validación de Gramática", "La pila está vacía")
    else:
        



    # Crear una nueva ventana
        ventana = tk.Toplevel()
        ventana.title("AP Válidos")
        ventana.geometry("800x600")

        tk.Label(ventana, text="Listado de Automatas de Pila disponibles").place(x=25,y=20)

        for i, gramatica in enumerate(Apila):
            tk.Label(ventana, text=f"{i+1}: {gramatica.nombre}").place(x=25,y=(40+(20*i)))
            

        entry = tk.Entry(ventana)
        entry.place(x=600,y=20)

        tk.Label(ventana, text=" Ingrese el numero del Automata de Pila que desea consultar ").place(x=250,y=20)
        tk.Button(ventana, text=" Consultar ", command=seleccionar_elemento).place(x=600,y=50)     
        tk.Label(ventana, text=" Informacion del Automata de Pila: ").place(x=150,y=120)
        label_glc1=tk.Label(ventana, text="")
        label_glc1.place(x=150,y=140)
        
     

        texto_cuadro = tk.Text(ventana, height=15, width=75)
        texto_cuadro.place(x=150,y=200)
       

               # Función para cerrar la ventana
        def cerrar_ventana():
            ventana.destroy()

        # Crear un botón de cierre
        tk.Button(ventana, text="  Cerrar   ", command=cerrar_ventana).place(x=675,y=50)
 

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