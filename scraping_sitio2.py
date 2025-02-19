from time import sleep
import requests
from bs4 import BeautifulSoup
import datetime
import os
import random
import sqlite3
import math
# -*- coding: utf-8 -*-

os.system('cls')
print("--------NUEVA PRUEBA, HORA: "+str(datetime.datetime.now())+"-------------")
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

busqueda_eng=[
    "Adaptability",
    "Critical thinking",
    "Creative thinking",
    "Creativity",
    "Teamwork",
    "Problem-solving",
    "Work ethic",
    "Leadership",
    "Time management",
    "Strategic thinking",
    "Communication",
    "Attention to details",
    "Soft skills",
    "Stress management",
    "Resilience",
    "adaptability",
    "critical thinking",
    "creative thinking",
    "creativity",
    "teamwork",
    "problem-solving",
    "work ethic",
    "leadership",
    "time management",
    "strategic thinking",
    "communication",
    "attention to details",
    "soft skills",
    "stress management",
    "resilience"
]

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

def has_SS(txt):
    habilidades=[]
    for habilidad in busqueda:
        if habilidad in txt:
            index=busqueda.index(habilidad)+1
            if(index>15):
                index=index-15
            habilidades.append(index)

    if(len(habilidades)!=0):
        return habilidades
    for habilidad in busqueda_eng:
        if habilidad in txt:
            index=busqueda_eng.index(habilidad)+1
            if(index>15):
                index=index-15
            habilidades.append(index)
    return habilidades

empleos=[]
sqliteConnection = sqlite3.connect('base_resultados_scraping.db')
cursor = sqliteConnection.cursor()

for pag in range(5):
    update_consola("PROCESO INICIADO", (pag*33)-33, pag)

    url="https://www.occ.com.mx/empleos/trabajo-en-tecnologias-de-la-informacion-sistemas/?page="+str(pag)
    pag=requests.get(url)
    update_consola("Obtenido contenido de pagina principal", (pag*33)-33+2, pag)
    soup=BeautifulSoup(pag.content, "html.parser")
    #dom = etree.HTML(str(soup))
    try:
        #print(dom.xpath('//*[@id="meteored_page"]/main/span[1]/span/span[1]/span[3]/span/span[1]/section/span[2]/span[2]')[0].text)
        # print(soup.find(class="dato-temperatura"))
        # 
        update_consola("Obtenido soup de la pagina principal", (pag*33)-33+2, pag)
        # for i in soup.find_all("a", class_="out"):
        #     url_emp="https://www.jobatus.mx"+i["href"]
        #     
        #     empleos.append(url_emp)
        for i in soup.find_all("a", class_="jobcard-0-2-568"):
            url_emp="https://www.occ.com.mx"+i["href"]
            update_consola("LINK DETECTADO en pagina principal", (pag*33)-33+2, pag, url_emp)
            empleos.append(url_emp)
    except:
        update_consola("ERROR AL OBTENER LINKS DE LA PAGINA PRINCIPAL", 0, pag, "modificar para ver, supongo")
        break

    update_consola("OBTENIDOS LINKS DE LA PAGINA PRINCIPAL", (pag*33)-33+10, pag)
    # revision pagina por pagina
    cont=0
    for j in empleos:
        cont=cont+1
        url_un_emp=j
        pag_emp=requests.get(url_un_emp)
        av_prel=(cont*33)/len(empleos)
        
        soup_uniq=BeautifulSoup(pag_emp.content, "html.parser")
        update_consola("OBTENIDO SOUP DE SOLICITUD", (pag*33)-33+av_prel-40, pag, "siguiente: entrar a bloque try")
        try:
            desc=soup_uniq.find("div", class_="noMargin-0-2-567").getText()

            vacante=soup_uniq.find("p", class_="text-0-2-81 heading-0-2-84 highEmphasis-0-2-102 title-0-2-517").getText()#text-0-2-81 heading-0-2-84 highEmphasis-0-2-102 title-0-2-517  <-class
            empresa=soup_uniq.find("span", class_="text-0-2-81 standard-0-2-88 highEmphasis-0-2-102 strong-0-2-91").getText()#text-0-2-81 standard-0-2-88 highEmphasis-0-2-102 strong-0-2-91   <- class
            salario=soup_uniq.find("p", class_="text-0-2-81 subheading-0-2-85 highEmphasis-0-2-102").getText()#text-0-2-81 subheading-0-2-85 highEmphasis-0-2-102   <- class
            fecha="fecha no proporcionada"#creo que un now o un no se proporciono

            update_consola("UBICADOS ELEMENTOS NECESARIOS", (pag*33)-33+av_prel-30, pag)

            skills=has_SS(desc)
            query_emp="INSERT INTO solicitudes(link, vacante, sueldo, empresa, fecha_publicacion) VALUES('"+str(j)+"', '"+str(vacante)+"', '"+str(salario)+"', '"+str(empresa)+"', '"+str(fecha)+"');"
            
            cursor.execute(query_emp)
            update_consola("NUEVO EMPLEO REGISTRADO", (pag*33)-33+av_prel-20, pag)
            last_id_sol=cursor.lastrowid
            sqliteConnection.commit()
            update_consola("commit realizado (1)", (pag*33)-33+av_prel-10, pag, "siguiente: insertar SS")

            for skill in skills:
                query_habil="INSERT INTO habilidades_solicitud(id_habilidad, id_solicitud) VALUES("+int(skill)+", "+last_id_sol+");"
                cursor.execute(query_habil)
                sqliteConnection.commit()
            
            update_consola("Termino de operacion empleo individual", (pag*33)-33+av_prel)

            #lo que sea que se requiera
            
        except:
            update_consola("ERROR DURANTE LA INSERCION DE LOS DATOS DEL EMPELO INDIVIDUAL", 0, pag, "cambiar...")
            cursor.close()
            pass
        
        segs=random.randint(5, 9)
        update_consola("COMPLETADA SOLICITUD DE EMPLEO, PREPARANDO EL SIGUIENTE CONJUNTO", pag*33, pag, "sin errores")
        sleep(segs)
    cursor.close()
update_consola("COMPLETADO SITIO DE JOBATUS", 100, 5, "exito")