from string import Template
nama='namaku jaka'
#satu line komenta
"""
multiline coments
"""
print(nama.lower())
print(nama.upper())
print(nama.title())
print("pembulatan pembagian ",12//5)
print(Template("modulus $modulus").substitute(modulus=5%2))
print(Template("pangkat $pangkat").substitute(pangkat=4**2))

#perbandingan
print(1==1)
print(1!=2)

for i in range(12):
    print(i)

def hoby(mood):
    if(mood.lower() == 'semangat'):
        print("koding")
    elif mood.lower() == 'muram' :
        print("bosen ngoding ah mending baca buku ajah")
    else:        
        raise TypeError("pilihannya hanya semangat atau muram")    
try:
    hoby("muram")
except KeyError as err:
    print(err)           
"""
parameter adalah placeholder untuk nilai yang ada didalam fungsi seperti parameter mood
kalau fungsi hoby dipanggil dan isi dari parameter diisi maka istilahnya berubah jadi argument
"""
#unlimited parameter
def buah(*list_buah):
    for buah in list_buah:
        print(buah)
buah("pir",'apple','jeruk','nangka')        
#default argumen
def greeting(name="katyusha"):
    list_guests=['jack','joko','lady miko','alex']
    if(name == 'katyusha'):
       print("halo lady ",name,' sama wellcome to our party')
    elif name=='alex':       
       print("halo and wellcome mr.",name)    
    elif not list_guests.__contains__(name):
        print("you are not our guest just get out in here!")   
        
 #index sekaligus element
buahs=['pir','apple','anggur']

for i,nilai in enumerate(buahs):
    print("index nilai ",i,nilai)
 

       