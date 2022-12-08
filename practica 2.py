# Lista de dias de la semana
diaSemanal = []
horasSemanal = []
mayor_y_menor = ["mayor horas laboradas", "Menor Horas laboradas"]


# subprograma de los datos del empleado

def datosempleados():
    nombre = input("Digite el nombre completo del empleado")
    cedula = int(input("Digite el numero de cedula"))
    print("El empleado con el nombre", nombre, "que porta la cedula", cedula)


def ingresarlosdatoslarales():
    i = 0
    while i != 6:
        dia = input("Digite el dia que laboro\n")
        diaSemanal.append(dia)
        horasLaborales = int(input("Digite la cantidad de hora que laboro en ese dia"))
        horasSemanal.append(horasLaborales)
        i += 1
    print("\t\t\tLos datos obtenidos por medio de nuestro programa\t\t\t ")
    x = 0
    y = 0
    print("\n      Dia        \t\t\t", "Horas laboradas")
    print()
    while x != 6:
        print("\n", diaSemanal[x], "\t\t\t", horasSemanal[y], "\t\t\t")

        x += 1
        y += 1
    total_horas=horasSemanal[0]+horasSemanal[1]+horasSemanal[2]+horasSemanal[3]+horasSemanal[4]+horasSemanal[5]
    print("Total de horas laboradas\t\t\t\t",total_horas )


def mayorymenorhoras():
    x = 0
    y = 0
    z = 0
    print("Mayor horas laboradas durante la semana")
    while y != 6:
        print("\n", diaSemanal[x], "\t\t\t", horasSemanal[y], "\t\t\t", mayor_y_menor[z])

        x += 1
        y += 1
        z += 1

        if horasSemanal > 8:
            mayor_y_menor[0]=horasSemanal
        if horasSemanal <= 7:
            mayor_y_menor[1]=horasSemanal

calculodesalariobruto():



def main():
    print("\t\t\t Programa de calculo salarial los Melocotones S.A\t\t\t")
    print("Bienvenido al programa que te permite calcular tu salario bruto y neto semanalmente a todos nuestros")
    while True:
        print("Seleccione uno de los datos que aparece en nuestro menu")
        print("1- datos principal")
        print("2- Ingresar los datos laborales")
        print("3- Mayor y menor horas laborales")
        print("4- Calculo de salario bruto")
        print("5- calculo de dalario neto")
        print("6- Salir")
        print()
        y = int(input("Digite el numero del menu que desea ingresar"))

        if y == 1:
            print("Bienvenido a la pagina principal, en esta pagina tendras que llenar los datos solicitados")
            datosempleados()
            continue
        if y == 2:
            print("Esta pagina te permite llenar los datos laboradas en la empresa semanalmente")
            ingresarlosdatoslarales()
            print("fin de la sección de ingresar datos laborales")
            continue
        if y == 3:
            print("Esta pagina te permite saber cuales dias fue las horas mas laboradas y las menos laboradas ")
            mayorymenorhoras()
            print("fin de la sección de datos mayor y menor horas laboradas ")
            continue
        if y == 4:
            calculodesalariobruto()
            continue

        if y == 5:
            calculodesalarioneto()
            continue

        if y == 6:
            print("Gracias por visitarnos ")
            break

        else:
            print("Error, intente nuevamente en el programa")
main()
