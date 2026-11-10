# ? operasi binary
# ? and or xor not
a=9
b=5

c=a|b
print("========or========")
print("nilai :",a,' binary: ',format(a,'08b'))
print("nilai :",b,' binary: ',format(b,'08b'))
print("_"*45)
print("========or========(|)")
print("nilai ",c,"binary ",format(c,"08b"))

#bitwise and &
c=a&b
print("========and========")
print("nilai :",a,' binary: ',format(a,'08b'))
print("nilai :",b,' binary: ',format(b,'08b'))
print("_"*45)
print("========or========(&)")
print("nilai ",c,"binary ",format(c,"08b"))

#bitwise xor ^
c=a^b
print("========xor========")
print("nilai :",a,' binary: ',format(a,'08b'))
print("nilai :",b,' binary: ',format(b,'08b'))
print("_"*45)
print("========xor========(^)")
print("nilai ",c,"binary ",format(c,"08b"))

#bitwise not ~
c=~a
print("========not========")
print("nilai :",a,' binary: ',format(a,'08b'))
print("nilai :",b,' binary: ',format(b,'08b'))
print("_"*45)
print("========not========(^)")
print("nilai ",c,"binary ",format(c,"08b"))
print("------------------------------------(xor)")
d=0b0000001001
e=0b1111111111
print("nilai : ",e^d," binary ",format(e^d,"08b"))

#shifting
#shift right (>>)
# todo geser ke kanan 1 kali
c=a>>1
print("========>>========")
print("nilai :",a,' binary: ',format(a,'08b'))
print("_"*45)
print("========xor========(>>)")
print("nilai ",c,"binary ",format(c,"08b"))
