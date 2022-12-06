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
    
    datos = [
        ("Antonio", "García", 240),
        ("Maria", "Rodríguez", 210),
        ("Manuel", "Gonzalez", 300),
        ("Isabel", "Fernandez", 270),
        ("Jose", "Martínez", 330),
    ]
    empleados = []

    for empleado in datos:
        empleados += [Empleado(*empleado)]

    for e in empleados:
        empleado = f"{Fore.RED}Empleado {Fore.BLUE}[{Fore.WHITE}{e.nombre} {e.apellido}{Fore.BLUE}]"
        nomina = f"{Fore.GREEN}\tNomina: {Fore.WHITE}{e.calcular_nomina()}"
        print(f"{empleado}. {nomina}")


if __name__ == "__main__":
    main()
