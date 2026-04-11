# Laboratorio 1: Simulación de un Robot Móvil
### Nombres:
* **Hans Silva**
* **Zhiheng Lei**
* **Inti Liberona**
* **Kevin Álvarez**
* **Renato Mujica**


### Descripcion del laboratorio:
Este proyecto implementa el control cinemático de un robot diferencial **e-puck** en el entorno **Webots**. El objetivo es manipular las velocidades de los motores izquierdo ($v_l$) y derecho ($v_r$) para ejecutar movimientos rectos, curvas y rotaciones, validando las ecuaciones de velocidad lineal ($v$) y angular ($\omega$). 


### Como ejecutar:
1. **Requisitos:** Tener instalado **Webots** y **Python 3.x**.
2. **Crear el mundo:** Abrir Webots y crear un mundo nuevo en plano.
4. **Configuración:** * Seleccionar el robot e-puck en el árbol de escena.
    * En el campo `controller`, pegar el código del controlador que se encuentra en este repositorio.
5. **Simulación:** Presionar el botón `Play` para iniciar el movimiento.


### Resultados obtenidos:

Se validaron los estados de movimiento base mediante la configuración de velocidad en los motores:

| Tarea | Velocidad Izq ($v_l$) | Velocidad Der ($v_r$) | Resultado |
| :--- | :--- | :--- | :--- |
| **Línea Recta** | 2.0 | 2.0 | Movimiento lineal uniforme. |
| **Curva** | 1.0 | 2.0 | Trayectoria circular hacia la izquierda. |
| **Rotación** | 2.0 | -2.0 | Giro sobre su propio eje central. |

**Nota:** El código del controlador está hecho para que, cada ciertos segundos, cambie el tipo de movimiento, de esta manera, en una sola ejecución podemos ver los 3 tipos de movimiento (Linear, Curva y Rotación)


### Preguntas de análisis:

1. **¿Qué ocurre cuando ambas ruedas tienen la misma velocidad?** El robot se desplaza en línea recta. Al ser las velocidades iguales, la diferencia entre ellas es cero, lo que anula la velocidad angular ($\omega = 0$).

2. **¿Cómo cambia la trayectoria cuando las velocidades son diferentes?** Se produce una trayectoria curva. El robot gira hacia el lado de la rueda que tiene menor velocidad; a mayor diferencia de velocidad, menor es el radio de giro.

3. **¿Qué ocurre cuando una rueda gira en sentido opuesto a la otra?** Si las magnitudes son iguales pero de signo contrario, el robot realiza una rotación pura sobre su propio eje. La velocidad lineal es $0$, por lo que cambia su orientación sin desplazarse.

4. **¿Qué tipo de movimiento permite dibujar un círculo?** Mantener velocidades constantes pero asimétricas ($v_r \neq v_l$) durante todo el recorrido. Esto asegura un radio de giro constante que cierra la trayectoria en un círculo.
