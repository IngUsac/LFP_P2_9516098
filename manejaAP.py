class AutomataPila:
    def __init__(self,nombreAP, estados, alfabeto_entrada, alfabeto_pila, estado_inicial, estado_final, funciones_transicion):
        self.nombreAP = nombreAP
        self.estados = estados
        self.alfabeto_entrada = alfabeto_entrada
        self.alfabeto_pila = alfabeto_pila
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        self.funciones_transicion = funciones_transicion
        self.pilaAP = []
        self.estado_actual = estado_inicial

        
    def transicion(self, simbolo_entrada,ruta,tabla_una_pasada,i):
        print ("i-> ",i)
        for funcion in self.funciones_transicion:
            estado_actual, simbolo_lectura, simbolo_pila_lectura, estado_siguiente, simbolos_a_apilar = funcion                      
            if (estado_actual == self.estado_actual and simbolo_lectura == 'ε' and simbolo_pila_lectura == 'ε'):
                self.estado_actual = estado_siguiente  #insertar en pila el simbolo # inicial                 
                self.pilaAP = [simbolos_a_apilar]
                ruta.append(funcion)
                tabla_una_pasada[0].append(i)
                tabla_una_pasada[1].append("-")
                tabla_una_pasada[2].append("-")
                tabla_una_pasada[3].append(str(estado_actual)+str(simbolo_lectura)+str(simbolo_pila_lectura)+str(simbolos_a_apilar)+str( estado_siguiente))
                i+=1
  
            if ( estado_actual == self.estado_actual and simbolo_lectura == simbolo_entrada ):              
                self.estado_actual = estado_siguiente
                                
                if simbolo_pila_lectura != 'ε' and simbolos_a_apilar == 'ε':
                    self.pilaAP.pop()
                    self.estado_actual = estado_siguiente
                    ruta.append(funcion)      
                   
                    tabla_una_pasada[0].append(i)
                    tabla_una_pasada[1].append(self.pilaAP)
                    tabla_una_pasada[2].append(simbolo_entrada)
                    tabla_una_pasada[3].append(str(estado_actual)+str(simbolo_lectura)+str(simbolo_pila_lectura)+str(simbolos_a_apilar)+str( estado_siguiente))
                    break
            
                if simbolo_pila_lectura == 'ε' and simbolos_a_apilar == simbolo_entrada :
                    self.estado_actual = estado_siguiente
                    for simbolo in reversed(simbolos_a_apilar):
                        self.pilaAP.append(simbolo)
                    ruta.append(funcion)
              
                    tabla_una_pasada[0].append(i)
                    tabla_una_pasada[1].append(self.pilaAP)
                    tabla_una_pasada[2].append(simbolo_entrada)
                    tabla_una_pasada[3].append(str(estado_actual)+str(simbolo_lectura)+str(simbolo_pila_lectura)+str(simbolos_a_apilar)+str( estado_siguiente))
                    break
          
            if simbolo_pila_lectura == '#'and  simbolos_a_apilar == 'ε':  
                self.estado_actual = estado_siguiente
                if self.estado_actual == self.estado_final:
                    self.pilaAP.pop()
                    self.estado_actual = self.estado_final
                    ruta.append(funcion) 
                   
                    tabla_una_pasada[0].append(i)
                    tabla_una_pasada[1].append(self.pilaAP)
                    tabla_una_pasada[2].append(simbolo_entrada)
                    tabla_una_pasada[3].append(str(estado_actual)+str(simbolo_lectura)+str(simbolo_pila_lectura)+str(simbolos_a_apilar)+str( estado_siguiente))
                    break



    def acepta_cadena(self, cadena,ruta,tabla_una_pasada):
        
        i= -1
        cadena=cadena
        self.estado_actual = self.estado_inicial
        for simbolo in cadena:  
            i+=1
               
            if simbolo not in self.alfabeto_entrada : # si un simbolo no esta en el alfabeto de entrada no acepta la cadena
                return False
            self.transicion(simbolo,ruta,tabla_una_pasada,i)  
        
        if len(self.pilaAP)==1:
            self.transicion("#",ruta,tabla_una_pasada,i)   
        return self.estado_actual == self.estado_final and len(self.pilaAP) == 0 

def validar_cadena(Ap_seleccionado,cadena,ruta,aceptada,tabla_una_pasada): #Valida la cadena ingresada por el usuario
    # Datos del autómata de pila
    ap1 =Ap_seleccionado
    
  # Datos del autómata de pila entrante:  nombre, alfabeto, simbolos, estados, s_inicial, aceptacion, transiciones
    nombreAP=ap1.nombre
    alfabeto_entrada =  ap1.alfabeto
    alfabeto_pila = ap1.simbolos
    estados = ap1.estados
    estado_inicial = ap1.s_inicial
    estado_final = ap1.aceptacion

    lista_funciones_transicion = []

    # Procesar cada línea y agregarla a la lista final
    for linea in ap1.transiciones:
        elementos = linea.split(';')
        funcion = []
        for elemento in elementos:
            funcion.extend(elemento.split(','))
        lista_funciones_transicion.append(funcion)


    # Crear instancia del autómata de pila
    automata = AutomataPila(nombreAP,estados, alfabeto_entrada, alfabeto_pila, estado_inicial, estado_final, lista_funciones_transicion)

    # Prueba de cadenas
    if automata.acepta_cadena(cadena.strip(),ruta,tabla_una_pasada):
        aceptada=True
        return aceptada 
    else:
        aceptada=False
        return aceptada 
































""" 
class AutomataPila:
    def __init__(self, estados, alfabeto_entrada, alfabeto_pila, estado_inicial, estado_final, funciones_transicion):
        self.estados = estados
        self.alfabeto_entrada = alfabeto_entrada
        self.alfabeto_pila = alfabeto_pila
        self.estado_inicial = estado_inicial
        self.estado_final = estado_final
        self.funciones_transicion = funciones_transicion
        self.pila = []
        self.estado_actual = estado_inicial

    def transicion(self, simbolo_entrada):
        for funcion in self.funciones_transicion:
            estado_actual, simbolo_lectura, simbolo_pila_lectura, estado_siguiente, simbolos_a_apilar = funcion
            if (
                estado_actual == self.estado_actual
                and simbolo_lectura == simbolo_entrada
                and (simbolo_pila_lectura == self.pila[-1] or simbolo_pila_lectura == 'ε')
            ):
                self.estado_actual = estado_siguiente
                self.pila.pop()
                if simbolos_a_apilar != 'ε':
                    for simbolo in reversed(simbolos_a_apilar):
                        self.pila.append(simbolo)
                break

    def acepta_cadena(self, cadena):
        self.estado_actual = self.estado_inicial
        self.pila = ['#']
        for simbolo in cadena:
            if simbolo not in self.alfabeto_entrada:
                return False
            self.transicion(simbolo)
        return self.estado_actual == self.estado_final and self.pila == ['#']


# Datos del autómata de pila
alfabeto_entrada = ['a', 'b']
alfabeto_pila = ['a', 'b', '#']
estados = ['I', 'A', 'B', 'C', 'F']
estado_inicial = 'I'
estado_final = 'F'
funciones_transicion = [
    ['I', 'ε', 'ε', 'A', '#'],
    ['A', 'a', 'ε', 'B', 'a'],
    ['B', 'a', 'ε', 'B', 'a'],
    ['B', 'b', 'a', 'C', 'ε'],
    ['C', 'b', 'a', 'C', 'ε'],
    ['C', 'ε', '#', 'F', 'ε']
]

# Crear instancia del autómata de pila
automata = AutomataPila(estados, alfabeto_entrada, alfabeto_pila, estado_inicial, estado_final, funciones_transicion)

# Prueba de cadenas
cadenas = ['ab', 'abb', 'abba', 'aabb', 'aabba']
for cadena in cadenas:
    if automata.acepta_cadena(cadena):
        print(f"Cadena '{cadena}': Aceptada")
    else:
        print(f"Cadena '{cadena}': Rechazada")""" 