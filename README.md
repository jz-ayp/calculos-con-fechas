# Funciones

## Ejercicio: Cálculos con fechas

## Enunciado

Escribe las siguientes funciones en Python:

1. Una función (`es_bisiesto`) que determine si un año es bisiesto (regresa `True`) o no (regresa `False`).

2. Una función (`dias_del_mes`) que determine la cantidad de días en un mes dado. Para el mes de febrero se debe tomar en cuenta si el año es bisiesto, por lo tanto, la función debe tener dos entradas numéricas: `mes` y `anho`. Utiliza la función del inciso anterior para determinar si el año es o no bisiesto, no repliques el código en esta nueva función. El año deberá ser opcional; si no se indica, se considerará, por omisión que el año no es bisiesto.
  
3. Usando las dos funciones anteriores, escribe una función (`dia_siguiente`) que reciba como entrada tres números enteros que representen una fecha (día, mes y año) y determine la fecha del día siguiente, y regrese tres enteros que representen dicha fecha, en el mismo orden (día, mes y año).

4. Usando las funciones de los incisos (1) y (2), escribe una función (`dia_anterior`) que reciba como entrada tres números enteros que representan una fecha (día, mes y año) y determine la fecha del día anterior, y regrese tres enteros que representen dicha fecha, en el mismo orden (día, mes y año).

5. Usando las funciones anteriores, escribe una función (`sumar_dias`) que reciba como entrada una tupla y un número entero. La tupla representa una fecha (día, mes, año), y el entero, que puede ser positivo o negativo, representa la cantidad de días después (o antes, de ser negativo) de dicha fecha. Es decir, la función determinará la fecha que se obtiene al sumar o restar la cantidad días indicados a la fecha inicial. La función debe regresar una tupla de tres enteros que representen la fecha resultante: (día, mes, año).

**_Nota_**: Utilizar únicamente código propio y el trabajado en clase para estos ejercicios. En particular, el módulo `datetime` contiene funciones para realizar estos cálculos, ***y no se deberá usar*** para codificar la solución. Aunque sí lo pueden utilizar para verificar sus resultados.


## Instrucciones
- Elabora los correspondientes análisis y algoritmos antes de escribir el código de cada una de las funciones. Utiliza diagramas de flujo para representar cada uno de tus algoritmos e ilustrar su lógica. 

- Codifica tu solución en el archivo [`funciones_fecha.py`](/funciones_fecha.py).
     
- Prueba tus funciones corriéndolas varias veces con diferentes datos de entrada. Verifica que tu algoritmo produzca las salidas correctas. Identifica y pon atención especial a los casos que pudieran ser problemáticos de manejar (casos límite).

- Añade cadenas de documentación a tu programa y a cada una de tus funciones.

  
## Entrega
Completa éste y el resto de los ejercicios y compila, para cada uno, el enunciado, análisis, diagrama de flujo, código y pruebas de ejecución, en un informe tal como se describe en los requisitos para entrega de tareas en Canvas. No olvides incluir portada y conclusiones.


## Casos de prueba de ejemplo

### `es_bisiesto`
| Entradas | Salidas |
|:---------|:--------|
| `2000`  | `True`   |
| `2026`  | `False`  |

### `dias_del_mes`
| Entradas    | Salidas |
|:------------|:--------|
| `1`         | `31`    |
| `2`         | `28`    |
| `4`, `2026` | `30`    |
| `2`, `2000` | `29`    |

### `dia_siguiente`

| Entradas          | Salidas          |
|:------------------|:-----------------|
| `1`, `2`, `2026`  | `2`, `2`, `2026` |
| `28`, `2`, `2026` | `1`, `3`, `2026` |

### `dia_anterior`

| Entradas          | Salidas            |
|:------------------|:-------------------|
| `10`, `5`, `2017` | `9`, `5`, `2017`   |
| `1`, `1`, `2019`  | `31`, `12`, `2018` |

### `sumar_dias`

| Entradas                 | Salidas          |
|:-------------------------|:-----------------|
| `(17, 5, 2028)`, `365`   | `(17, 5, 2029)`  |
| `(17, 5, 2028)`, `-365`  | `(18, 5, 2027)`  |
| `(25, 12, 2026)`, `-365` | `(25, 12, 2025)` |


## Rúbrica
Verifica tu entrega contra la rúbrica disponible en Canvas para maximizar tu calificación.
