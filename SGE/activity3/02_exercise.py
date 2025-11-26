student = {}

id = 0
name = ""
subjects = []
grades = []

options = """
Seleccione una opción:
1. Añadir estudiante
2. Mostrar todos los estudiantes
3. Calcular promedio de un estudiante
4. Salir
"""

while True:
    print(options)
    try:
        option = int(input("Ingrese una opción: "))
    except ValueError:
        print("Debe ingresar un número válido.\n")
        continue

    if option == 1:
        # Añadir un estudiante con sus materias y notas
        while id != -1:
            try:
                id = int(input("Ingrese el ID del estudiante (-1 para terminar): "))
            except ValueError:
                print("ID inválido.\n")
                continue

            if id == -1:
                break

            # Excepción → el ID ya existe
            if id in student:
                print("⚠️ Ese estudiante ya existe.\n")
                continue

            name = input("Ingrese el nombre del estudiante: ")

            try:
                num_subjects = int(input("Ingrese el número de materias: "))
            except ValueError:
                print("Debe ingresar un número válido.\n")
                continue

            subjects = []
            grades = []

            for _ in range(num_subjects):
                subject = input("Ingrese el nombre de la materia: ")

                # Excepción → nota no válida
                try:
                    grade = float(input("Ingrese la nota de la materia: "))
                except ValueError:
                    print("Nota inválida. Debe ser numérica.\n")
                    continue

                subjects.append(subject)
                grades.append(grade)

            student[id] = {
                "name": name,
                "subjects": subjects,
                "grades": grades
            }

    elif option == 2:
        # Mostrar todos los estudiantes con sus materias y notas
        if not student:
            print("No hay estudiantes registrados.\n")
        else:
            for student_id, info in student.items():
                name = info.get("name", "")
                subjects = info.get("subjects", [])
                grades = info.get("grades", [])
                print(f"\nID del estudiante: {student_id}")
                print(f"Nombre: {name}")
                print("Materias y notas:")
                for subject, grade in zip(subjects, grades):
                    print(f"  - {subject}: {grade}")

    elif option == 3:
        # Calcular el promedio de las notas de un alumno
        try:
            student_id = int(input("\nIngrese el ID del estudiante para calcular el promedio de sus notas: "))
        except ValueError:
            print("Debe ingresar un número válido.\n")
            continue

        # Excepción → estudiante no existe
        if student_id not in student:
            print("⚠️ Ese estudiante no existe.\n")
            continue

        grades = student[student_id].get("grades", [])
        if grades:
            average = sum(grades) / len(grades)
            print(f"El promedio de las notas del estudiante con ID {student_id} es: {average:.2f}")
        else:
            print("El estudiante no tiene notas registradas.")

    elif option == 4:
        break

    else:
        print("Opción no válida. Por favor, seleccione una opción del 1 al 4.\n")
