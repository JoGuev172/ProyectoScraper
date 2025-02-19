import requests
from bs4 import BeautifulSoup
from lxml import etree

sitios=[
    "https://www.jobatus.mx/trabajo?q=programador&l=Puebla,+Puebla&jb=all&page=1",
    "https://www.buscojobs.mx/ofertas/tc25/trabajo-de-tecnologias-de-la-informacion/programador_puebla",#PARA PASAR DE PAGINA  SE AÑADE /<<PAGINA>>
    "https://www.opcionempleo.com.mx/buscar/empleos?s=programador&l=M%C3%A9xico&radius=25&sort=relevance"
]

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

#sitio ejemplo: https://www.buscojobs.mx/programador-backend-parque-industrial-2000-en-puebla-de-los-angeles-ID-43933288