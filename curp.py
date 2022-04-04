
import random


def primer_apellido_letra_vocal(primer_apellido):
    vocales = "aeiou"
    letras = primer_apellido[0]

    for i in primer_apellido[1:]:
        if i in vocales:
            letras += i
            break

    return letras.upper()


def segundo_apellido_primer_letra(segundo_apellido):
    return segundo_apellido[0].upper()


def nombre_pila(nombre):
    if len(nombre.split()) == 1:
        return nombre[0].upper()

    if len(nombre.split()) == 2:
        if nombre[0:4].upper() == "JOSE" or nombre[0:5].upper() == "MARIA":
            return nombre.split()[1][0].upper()
        else:
            return nombre.split()[0][0].upper()


def fecha_nacimiento(anno, mes, dia):

    meses = {'Enero': "01", 'Febrero': "02", 'Marzo': "03", 'Abril': "04", 'Mayo': "05", 'Junio': "06",
             'Julio': "07", 'Agosto': "08", 'Septiembre': "09", 'Octubre': "10", 'Noviembre': "11", 'Diciembre': "12"}

    fecha = str(anno)[2:]+meses[mes.capitalize()]+str(dia)
    return fecha


def letra_genero(genero):

    if genero == 1:
        return "H"
    elif genero == 2:
        return "M"
    else:
        return "Opcion incorrecta"


def entidad_federativa(entidad):

    entidades_federativas = {
        "AGUASCALIENTES": "AS",
        "BAJA CALIFORNIA": "BC",
        "BAJA CALIFORNIA SUR": "BS",
        "CAMPECHE": "CC",
        "COAHUILA": "CL",
        "COLIMA": "CM",
        "DISTRITO FEDERAL": "DF",
        "DURANGO": "DG",
        "GUANAJUATO": "GT",
        "GUERRERO": "GR",
        "HIDALGO": "HG",
        "JALISCO": "JC",
        "MEXICO": "MC",
        "MICHOACAN": "MN",
        "MORELOS": "MS",
        "NAYARIT": "NT",
        "NUEVO LEON": "NL",
        "OAXACA": "OC",
        "PUEBLA": "PL",
        "QUERETARO": "QT",
        "QUINTANA ROO": "QR",
        "SAN LUIS POTOSI": "SP",
        "SINALOA": "SL",
        "SONORA": "SR",
        "TABASCO": "TC",
        "TAMAULIPAS": "TS",
        "TLAXCALA": "TL",
        "VERACRUZ": "VZ",
        "YUCATAN": "YN",
        "ZACATECAS": "ZS",
        "NACIDO EN EL EXTRANJERO": "NE"
    }

    return entidades_federativas[entidad.upper()]


def primer_consonante_interna(palabra):
    consonantes = "BCDFGHJKLMNÑPQRSTVXZWY"
    
    for i in palabra.upper()[1:]:
        if i in consonantes:
            return i


def alfanumerico_aleatorio():
    alfa = "abcdefghijklmnñopqrstuvwxyz"
    return random.choice(alfa).upper()


def digito_aleatorio():
    digitos = "0123456789"
    return str(random.choice(digitos))
