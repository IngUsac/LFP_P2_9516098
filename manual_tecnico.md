<img src="https://media.ingenieria.usac.edu.gt/images/joomla_template/logo_institucional.png" alt="USAC Logo" width="" height="100">

### Universidad de San Carlos de Guatemala
### Facultad de Ingeniería en Ciencias y Sistemas
### Lenguajes Formales y de Programación
### Sección "P" - Junio 2023

---
# Manual Tecnico - Proyecto Spark Stack
```python
# Manejo de Automatas de Pila 
```


### Tareas del proyecto 🦾
---

* [x] Pantalla de bienvenida
* [x] Ventana principal
* [x] Menu principal
* [x] Cargar archivo 
* [x] Validar nombres repetidos de gramaticas
* [x] informacion del automata
* [x] mostrar correctamente las transiciones
* [x] Sustituir el simbolo ">" por "|" en las transiciones
* [x] Arbol de derivación  
* [x] Cargar archivo pila
* [x] informacion pila 
* [x] Validar cadena pila
* [x] Ruta_de validacion de cadena
* [x] Mostrar recorido paso a paso
* [ ] Validar cadena en una sola pasada   🦾😮‍💨en construccion
* [x] Desplegar manual de Usuario en Markdown
* [x] Desplegar manual tecnico en Markdown
* [x] Pantalla de despedida al cerrar


---

### Funciones principalesdeclaradas 👾 


```python
    
#Main.py

def ventana_bienvenida():   # Muestra una ventana de bienvenida durante 5 segundos y luego abre la ventana principal
def ventana_principal():    # Crear la ventana principal
def cerrar_ventana():       # Cierra la ventana principal y muestra la ventana de despedida durante 5 segundos

#Modulo Gramaticas libres de contexto
#funciones.py
def cargar_archivo_glc():   # Permite cargar N gramaticas libres del contexto
def informacion_glc():      # Muestra todos los nombres de las gramaticas que se encuentran cargados en el sistema
def arbol_derivacion():     # Muestra arbol de derivacion previa solicitud del nombre de la gramatica 
def cargar_archivo_pila():  # Permite cargar N autómatas de pila al sistema
def informacion_pila():     # Muestra informacion del automata almacenado previamente
def validar_cadena_pila():  # Valida una cadena con un automata previamente cargado por el usuario
def ruta_validacion_cadena(): #Muestra las transiciones hechas por una cadena ingresada por el usuario, a un automata previamente cargado
def recorido_paso_paso():   # Muestra paso a paso el comportamiento del automata al validar una cadena ingresada por el usuario, a un automata previamente cargado
def cerrar_ventana():       # Cierra la ventana principal y muestra la ventana de despedida durante 5 segundos


#generarderivacion.py 
class NodoDerivacion:       # Para manejar el arbol de derivaciones
def graficar(nodo,nivel):  # para Generar grafo
def construir_arbol_derivacion(glc):  # para armar el arbol de derivacion
    nodo = NodoDerivacion(glc.s_inicial)
class GramaticaLibredeContexto: # Para manejar el la pila 
def genera_arbol_derivacion( nom,nt,t,i,prod):   # para generar el arbol de derivacion
def visualizar_arbol_derivacion(arbol_derivacion) #despliega el arbol por medio del metodo graficar  

#Modulo Automatas de Pila

def cargar_archivo_pila(): # Permite cargar N Automatas de Pila
def informacion_pila():     #Permite mostrar la informacionde los Automatas de pila y genera pdf y grafo
def validar_cadena_pila():  #Permite validar si una cadena ingresada es aceptada o rechazada por el AP seleccionado
def ver_ruta():             # Muestra el recorrido que hizo el autoamata hasta validar la cadena de entrada

# cargarMD.py    Modulo para cargar los manuales de usuario en Markdown
def abrir_manual_tecnico(): #abre manual tecnico en Markdown
def abrir_manual_usuario(): # Abre Manual de Usuario en Markdown

# manejaAP.py    Modulo para validar las cadenas ingresadas del AP
def validar_cadena(Ap_seleccionado,cadena): #Valida la cadena ingresada por el usuario

```


---
## Repositorio del proyecto 
---
<img src="https://cdn4.iconfinder.com/data/icons/iconsimple-logotypes/512/github-512.png" alt="Github Logo" width="75" height="75">


🐱
[Repositorio github.com](https://github.com/IngUsac/LFP_P2_9516098 "Repositorio del Proyecto 2 - LFP") 


---

## Enlaces útiles

[Emojis para MD](https://www.webfx.com/tools/emoji-cheat-sheet/)
🤖
