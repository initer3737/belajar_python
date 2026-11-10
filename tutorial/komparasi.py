# ? >,<, >=, <=, != ,==, is, not
print("java" == "java")
is_sintaks='membandingkan object'
#is sebagai komparasi object
x=5 # ini adalah object
y=5 # ini adalah object
print(x is y)
memori=hex(id(y))
print(memori)
# ? not or and xor
# ? not is to negate from false to true and vice versa
# ? or jika salah 1 true maka dia true,jika keduanya false maka false
# ? and jika keduanya true maka dia true,jika ada 1 false maka false
# ? xor jika true, maka salah satu true sisanya false
# ? xor salah satu aja yang true maka true jika keduanya true maka false
# ? xor hanya bisa true selagi kedua nilai yang dibandingkan berbeda false ^ true == true  
a=False
b=False
c=a or b
print(a,'or',b,'=',c)

a=True
b=True
c=a and b
print(a,'and',b,'=',c)
# ? dia akan true jika komparasinya adalah true ^ false jika nilainya sama maka dia false
a=False
b=True
c=a ^ b
print(a,'xor',b,'=',c)

waifus:list=['megumin','aqua','yukinoshota yukino']
age=12
waras=True
is_okay_to_have_waifu=(age >=16) ^ waras

if is_okay_to_have_waifu:
    print("you dont deserve to get waifu wangy-wangy all waifus is mine ",waifus)
# ? masukkan angka angka lalu di logikakan dengan true atau false
inputUser = float(input("masukkan angka:"))
a = (inputUser > 0)
b = (inputUser < 5)
c = (inputUser > 8)
d = (inputUser < 11)

isCorrect = (a and b) or  (c and d)
print("angka yang anda masukkan :", isCorrect)

print("\n",20*"=","\n")
inputUser = float(input("masukkan angka:"))

a = (inputUser > 5)
b = (inputUser < 0)
c = (inputUser > 11)
d = (inputUser < 8)

isCorrect = (b or a) and (d or c)
print("angka yang anda masukkan :", isCorrect)
