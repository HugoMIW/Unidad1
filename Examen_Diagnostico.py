
#se pide 3 calificaciones de n alumnos de 0 a 100, asi como el nombre del alumno, se promedia, los alumnos que tengan calificacion menor a 70
#se les imprime un mensaje de reprobado
#al finalizar el sistema se imprime el nombre y promedio del alumno con mayor calificacion y el alumno con menor calificacion.
#se entrega algoritmo diagrama de flujo y codigo.

#Tecnologico Nacional de Mexico
#Autor: Hugo Francisco Martinez Briseño
#Programación Orientada a Objetos.
#Profesor: Rosales Alvarez Domingo

def ingresar_datos_alumnos(numero_alumnos):
    alumnos = []
    for i in range(numero_alumnos):
        print(f"\nIngrese los datos del alumno {i + 1}:")
        nombre = input("Nombre del alumno: ")
        calificaciones = []
        for j in range(3):
            while True:
                    calificacion = float(input(f"Calificación {j + 1}: "))
                    if 0 <= calificacion <= 100:
                        calificaciones.append(calificacion)
                        break
                    else:
                        print("La calificación debe estar entre 0 y 100 Inténtalo de nuevo.")
        alumnos.append((nombre, calificaciones))
    return alumnos

def calcular_promedio(calificaciones):
    sum = (lambda number: sum(calificaciones)/ len(calificaciones), calificaciones)
    return sum

def determinar_estado(promedio):
    return "Aprobado" if promedio > 70 else "Reprobado"

def mostrar_resultados(alumnos):
    promedios = []
    
    for nombre, calificaciones in alumnos:
        promedio = calcular_promedio(calificaciones)
        promedios.append(promedio)
        
        estado = determinar_estado(promedio)
        print(f"{nombre} - Promedio: {promedio} - Estado: {estado}")
        
        if promedio > promedio_mayor:
            promedio_mayor = promedio
        else: 
            promedio < promedio_menor
            promedio_menor = promedio
    
    print(f"\n Promedio mayor: {promedio_mayor:}")
    print(f"Promedio menor: {promedio_menor:}")

def main():
    while True:
            numero_alumnos = int(input("Ingrese el número de alumnos: "))
            if numero_alumnos > 0:
                break
    alumnos = ingresar_datos_alumnos(numero_alumnos)
    mostrar_resultados(alumnos)

main()
