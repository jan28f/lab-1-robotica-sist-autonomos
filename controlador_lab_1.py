from controller import Robot
from random import uniform

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# https://www.cyberbotics.com/doc/guide/epuck?version=cyberbotics:R2019a
separacion_ruedas: float = 0.071
radio_ruedas: float = 0.0205

rueda_izq = robot.getDevice("left wheel motor")
rueda_der = robot.getDevice("right wheel motor")

rueda_izq.setPosition(float("inf"))
rueda_der.setPosition(float("inf"))
rueda_izq.setVelocity(0)
rueda_der.setVelocity(0)

def generarRuido() -> float:
    return uniform(-0.1, 0.1)

def calcularVelocidad(vel_izq_rad: float, vel_der_rad: float):
    vel_izq_metros: float = radio_ruedas * vel_izq_rad
    vel_der_metros: float = radio_ruedas * vel_der_rad

    vel_lineal: float = (vel_izq_metros + vel_der_metros) / 2
    vel_angular: float = (vel_der_metros - vel_izq_metros) / separacion_ruedas

    return vel_lineal, vel_angular

def moverRobot(vel_izq: float, vel_der: float, ruido: bool = False) -> None:
    ruido_izq: float = 0 if ruido == False else generarRuido()
    ruido_der: float = 0 if ruido == False else generarRuido()
    vel_izq_final = vel_izq + ruido_izq
    vel_der_final = vel_der + ruido_der

    rueda_izq.setVelocity(vel_izq_final)
    rueda_der.setVelocity(vel_der_final)

    vel_lineal, vel_angular = calcularVelocidad(vel_izq_final, vel_der_final)
    print(f"Ruido activado: {ruidoActivo}")
    print(f"Velocidad lineal (m/s): {vel_lineal}")
    print(f"Velocidad angular (m/s): {vel_angular}")

contador: int = 0
ruidoActivo: bool = False
print(f"Ruido activado: {ruidoActivo}")
while robot.step(timestep) != -1:
    if contador <= 300:
        # Linea recta
        moverRobot(3.0, 3.0, ruido=ruidoActivo)
    elif contador <= 600:
        # Girar sobre si mismo
        moverRobot(3.0, -3.0, ruido=ruidoActivo)
    elif contador <= 900:
        # Circunferencia
        moverRobot(3.0, 1.5, ruido=ruidoActivo)
    elif contador == 1200:
        contador = 0
        ruidoActivo = not ruidoActivo
    
    contador += 1