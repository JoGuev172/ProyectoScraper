import requests
from bs4 import BeautifulSoup
import datetime
import os

url="https://www.opcionempleo.com.mx/buscar/empleos?s=programador&l=M%C3%A9xico&lid=36815&radius=15"
pag=requests.get(url)

soup=BeautifulSoup(pag.content, "html.parser")
#dom = etree.HTML(str(soup))
try:
    #print(dom.xpath('//*[@id="meteored_page"]/main/span[1]/span/span[1]/span[3]/span/span[1]/section/span[2]/span[2]')[0].text)
    # print(soup.find(class="dato-temperatura"))
    #
    # desc=soup.find("div", class_="noMargin-0-2-567").getText()
    # print(desc)
    # print("vacante", soup.find("p", class_="text-0-2-81 heading-0-2-84 highEmphasis-0-2-102 title-0-2-517").getText())
    # print("empresa", soup.find("span", class_="text-0-2-81 standard-0-2-88 highEmphasis-0-2-102 strong-0-2-91").getText())
    # print("salario", soup.find("p", class_="text-0-2-81 subheading-0-2-85 highEmphasis-0-2-102").getText())
    print(soup)
    # for i in soup.find_all("a", class_="jkit_Efecu jkit_ff9zU hyperlink_appearance_undefined jkit__gDKk _2dWEc6"):
    #     url_emp=i["href"]
    #     print(url_emp)
except:
    print("f")