from time import sleep
import requests
from bs4 import BeautifulSoup
import datetime
import os
import random
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
#que obtenga las habilidades
#/////puesto que ofrecen
#////numero de habilidades
#//////enlace
#vacante
#que habilidaes tienen
###si se puede, el sueldo
#4 sitios en total
#50 cada uno
#
#
#
#
#
#
#https://bolsadetrabajobuap.blogspot.com/
def has_SS(txt):
    habilidades=[]
    for habilidad in busqueda:
        if habilidad in txt:
            index=busqueda.index(habilidad)+1
            if(index>15):
                index=index-15
            habilidades.append(index)
    return habilidades

empleos=[]

for i in range(4):

    url="https://www.occ.com.mx/empleos/de-programador/en-puebla/?page="+str(i)
    pag=requests.get(url)

    soup=BeautifulSoup(pag.content, "html.parser")
    #dom = etree.HTML(str(soup))
    try:
        #print(dom.xpath('//*[@id="meteored_page"]/main/span[1]/span/span[1]/span[3]/span/span[1]/section/span[2]/span[2]')[0].text)
        # print(soup.find(class="dato-temperatura"))
        # 
        #print(soup)
        for i in soup.find_all("a", class_="jobcard-0-2-568"):
            url_emp="https://www.occ.com.mx"+i["href"]
            print(url_emp)
            empleos.append(url_emp)
    except:
        print("f")


    # revision pagina por pagina
    for j in empleos:
        url_un_emp=j
        pag_emp=requests.get(url_un_emp)

        soup_uniq=BeautifulSoup(pag_emp.content, "html.parser")
        try:
            desc=soup_uniq.find("div", class_="noMargin-0-2-567").getText()
            #lo que sea que se requiera
            if(has_SS(desc)):
                print("Empleo con url:", j, "revisado, resultado: solicita habilidades blandas")
            else:
                print("Empleo con url:", j, "revisado, resultado: NO solicita habilidades blandas")
        except:
            print("Fx2")
        segs=random.randint(5, 9)
        sleep(segs)
