#EJERCICIO 6

class NodoJedi:
    def __init__(self, jedi):
        self.jedi = jedi
        self.izq = None
        self.der = None

class ArbolJedi:
    def __init__(self):
        self.raiz = None
    
    # a) CREAR ÁRBOLES DE ACCESO (por nombre, ranking, especie)
    def insertar_por_nombre(self, jedi):
        """Inserta ordenado por nombre"""
        if self.raiz is None:
            self.raiz = NodoJedi(jedi)
        else:
            self._insertar_recursivo(self.raiz, jedi, lambda x: x['nombre'])
    
    def insertar_por_ranking(self, jedi):
        """Inserta ordenado por ranking"""
        if self.raiz is None:
            self.raiz = NodoJedi(jedi)
        else:
            self._insertar_recursivo(self.raiz, jedi, lambda x: x['ranking'])
    
    def _insertar_recursivo(self, nodo, jedi, clave):
        if clave(jedi) < clave(nodo.jedi):
            if nodo.izq is None:
                nodo.izq = NodoJedi(jedi)
            else:
                self._insertar_recursivo(nodo.izq, jedi, clave)
        else:
            if nodo.der is None:
                nodo.der = NodoJedi(jedi)
            else:
                self._insertar_recursivo(nodo.der, jedi, clave)
    
    # b) BARRIDO INORDEN (izquierda → nodo → derecha)
    def barrido_inorden(self):
        resultado = []
        self._inorden_recursivo(self.raiz, resultado)
        return resultado
    
    def _inorden_recursivo(self, nodo, resultado):
        if nodo:
            self._inorden_recursivo(nodo.izq, resultado)
            resultado.append(nodo.jedi)
            self._inorden_recursivo(nodo.der, resultado)
    
    # c) BARRIDO POR NIVELES (BFS)
    def barrido_por_niveles(self):
        if not self.raiz:
            return []
        
        resultado = []
        cola = [self.raiz]
        
        while cola:
            nodo = cola.pop(0)
            resultado.append(nodo.jedi)
            
            if nodo.izq:
                cola.append(nodo.izq)
            if nodo.der:
                cola.append(nodo.der)
        
        return resultado
    
    # d) MOSTRAR TODO SOBRE YODA Y LUKE
    def buscar_por_nombre(self, nombre):
        return self._buscar_recursivo(self.raiz, nombre, lambda x: x['nombre'])
    
    def _buscar_recursivo(self, nodo, valor, clave):
        if not nodo:
            return None
        
        if clave(nodo.jedi) == valor:
            return nodo.jedi
        elif valor < clave(nodo.jedi):
            return self._buscar_recursivo(nodo.izq, valor, clave)
        else:
            return self._buscar_recursivo(nodo.der, valor, clave)
    
    # e) MOSTRAR TODOS LOS JEDI MASTER
    def buscar_por_ranking(self, ranking):
        resultado = []
        self._buscar_ranking_recursivo(self.raiz, ranking, resultado)
        return resultado
    
    def _buscar_ranking_recursivo(self, nodo, ranking, resultado):
        if nodo:
            if nodo.jedi['ranking'] == ranking:
                resultado.append(nodo.jedi)
            
            # Buscar en ambos lados (el árbol por ranking puede tener coincidencias)
            self._buscar_ranking_recursivo(nodo.izq, ranking, resultado)
            self._buscar_ranking_recursivo(nodo.der, ranking, resultado)


#EJERCICIO 15
class NodoIndice:
    def __init__(self, nombre, posicion_archivo):
        self.nombre = nombre
        self.mrr = posicion_archivo  # Posición en el archivo
        self.izq = None
        self.der = None

class IndiceStarWars:
    def __init__(self, archivo):
        self.raiz = None
        self.archivo = archivo  # TDA archivo (del capítulo V)
    
    # a) ALMACENAR SOLO NOMBRE Y MRR
    def construir_indice(self):
        """Construye el árbol índice leyendo el archivo"""
        posicion = 0
        while posicion < len(self.archivo.registros):
            personaje = self.archivo.leer(posicion)
            self.insertar_indice(personaje['nombre'], posicion)
            posicion += 1
    
    def insertar_indice(self, nombre, mrr):
        if self.raiz is None:
            self.raiz = NodoIndice(nombre, mrr)
        else:
            self._insertar_recursivo(self.raiz, nombre, mrr)
    
    def _insertar_recursivo(self, nodo, nombre, mrr):
        if nombre < nodo.nombre:
            if nodo.izq is None:
                nodo.izq = NodoIndice(nombre, mrr)
            else:
                self._insertar_recursivo(nodo.izq, nombre, mrr)
        else:
            if nodo.der is None:
                nodo.der = NodoIndice(nombre, mrr)
            else:
                self._insertar_recursivo(nodo.der, nombre, mrr)
    
    # b) CARGAR, MODIFICAR, ELIMINAR
    def cargar_nuevo_personaje(self, nombre, mrr):
        """Inserta nuevo personaje en el índice"""
        self.insertar_indice(nombre, mrr)
    
    def modificar_personaje(self, nombre, nuevos_datos):
        """Modifica los datos usando el índice"""
        nodo = self._buscar_nodo(self.raiz, nombre)
        if nodo:
            self.archivo.modificar(nodo.mrr, nuevos_datos)
    
    def eliminar_personaje(self, nombre):
        """Elimina personaje del índice y archivo"""
        nodo = self._buscar_nodo(self.raiz, nombre)
        if nodo:
            self.archivo.eliminar(nodo.mrr)
            self.raiz = self._eliminar_recursivo(self.raiz, nombre)
    
    # c) MOSTRAR TODO SOBRE YODA Y BOBA FETT
    def obtener_informacion(self, nombre):
        nodo = self._buscar_nodo(self.raiz, nombre)
        if nodo:
            return self.archivo.leer(nodo.mrr)
        return None
    
    def _buscar_nodo(self, nodo, nombre):
        if not nodo:
            return None
        if nodo.nombre == nombre:
            return nodo
        elif nombre < nodo.nombre:
            return self._buscar_nodo(nodo.izq, nombre)
        else:
            return self._buscar_nodo(nodo.der, nombre)
    
    # d) LISTAR PERSONAJES CON ALTURA > 1 METRO (alfabético)
    def personajes_por_altura(self, altura_minima):
        resultado = []
        self._recorrer_inorden(self.raiz, resultado)
        return [p for p in resultado if p['altura'] > altura_minima]
    
    # e) LISTAR PERSONAJES CON PESO < 75 KG (alfabético)
    def personajes_por_peso(self, peso_maximo):
        resultado = []
        self._recorrer_inorden(self.raiz, resultado)
        return [p for p in resultado if p['peso'] < peso_maximo]
    
    def _recorrer_inorden(self, nodo, resultado):
        """Recorre alfabéticamente (inorden)"""
        if nodo:
            self._recorrer_inorden(nodo.izq, resultado)
            personaje = self.archivo.leer(nodo.mrr)
            resultado.append(personaje)
            self._recorrer_inorden(nodo.der, resultado)