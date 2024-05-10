# Antonio Aguilera

### Hipótesis:
Dado un número entero no negativo 
𝑛
n, queremos calcular su factorial 
𝑛
!
n!.

### Precondición:
El parámetro de entrada 
𝑛
n debe ser un número entero no negativo.

### Postcondición:
La función devuelve el factorial del número 
𝑛
n.

### Entrada:
Un número entero no negativo 
𝑛
n.

### Salida:
El factorial 
𝑛
!
n! del número 
𝑛
n.

### Efecto:
El efecto de la función es calcular recursivamente el factorial del número 
n según la definición matemática.

### Pseudocódigo:
1. Función factorial(n):
2.    Si n es igual a 0:
3.        Retornar 1  # Caso base
4.    Sino:
5.        Retornar n multiplicado por factorial(n - 1)  # Paso recursivo

## Bubble Sort
Bubble Sort es un algoritmo de ordenación simple que funciona comparando pares de elementos adyacentes y intercambiándolos si están en el orden incorrecto. Este proceso se repite hasta que no se necesiten más intercambios, lo que significa que la lista está ordenada.

### Funcionamiento del Bubble Sort
Comenzando desde el principio de la lista, se comparan los elementos adyacentes.
Si el elemento actual es mayor que el siguiente, se intercambian.
Este proceso se repite hasta llegar al final de la lista.
Después de un pase completo por la lista, el elemento más grande se ha "burbujeado" hacia su posición final.
Luego, se repiten los pasos 1-4 para el resto de la lista, excluyendo el último elemento que ya está en su posición correcta.
Este proceso se repite hasta que no se realicen más intercambios, lo que indica que la lista está ordenada.
Casos de Uso
Bubble Sort es adecuado para ordenar listas pequeñas o para propósitos educativos, ya que su complejidad de tiempo es 
O(n[2]), lo que significa que puede ser ineficiente para listas grandes. Sin embargo, debido a su simplicidad, es fácil de implementar y entender.

### Ejemplo Conceptual
Consideremos la lista de números: [34, 7, 23, 32, 5].

Primer pase:
Se comparan y se intercambian (34, 7) → [7, 34, 23, 32, 5]
Se comparan y se intercambian (34, 23) → [7, 23, 34, 32, 5]
Se comparan y se intercambian (34, 32) → [7, 23, 32, 34, 5]
Se comparan y se intercambian (34, 5) → [7, 23, 32, 5, 34]
Segundo pase:
Se comparan y se intercambian (7, 23) → [7, 23, 32, 5, 34]
Se comparan y se intercambian (23, 32) → [7, 23, 32, 5, 34]
Se comparan y se intercambian (32, 5) → [7, 23, 5, 32, 34]
Tercer pase:
Se comparan y se intercambian (7, 23) → [7, 23, 5, 32, 34]
Se comparan y se intercambian (23, 5) → [7, 5, 23, 32, 34]
Cuarto pase:
Se comparan y se intercambian (7, 5) → [5, 7, 23, 32, 34]
Después de cuatro pases, la lista está ordenada: [5, 7, 23, 32, 34].