__author__ = 'ucitel'
#from __future__ import unicode_literals
import xml.sax
pole_zamestanci=[]

class XMLContextHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)
        self.element = None
        self.user_name = None
        self.user_group = None
        self.mzda = None
        self.odmena = None

    def startElement(self, name, attrs):
        self.element = name

    def endElement(self, name):
        self.element = None
        if name =='row':
            self.pole_array=[self.user_name,self.user_group,self.mzda,self.odmena]
            pole_zamestanci.append(self.pole_array)

    def characters(self, content):
        if self.element == 'loginid':
            self.user_name = content
            #self.veta_array[self.user_name,]
        if self.element == 'stredisko':
            self.user_group = content
        if self.element == 'mzda':
            self.mzda = content
        if self.element == 'odmena':
            self.odmena = content


f = open("vstup.xml", "r")
xml.sax.parse(f, XMLContextHandler())
f.close()
suma = 0
suma_odmena = 0
print pole_zamestanci
for i in range(len(pole_zamestanci)):
    #print pole_zamestanci[i][2]
    suma = suma + float(pole_zamestanci[i][2])
    suma_odmena = suma_odmena + float(pole_zamestanci[i][3])
print 'Prumerna mzda :' + str(suma / len(pole_zamestanci))
print 'Prumerna odmena:' + str(suma_odmena / len(pole_zamestanci))

