promedios = []
Notas_totales = []
notas_ordenadas = []
ordenado = []
contador = 0
estudiantes = [
    {"nombre": "Ana", "notas": [4.9, 5.2, 4.3]},
    {"nombre": "Luis", "notas": [6.1, 5.8, 6.5]},
    {"nombre": "María", "notas": [3.8, 4.5, 2.9]},
    {"nombre": "Carlos", "notas": [6.5, 6.2, 6.8]},
    {"nombre": "Sofía", "notas": [5.2, 4.9, 6.1]},
    {"nombre": "Javier", "notas": [2.0, 3.5, 2.8]},
    {"nombre": "Lucía", "notas": [6.2, 6.5, 6.9]},
    {"nombre": "Diego", "notas": [3.5, 4.9, 2.1]},
    {"nombre": "Valentina", "notas": [6.8, 6.5, 7.0]},
    {"nombre": "Fernando", "notas": [4.9, 3.8, 5.1]},
    {"nombre": "Clara", "notas": [5.2, 6.1, 2.9]},
    {"nombre": "Andrés", "notas": [1.8, 2.5, 2.1]},
    {"nombre": "Gabriela", "notas": [6.1, 6.2, 6.5]},
    {"nombre": "Pablo", "notas": [4.5, 5.2, 3.9]},
    {"nombre": "Isabel", "notas": [6.5, 6.8, 7.0]},
    {"nombre": "Ricardo", "notas": [3.0, 4.2, 5.0]},
    {"nombre": "Natalia", "notas": [6.2, 6.1, 6.5]},
    {"nombre": "Samuel", "notas": [4.9, 5.8, 3.7]},
    {"nombre": "Laura", "notas": [5.2, 4.9, 5.8]},
    {"nombre": "Martín", "notas": [2.0, 3.0, 2.5]},
    {"nombre": "Carmen", "notas": [6.8, 6.5, 7.0]},
    {"nombre": "Jorge", "notas": [3.5, 4.8, 2.7]},
    {"nombre": "Patricia", "notas": [6.1, 6.2, 6.5]},
    {"nombre": "Esteban", "notas": [4.0, 3.9, 5.2]},
    {"nombre": "Silvia", "notas": [6.5, 6.8, 7.0]},
    {"nombre": "Alberto", "notas": [2.9, 4.2, 5.0]},
    {"nombre": "Teresa", "notas": [5.2, 4.9, 5.8]},
    {"nombre": "Victor", "notas": [1.5, 2.0, 1.7]},
    {"nombre": "Mónica", "notas": [6.8, 6.5, 7.0]},
    {"nombre": "Raúl", "notas": [4.5, 3.2, 2.8]},
    {"nombre": "Elena", "notas": [6.1, 6.2, 6.5]},
    {"nombre": "Sergio", "notas": [3.0, 4.0, 2.6]},
    {"nombre": "Ana María", "notas": [6.5, 6.8, 7.0]},
    {"nombre": "Cristian", "notas": [4.9, 5.8, 6.1]},
    {"nombre": "Lina", "notas": [2.5, 3.8, 4.2]},
    {"nombre": "Hugo", "notas": [1.0, 1.5, 2.0]},
    {"nombre": "Rosa", "notas": [6.8, 6.5, 7.0]},
    {"nombre": "Fernando", "notas": [3.9, 4.2, 5.1]},
    {"nombre": "Claudia", "notas": [6.1, 6.2, 6.5]},
    {"nombre": "Julián", "notas": [2.8, 3.7, 4.5]},
    {"nombre": "Gabriel", "notas": [6.5, 6.8, 7.0]},
]

# Calcular el promedio de cada estudiante
for estudiante in estudiantes:
    nombre = estudiante["nombre"]
    notas = estudiante["notas"]
    promedio = sum(notas) / len(notas)
    promedios.append(promedio)
    print(f"El promedio de {nombre} es: {promedio:.1f}")

maximo = max(promedios)
minimo = min(promedios)
print(f"Máximo: {maximo:.1f}  Mínimo: {minimo:.1f}")

# Contar estudiantes con todas las notas >= 4
for estudiante in estudiantes:
    notas = estudiante["notas"]
    if notas[0] >= 4.0 and notas[1] >= 4.0 and notas[2] >= 4.0:
        contador += 1

# Juntar todas las notas
for estudiante in estudiantes:
    for nota in estudiante["notas"]:
        Notas_totales.append(nota)

# Buscar la más frecuente
M_frecuente = None
Repeticiones_Max = 0
for nota in Notas_totales:
    Repeticiones = Notas_totales.count(nota)
    if Repeticiones > Repeticiones_Max:
        M_frecuente = nota
        Repeticiones_Max = Repeticiones

# Contar estudiantes con al menos una nota < 4
total_de_estudiantes = len(estudiantes)
los_bajos = 0
for estudiante in estudiantes:
    notas = estudiante["notas"]
    if notas[0] < 4.0 or notas[1] < 4.0 or notas[2] < 4.0:
        los_bajos += 1

porcentaje = (los_bajos / total_de_estudiantes) * 100

for promedio in promedios:
    notas_ordenadas.append(promedio)  

notas_ordenadas.sort(reverse=True)   
  

# Resultados finales
print(f"Cantidad de alumnos que aprobaron todas sus asignaturas: {contador}")
print(f"La nota más frecuente (moda) es: {M_frecuente} y aparece {Repeticiones_Max} veces")
print(f"Estudiantes con al menos una nota bajo 4.0: {los_bajos} de {total_de_estudiantes}")
print(f"Porcentaje: {porcentaje:.1f}%")
print("Promedios ordenados de mayor a menor:")
for promedio in notas_ordenadas:
    print(f"{promedio:.1f}", end=" ")