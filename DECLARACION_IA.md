# Declaración de uso de Inteligencia Artificial

**Actividad:**
Proyecto final: Ray Tracer

**Integrantes:**
Gustavo Botello Salcido

**Fecha:**
9/Nov/2026

> Esta declaración es obligatoria en toda tarea, práctica y en el proyecto final.
> **No da ni quita puntos**: es un reporte adicional que se revisa aparte y se
> devuelve con comentarios. **No se evalúa cuánta IA usaron**, sino si pueden
> dar cuenta de lo que entregaron.

---

## 0. ¿Se usó IA en esta actividad?

- [ ] **No.** Firmen la última sección y terminen. Con eso queda completa.
- [x] **Sí.** Contesten los cinco puntos.

---

## 1. Herramienta(s) utilizada(s)

| Herramienta               | Versión o modelo, si lo saben |
| ------------------------- | ----------------------------- |
| Claude ia                 | Sonet 5.5                     |
| Autocompletado de VS Code |

> Cuenta también el autocompletado del editor (Copilot y similares). Si sólo
> fue eso, basta con decirlo en un renglón y seguir al punto 4.

---

## 2. Objetivo del uso

| Para qué la usamos                                                                        | En qué parte del entregable                                                                                   |
| ----------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Apoyo en sustitución y resolución de las cuadráticas del plano y esfera cuando me atoraba | Métodos de interseccion de las clases Esfera y Plaano en figuras.py                                           |
| Generación de algunos casos de frontera para probar la intersección en plano y esfera     | test_figuras.py: test_esfera_con_choque, test_esfera_sin_choque, test_plano_con_choque, test_plano_sin_choque |

> Sean específicos. _"Para la tarea"_ no dice nada.
> _"Para generar las pruebas de `minimo_de_llaves`"_ sí.

---

## 3. Prompts principales

Textuales, tal como los escribieron. No los limpien ni los reescriban.

```
en plano, dame casos frontera dode d= 1 y d = -1, igual con t y en esfera dame delta = 1 y -1,  igual t1, t2, pq solo se me
ocurrieron cunado es 0
```

```
los que tengo que desarrollar son : |P(t) − C|² = r² y (P(t) − Q) · N = 0 vea¿
```

```
aiiuuuuuudaaaaaa muestrame el proceso completo de sustitucion y resolucion de la cuadratica, de la esfera y el plano, ya m atore
```

---

## 4. Cómo se incorporó o se descartó lo obtenido

**Éste es el punto que más pesa.**

| Qué produjo la herramienta                      | ¿Aceptado, modificado o descartado? | Por qué                                                                                                                                                                                                                | Dónde quedó (archivo / commit)                                                |
| ----------------------------------------------- | ----------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------- |
| Resolucón paso a paso de ecuaciones cuadráticas | Rechazado                           | A pesar de que me dió las soluciones, lo que hice fue comparar donde me atoré con lo que me dió claude, después yo seguí con la solucón y volví a comparar con lo que me dió claude cuando llegue a la respuesta final | Figuras.py, metodo interseccion de plano y esfera, commits: fbe44d9 y 3b9ebbd |
| Casos de prueba para casos frontera             | Aceptado                            | Probaban casos que no sabía como llegar a ellos                                                                                                                                                                        | test_figuras.py, commit: 2882bf1                                              |

> **"Lo descartamos" es una respuesta excelente**, si dicen por qué.
> Una declaración donde todo se aceptó sin cambios es una declaración que
> no muestra criterio.

### 4.1 Si la usaron para el análisis: el contraste

Se les pidió intentarlo primero por su cuenta. Si lo hicieron así:

|                                                                      |                                                                                            |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| ¿Qué encontró la herramienta que ustedes **no** habían notado?       | Un pequeño error cuando escribí los metodos de intersección (puse \* en lugar de .punto()) |
| ¿Qué **no** encontró, que en este curso sí consideramos un problema? | No me recomendó refactorizar epsilon en interseccion                                       |

> La segunda es la que más nos interesa. Una herramienta suele no señalar la
> duplicación de código, porque el programa funciona igual. Ustedes ya saben
> por qué eso sí importa.
>
> Si no usaron IA para el análisis, escriban _"no aplica"_.

### 4.2 ¿Cómo verificaron que lo que incorporaron era correcto?

Las soluciones de cuadráticas que me dió se acercaban a lo que tenía yo, sólo tuve que comparar lo que me dió con lo que llevaba yo y al final yo llegue a mi respuesta, la comparé con la de claude y ambas coincidian. Y los casos de prueba probaban casos forntera y pasaban

> Una prueba que escribieron, una ejecución, un contraste contra las notas de
> clase o contra el enunciado. _"Lo revisamos"_ no es una verificación.

---

## 5. Reflexión

### 5.1 ¿Qué limitación concreta observaron **en esta actividad**?

No recomendó refactorizar epsilon, y también me generó casos frontera que ya tenía cuando claramente le indiqué cuales me hacían falta

> Concreta. No _"a veces se equivoca"_, sino _"propuso pruebas sólo para
> m = 4 y nunca para órdenes impares, porque no conocía la definición del
> laboratorio"_.

### 5.2 ¿Qué harían distinto la próxima vez?

No rendirme tan fácilmente.. no era tan difícil como pensaba, solamente no se me ocurría como seguir

---

## Firma

> Declaramos que entendemos y podemos explicar todo lo que entregamos,
> independientemente de las herramientas que hayamos utilizado.

| Nombre                  | Número de cuenta |
| ----------------------- | ---------------- |
| Gustavo Botello Salcido | 323177308        |
