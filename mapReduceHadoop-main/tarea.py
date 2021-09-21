f = open("wordcountFile", "r")
respuesta=f.read()
respuesta=respuesta.upper()
print(respuesta)
print("split Linea")
respuesta=respuesta.replace("\n"," ")
bien=""
for i in respuesta:
    if( i.isalpha() or i==" "):
        bien+=i
print(bien)
bien=bien.split(" ")
bien2=[]
for i in bien:
    if(i!=" " or i!="" or i!="\n"):
        bien2.append(i)
        print(i)
palabras={}
while(True):
    if(bien[0] in palabras):
        palabras[bien[0]]+=1
    else:
        palabras[bien[0]]=1
    del bien[0]
    if(len(bien)==0):
        break
print("FINAL  ----------------")
print(palabras)