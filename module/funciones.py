### Fichero de funciones
##Funcion para filtrar caracteres especiales dentro de una cadena.
import requests
import os
from bs4 import BeautifulSoup
## Funcion que realiza la busqueda de la informacion 
def list_search(url_search):
    if url_search.find("https://") == -1:
        return "Url no valida (-)"
    else:
        try:
            result = ""
            init = requests.get(url_search)
            soup = BeautifulSoup(init.text, "html.parser")
            products_list = soup.findAll("li", {"class" : "shops__layout-item"})
            for tag in products_list:
                product_name  = tag.find(class_="ui-search-item__title").text
                product_price = tag.find(class_="price-tag-fraction").text
                product_money = tag.find(class_="price-tag-symbol").text
                product_link  = tag.find('a', {"class" : "ui-search-link"}).get("href")
                result += "NOMBRE: {}\nPRECIO: {}-{}\nENLACE: {}\n".format(product_name, product_price, product_money, product_link)
                #result +="NOMBRE DEL PRODUCTO: {}\nPRECION: {}-{}\nENLACE: {} ".format(product_name, product_price, product_money, product_link)
            return result
        except:
            print("Error al realizar la operacion")
## funcion que guarda la informacion en un archivo TXT
def export_to_txt(string_products, filename):
    file = open("{}.txt".format(filename), "w")
    file.write(string_products+os.linesep)
    file.close()

    