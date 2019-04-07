"""

Dictio for Golden Dictionary (Online Version)

author= Dolan Hêriş

author_email= dolanskurd@mail.com

GitHub: https://github.com/dolanskurd/Dictio

"""

import requests
import sys
import io
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

root_url = 'http://dictio.kurditgroup.org/dictio/'
word = input('\r\n')
url = requests.get(root_url + word).text
soup = BeautifulSoup(url, 'lxml')


css = """<style type="text/css">

#gdarticlefrom-8760b966b9972903e0a7d6fc4519da4a .related-translation-title {
        font-size: 12pt;
        color: navy;
        direction: rtl;
}

#gdarticlefrom-8760b966b9972903e0a7d6fc4519da4a .kig_tran {
        direction: rtl;
}


#gdarticlefrom-8760b966b9972903e0a7d6fc4519da4a .kig_val, .en {
        direction: ltr;
        font-size: 12pt;
        color: navy;
}

#gdarticlefrom-8760b966b9972903e0a7d6fc4519da4a #top-title, p.bold {
        direction: rtl;
        text-align: center;
        font-size: 12pt;
        color: navy;
        font-family: 'Times New Roman';
}

#gdarticlefrom-8760b966b9972903e0a7d6fc4519da4a .related-translation-title {
        font-weight: bold;
}

#gdarticlefrom-8760b966b9972903e0a7d6fc4519da4a .ku {
        font-size: 12pt;
        
}

#gdarticlefrom-8760b966b9972903e0a7d6fc4519da4a .word {
        font-size: 12pt;
        font-weight: bold;
}
</style>"""

print(css, '\n')

dictio_title = soup.find('div', id='top-title')
print(css, dictio_title)

dictio_title2 = soup.find('p', 'bold')
print(css, dictio_title2)
print(css, '\n')

print('<div class="word">' + str(word) + '</div>')
print(css, '\n')


meaning = soup.find('h2')
if meaning == None:
        print(css, '\n')
else:  
        print(css, meaning)
print(css, '\n')
print(css, '<hr>')

extra = soup.find('div', 'related-translation-title')
print(css, extra)
print(css, '\n')

for all_related in soup.findAll('div', 'translation clear index parent'):
    en_word = all_related.find('div', attrs={'class': 'kig_val index en'})
    ku_word = all_related.find('div', attrs={'class': 'kig_tran ku'})
    if en_word == None or ku_word == None:
            print(css, '\n')
    else:     
            print(css, en_word, ku_word)
            print(css, '<hr>')
print(css, '\n')
