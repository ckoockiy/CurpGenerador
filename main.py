from curp import *


if __name__ == "__main__":
    curp = ''
    primer_apellido = input("Ingresa el primer apellido ")
    curp = primer_apellido_letra_vocal(primer_apellido)

    segundo_apellido = input("Ingresa el segundo apellido ")
    curp += segundo_apellido_primer_letra(segundo_apellido)

    nombre = input("Ingresa tu(s) nombre(s) ")
    curp += nombre_pila(nombre)

    anio_nacimiento = int(input("Ingresa tu año de nacimiento ej: 1990 "))
    mes_nacimiento = input("Ingresa tu mes de nacimiento ej: MARZO ")
    dia_nacimiento = int(input("Ingresa tu dia de nacimiento ej: 20 "))

    curp += fecha_nacimiento(anio_nacimiento, mes_nacimiento, dia_nacimiento)

    genero = int(input("""Selecciona tu genero: 1)H 2)M """))
    curp += letra_genero(genero)

    entidad = input("Ingresa tu entidad federativa ")
    curp += entidad_federativa(entidad)

    curp += primer_consonante_interna(primer_apellido)
    curp += primer_consonante_interna(segundo_apellido)
    curp += primer_consonante_interna(nombre)

    curp += alfanumerico_aleatorio()
    curp += digito_aleatorio()

    print(f"Tu curp es: {curp}")
