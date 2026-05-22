# spretes_pygame
import sys  # Importamos el módulo sys para inspeccionar el conteo de referencias y direcciones

# --- PASO 1: Objetos Inmutables y Referencias ---
print("--- Paso 1: Inmutables ---")

x = 42  # Se crea un objeto de tipo entero con el valor 42 en memoria. 'x' apunta a él.
y = x   # 'y' ahora apunta al MISMO objeto entero 42. No se creó un nuevo número.

# Verificamos si apuntan a la misma dirección de memoria usando 'id()' o el operador 'is'
print(f"Dirección de x: {id(x)}, Dirección de y: {id(y)}")
print(f"¿x e y apuntan al mismo objeto?: {x is y}")  # Retorna True

x = x + 1  # Al ser int inmutable, no se modifica el 42. Se crea un NUEVO objeto (43).
# 'x' ahora apunta a 43. 'y' sigue apuntando al 42 original.
print(f"Nuevo valor de x: {x} (Dirección: {id(x)})")
print(f"Valor de y: {y} (Dirección: {id(y)})")


# --- PASO 2: Objetos Mutables ---
print("\n--- Paso 2: Mutables ---")

lista_a = [1, 2, 3]  # Se crea un objeto lista en memoria. 'lista_a' lo referencia.
lista_b = lista_a    # 'lista_b' apunta exactamente a la misma lista.

print(f"¿Apuntan a la misma lista?: {lista_a is_not = lista_b}")  # Retorna True

lista_a.append(4)  # Modificamos la lista a través de 'lista_a'. 
# Como las listas son mutables, el objeto cambia internamente pero la dirección de memoria es la misma.

print(f"lista_b reflejó el cambio: {lista_b}")  # Muestra [1, 2, 3, 4] porque comparte el objeto
print(f"Dirección lista_a: {id(lista_a)} | Dirección lista_b: {id(lista_b)}")  # Son idénticas


# --- PASO 3: Conteo de Referencias ---
print("\n--- Paso 3: Conteo de Referencias ---")

mi_objeto = [9, 9, 9]  # Ref conteo inicial = 1
# Nota: sys.getrefcount() crea una referencia temporal al evaluar, por eso sumará 1 al total real.
```
print(f"Conteo de referencias de mi_objeto: {sys.getrefcount(mi_objeto) - 1}") 

otra_ref = mi_objeto  # Creamos una segunda referencia. Ref conteo = 2
print(f"Conteo tras nueva referencia: {sys.getrefcount(mi_objeto) - 1})"
```