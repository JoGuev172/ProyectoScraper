import datetime
import math
import os
#import sqlite3
# -*- coding: utf-8 -*-


# with open("habilidades blandas.txt", "r",encoding="utf-8") as archivo:
#     for linea in archivo:
#         lin=linea[:-1]
#         print("\""+lin+"\",")
os.system('cls')
busqueda=[
    "Adaptabilidad",
    "Pensamiento crítico",
    "Pensamiento creativo",
    "Creatividad",
    "Trabajo en equipo",
    "Resolución de problemas",
    "Ética laboral",
    "Liderazgo",
    "Gestión del tiempo",
    "Pensamiento estratégico",
    "Comunicación",
    "Atención a los detalles",
    "Habilidades blandas",
    "Gestión del estrés",
    "Resiliencia",
    "adaptabilidad",
    "pensamiento crítico",
    "pensamiento creativo",
    "creatividad",
    "trabajo en equipo",
    "resolución de problemas",
    "ética laboral",
    "liderazgo",
    "gestión del tiempo",
    "pensamiento estratégico",
    "comunicación",
    "atención a los detalles",
    "habilidades blandas",
    "gestión del estrés",
    "resiliencia"
]

hab=[
    "Adaptabilidad",
    "Pensamiento crítico",
    "Pensamiento creativo",
    "Creatividad",
    "Trabajo en equipo",
    "Resolución de problemas",
    "Ética laboral",
    "Liderazgo",
    "Gestión del tiempo",
    "Pensamiento estratégico",
    "Comunicación",
    "Atención a los detalles",
    "Habilidades blandas",
    "Gestión del estrés",
    "Resiliencia",
]

def has_SS(txt):
    habilidades=[]
    for habilidad in busqueda:
        if habilidad in txt:
            index=busqueda.index(habilidad)+1
            if(index>15):
                index=index-15
            habilidades.append(index)
    return habilidades

string="Por crecimiento, importante empresa del sector financiero, está en busca de:<br><br>LIDER DE CREDITO<br><br>Si te gustan las ventas o cambaceo, el trato con personas, eres dinámico y altamente competitivo, este trabajo es para ti.<br><br>FUNCIONES:<br>Prospección (Búsqueda de nuevos clientes), Evaluación (de prospectos), Promoción de Servicios Financieros, Colocación de créditos  y recuperación.<br><br>*TRABAJO 80% CAMPO*<br><br>REQUISITOS:<br>Escolaridad: Licenciatura comunicación (Concluido o trunco)<br>Edad: 30 a 50 años<br>Sexo: Indistinto<br>Experiencia en ventas o cambaceo<br>Gusto por el trabajo de campo<br>Manejo de personal<br>Vehículo propio <br><br>OFRECEMOS:<br>-Sueldo base mensual <br>-Prestaciones de Ley y superiores desde el primer día<br>-Atractivo esquema de comisiones<br>-Oportunidad de crecimiento laboral <br>-Actividades de integración<br><br>Si te interesa formar parte de este gran equipo, postúlate por este medio o bien, haznos llegar tu CV o Solicitud con fotografía.<br><br>==TE ESTAMOS ESPERANDO"

# res=has_SS(string)
# print(res)
# try:
#     sqliteConnection = sqlite3.connect('base_resultados_scraping.db')
#     cursor = sqliteConnection.cursor()
#     print("Successfully Connected to SQLite")

#     for ha in hab:
#         query="INSERT INTO habilidades('nombre') VALUES('"+ha+"')"
#         cont=cursor.execute(query)
#         sqliteConnection.commit()
    
# except sqlite3.Error as error:
#     print("no jaja salu2")


def update_consola(mensaje : str, porcentaje: int, pagina: int, log="Sin nada que mostrar..."):
    os.system('cls')
    print("--------PRUEBA EN CURSO, HORA: "+str(datetime.datetime.now())+"-------------")
    print("PAGINA: JOBAUTS, PAGINA:", pagina)
    print("Mensaje de estado: ", mensaje)
    print("Avance total:")
    por=math.floor(porcentaje/2)
    falt=50-por
    print(str("Avance: |"+'█'*por)+str('-'*falt)+"| ("+str(porcentaje)+".00% completado)")
    print("NOTAS ADICIONALES, VARIABLES, ETC: ")
    print(log)

update_consola("TEST::::", 26, 54, "variables")