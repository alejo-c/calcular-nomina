# Repositorio: https://github.com/alejo-c/calcular-nomina
# Presentado por: José Alejandro Castrillón Ortega

from colorama import Fore, Style, init


HORA_TRABAJO = 35000
PORCENTAJE_DESCUENTO = 0.4


class Empleado:

    nombre: str
    apellido: str
    horas_trabajadas: int

    def __init__(self, nombre, apellido, horas):
        self.nombre = nombre
        self.apellido = apellido
        self.horas_trabajadas = horas

    def descuento_salud(self, salario_base):
        return salario_base * PORCENTAJE_DESCUENTO

    def descuento_pension(self, salario_base):
        return salario_base * PORCENTAJE_DESCUENTO

    def calcular_nomina(self):
        base = HORA_TRABAJO * self.horas_trabajadas
        nomina = base - self.descuento_salud(base) - self.descuento_pension(base)
        return nomina


def main():
    init(convert=True)

    # datos = []
    # print('A continuación ingrese los datos de 5 empleados...')
    # for i in range(5):
    #     print (f'- Empleado {i+1} ----------') # Empleado i
    #     nombre = input('Nombre: ')
    #     apellido = input('Apellido: ')
    #     horas_trabajadas = int(input('Horas Trabajadas (mes): '))
    #     datos += [(nombre, apellido, horas_trabajadas)]

    datos = [
        ("Antonio", "García", 240),
        ("Maria", "Rodríguez", 210),
        ("Manuel", "González", 300),
        ("Isabel", "Fernández", 270),
        ("Jose", "Martínez", 330),
    ]
    empleados = []

    for empleado in datos:
        empleados += [Empleado(*empleado)]

    print("\n- Resultados -----------")
    for e in empleados:
        empleado = f"{Fore.RED}Empleado {Fore.BLUE}[{Fore.WHITE}{e.nombre} {e.apellido}{Fore.BLUE}]"
        nomina = f"{Fore.GREEN}Nomina = {Fore.WHITE}{e.calcular_nomina()}"
        print(f"{empleado}: \t{nomina}")


if __name__ == "__main__":
    main()
