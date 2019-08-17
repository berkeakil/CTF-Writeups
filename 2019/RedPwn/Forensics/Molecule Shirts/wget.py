import os

file = open("molecules","r")
for line in file:
    uri= "http://www.molecularshirts.com/wp-content/themes/poza-child/images/names/"+line[:-1]+".jpg"
    os.system("wget "+uri)
