#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""

Dictio English / Kurdish Open Dictionary for Golden Dictionary (Online Version)

author = Dolan Hêriş

author_email = dolanskurd@mail.com

GitHub: https://github.com/dolanskurd/Dictio

"""

import requests
import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

root_url = "https://dictio.kurditgroup.org/dictio/"
word = input("\r\n")
url = requests.get(root_url + word).text
soup = BeautifulSoup(url, "lxml")


css = """<style type="text/css">
.title_en {
        font-family: hack, Verdana, sans-serif;
        font-size: 13pt;
        font-weight: bold;
        color: #101010;
        text-align: center;
        line-height: 1.8;
    }
    .title_ku {
        font-family: estedad, vazir, arial, tahoma, sans-serif;
        font-size: 13pt;
        font-weight: bold;
        color: #990000;
        text-align: center;
        line-height: 1.8;
    }
    .en_entry {
        font-family: hack, Verdana, sans-serif;
        font-size: 14pt;
        color: #314089;
        font-weight: bold;
    }
    .ku_entry {
        font-family: estedad, vazir, arial, tahoma, sans-serif;
        font-size: 14pt;
        color: #314089;
        font-weight: bold;
        direction: rtl;
    }
    .ku {
        font-family: estedad, vazir, arial, tahoma, sans-serif;
        font-size: 12pt;
        color: #3B3E41;
        font-weight: bold;
        direction: rtl;
    }
    .en_meaning {
        font-family: estedad, vazir, arial, tahoma, sans-serif;
        font-size: 12pt;
        color: #3B3E41;
        font-weight: bold;
    }
    .en {
        font-family: Hack, Verdana, sans-serif;
        color: #333333;
        padding: 7px 7px;
        text-align: center;
        display: inline-block;
        font-size: 12px;
        font-weight: bold;
        margin: 4px 2px;
        background-color: #EDEDED;
        border: 2px solid #EDEDED;
        border-radius: 3px;
    }
    
    .ku_equ {
        font-family: estedad, vazir, arial, tahoma, sans-serif;
        color: #333333;
        padding: 7px 7px;
        text-align: center;
        font-size: 12px;
        font-weight: bold;
        margin: 4px 2px;
        background-color: #EDEDED;
        border: 2px solid #EDEDED;
        border-radius: 3px;
        direction: rtl;
        float: right;
    }
    
    .syn{
        font-family: hack, Verdana, sans-serif;
        font-size: 12pt;
        color: #ff2500;
        font-weight: bold;
        line-height: 2;
    }
    
    .ku_syn{
        font-family: estedad, vazir, arial, tahoma, sans-serif;
        font-size: 12pt;
        color: #ff2500;
        font-weight: bold;
        line-height: 2.5;
        margin: 0 75px 0 0;
        direction: rtl;
    }
    hr{ 
        border: 0;
        height: 1px;
        background: #333;
        background-image: linear-gradient(to right, #ccc, #333, #ccc);
    }
</style>"""

print(css, "<br>")
print(css, '<div class="title_en"> Dictio English / Kurdish Open Dictionary </div>')
print(css, '<div class="title_ku"> فەرهەنگی کراوەی کوردی / ئینگلیزی دیکتیۆ </div>')
print(css, "<br>")

if word.isascii():
    print(css, "<br>")
    print(css, '<div class="en_entry">' + word + "</div>")
    print(css, "<br>")
    for container in soup.find_all("div", "col-md-8 offset-md-2"):
        for ul in container.find_all("ul"):
            for li in ul.find_all("li", class_=["list-group-item", "rtl"]):
                for ku_meaning in li.find_all("span", "dictio-result-item"):
                    print(css, '<div class="ku">' + ku_meaning.text + "</div>")
                    print(css, "<br>")
                print(css, '<div class="syn">' + "Synonyms: " + "</div>")
                for en_equ in li.find_all("span", "text-secondary bg-light pl-2 pr-2"):
                    print(css, '<span class="en">' + en_equ.text + "</span>")
                print(css, "<br>")
                print(css, "<hr>")
                print(css, "<br>")
else:
    print(css, "<br>")
    print(css, '<div class="ku_entry">' + word + "</div>")
    print(css, "<br>")
    for en_meaning in soup.find_all("div", "col-md-8 offset-md-2"):
        for ul in en_meaning.find_all("ul"):
            for li in ul.find_all("li", class_=["list-group-item", "ltr"]):
                for en_meaning in li.find_all("span", "dictio-result-item"):
                    print(css, '<div class="en_meaning">' + en_meaning.text + "</div>")
                    print(css, "<br>")
                print(
                    css, '<div class="ku_syn">' + "هاوواتاکان: " + "</div>",
                )
                for ku_equ in li.find_all("span", "text-secondary bg-light pl-2 pr-2"):
                    print(
                        css, '<div class="ku_equ">' + ku_equ.text + "</div>",
                    )

                print(css, "<br>" * 4)
                print(css, "<hr>")
                print(css, "<br>")

    print(css, "<br>")
