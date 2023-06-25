import graphviz
from graphviz import Digraph
import random

class NodoDerivacion:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)

    def __str__(self):
        return self.valor

dot = Digraph()  # Crear un objeto Digraph    
global nodoanterior
nodoanterior="o"
nodovacio ="p"
nodonuevo="q"
nodohijo="r"

def graficar(nodo,nivel):  # para Generar grafo
    global nodoanterior
    global nodovacio
    global nodonuevo
    global nodohijo
       
    if str(nodo).strip() != "":  # verifica que no venga vacio el nodo
        if len(str(nodo))==1:
            if nivel==0:
                dot.node(str(nodo)+str(nivel),str(nodo)) #genera nodo inicial
                print("genera nodo inicial : ",str(nodo)+str(nivel), " nivel: ",nivel," label = ", str(nodo))    
                nodoanterior = (str(nodo)+str(nivel))
            else:
                dot.node(str(nodo)+str(nivel),str(nodo))                
                print("genera nodo: ",str(nodo)+str(nivel), " nivel: ",nivel," label = ", str(nodo))    #genera nodos
                dot.edge(str(nodoanterior),str(nodo)+str(nivel))                                              #Genera Transiciones              
                nodoanterior = (str(nodo)+str(nivel))
                nodovacio = str(nodoanterior)
        else:   # Separar la expresion si tiene mas de 1 simbolo T o NT
                  
            nodonuevo = (str(nodo)+str(nivel))   
            dot.node(str(nodonuevo),str(nodo))
            dot.edge(str(nodoanterior),str(nodonuevo))
         
            cadena=str(nodo)
            for hoja in cadena:
                i=random.randint(0,1000)
                if not hoja in nodoanterior:                    
                    dot.node(str(hoja)+str(i),str(hoja))                
                    print("genera hoja: ",str(hoja), " nivel ",nivel," label = ", str(hoja))                #genera nodos
                    dot.edge(str(nodonuevo),str(hoja)+str(i))                                            #Genera Transiciones
                    print("Transicion nodo: ",str(nodonuevo), " -------> ",str(hoja)+str(i))
                    #nodoanterior = str(nodovacio) 
                else:
                    dot.node(str(hoja)+str(i),str(hoja)) 
                    nodohijo = (str(hoja)+str(i))  
                    print("genera nodo: ",str(nodohijo), " nivel ",nivel," label = ", str(hoja))                #genera nodos
                    dot.edge(str(nodonuevo),str(nodohijo))                                            #Genera Transiciones
                    print("Transicion nodo: ",str(nodonuevo), " -------> ",str(nodohijo))
            nodoanterior = nodohijo
        
    else:        
        nodoanterior = str(nodovacio) 

def construir_arbol_derivacion(glc):
    nodo = NodoDerivacion(glc.s_inicial)

    for produccion in glc.producciones:
        hijo = construir_arbol_derivacion_aux(produccion, glc)
        nodo.agregar_hijo(hijo)

    return nodo

def construir_arbol_derivacion_aux(produccion, glc):
    no_terminal, produce, produccion = produccion.partition("::=")
    nodo = NodoDerivacion(produccion)
    for simbolo in produccion.split():
        if simbolo in glc.no_terminal:
            hijo = construir_arbol_derivacion_aux(simbolo, glc)
            nodo.agregar_hijo(hijo)

    return nodo

def visualizar_arbol_derivacion(nodo, nivel=0):
    #print("  " * nivel + str(nodo))
    #----------------------------------------------------------------
    graficar(nodo,nivel)  # Generar grafo
    for hijo in nodo.hijos:
        visualizar_arbol_derivacion(hijo, nivel + 1)

class GramaticaLibredeContexto:
    def __init__(self, nombre, no_terminal, terminal, s_inicial, producciones ):
        self.nombre = nombre
        self.no_terminal = no_terminal
        self.terminal = terminal
        self.s_inicial = s_inicial
        self.producciones = producciones

def genera_arbol_derivacion( nom,nt,t,i,prod):
# Variables para almacenar los datos de la gramatica actual
    
    nombre=nom
    no_terminal = nt
    terminal = t
    s_inicial = i
    producciones = prod

    # Construir el objeto GramaticaLibredeContexto
    glc = GramaticaLibredeContexto(nombre, no_terminal, terminal, s_inicial, producciones)

    # Construir el árbol de derivación
    arbol_derivacion = construir_arbol_derivacion(glc)

    # Visualizar el árbol de derivación
    visualizar_arbol_derivacion(arbol_derivacion)

    # Establecer atributos del grafo
    dot.attr(rankdir='TB')
    dot.render('grafo', format='png', view=True)  # Para ver el grafo en pantalla


