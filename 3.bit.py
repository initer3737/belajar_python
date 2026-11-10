#bitwise
#[v]program untuk konversi bilangan desimal ke biner dan sebaliknya
#[v]bikin mdule berbasis callback atau fungsi sebagai argument dengan opsi terakhir 
# menampilkan bilangan desimal ataukah biner 
#[v]args 1 sebagai bilangan desimal ke 1 dan args 2 juga desimal kalau dia biner maka throw error
#[v]args 3 sebagai penentu operaasi ^[xor] &[and] |[or] ~[not] dalam bentuk callback
#[v]args 4 sebagai penentu hasilnya berupa bit ataukah desimal
"""
    almost done try manual and play with for loops 
logika xor ^ (exclusive or)
kalau beda itu 1 kalau sama itu 0 misal 1 ^1 itu 0 1^0 itu 1
true dan true 0 false 
false dan true 1 true 
logika &
dikonversi ke biner lalu dibandingkan jika 0 dan 0 maka 0 jika 1 dan 1 maka 1 jika 1 dan 0 maka 0
kalau perbandingannya sama berarti true atau 1 kalau tidak sama maka false atau 0
true dan true maka true 
true dan false maka false
"""
"""
tulis program untuk konversi desimal ke bit 
aturan 8 bit
dibagi 2 lalu ditulis dari belakang ambil sisa bagi untuk angka bitnya diambil dari 
belakang untuk jadi bilangan bit 
6/2 == 3 sisa 0 ,3/2== 1 sisa 1,1/2 0 sisa 1  
110
dikonversi biner ke desimal itu dari digit paling kanan ke kiri dikali 2 pangkat x 
x adalah isi dari index  ,mulai dari 0
"""

#ini akan di reverse untuk mengetahui nilai dari bit karena dibaca dari kanan ke kiri
desimal_num=6
rule_bit=8
bit_nums=[]
#kalkulasi dari desimal ke bit,menghasilkan nilai bit dan nilai terusan yang akan 
# digunakkan untuk kalkulasi berikutnya
# kalkulasi di dalam while loop akan menghasilkan modulo yang akan dijadikan angka bitnya
# angka kalkulasi terusan akan disimpan di temp file
is_over=False
while True:
    bit_nums.append(desimal_num%2)
    desimal_num=desimal_num//2
    if desimal_num <1:is_over=True
    if is_over == True:
        break
bit_nums.reverse()#reverse
if rule_bit ==8:
    while len(bit_nums) < rule_bit:
        bit_nums.insert(0,0)    
    # print("".join(str(digit) for digit in bit_nums) )
# print(bit_nums)    
#tulis program untuk konversi bit ke desimal
bilangan=0
bit_num_reversed=bit_nums[::-1]
for idx,bit in enumerate(bit_num_reversed):
    bilangan+=bit*(2**idx)

# print(bilangan)   
def desimal_to_bit(num,cb):
    if not isinstance(num,int):raise TypeError("num arg harus integer")
    num=num
    bit_numeric=[]
    is_finish=False
    while True:
        num=num//2
        bit_numeric.append(num%2)
        if(num<1):is_finish=True
        if(is_finish):break
    cb(bit_numeric)     

# desimal_to_bit(6,lambda bit_result:print(bit_result))
# woilah callback hell cik
def calculate(arg1,arg2,cb,type):
    if not isinstance(arg1,int):
        raise TypeError('arg1 harus integer')
    elif not isinstance(arg2,int):
        raise TypeError('arg2 harus integer')
    if type.lower()=='bit':
        #desimal convert to bit 
         bit_numeric=cb(arg1,arg2)   
         desimal_to_bit(bit_numeric,lambda res:print(res))
    elif type.lower()=='desimal':
        #jadi desimal         
        print(cb(arg1,arg2))
# calculate(12,13,lambda a,b:a&b,'desimal')   

# print("validate 12&13 ",12&13)
"""
and &
or |
negate ~
xor ^
"""
def and_bitwise(number_bit_1,number_bit_2):
    if not isinstance(number_bit_1,str):raise TypeError("arg number_bit_1 must be string")
    if not isinstance(number_bit_2,str):raise TypeError("arg number_bit_2 must be string")
    data_bit1=[]
    data_bit2=[]
    bit_baru=[]
    length_str_bit1=len(number_bit_1)
    length_str_bit2=len(number_bit_2)
    for bit1 in range(length_str_bit1):
     data_bit1.append(number_bit_1[bit1])
    for bit2 in range(length_str_bit2):
     data_bit2.append(number_bit_2[bit2])
    # ?  logika dan jika keduanya sama maka sama 1&1 ===1
    # ! bug jika data dalam array bit 1 dan 2 jika tidak punya panjang yang sama maka data for loops harus ambil panjang yang paling panjang agar program for loop 
    # ! tetap bisa jalan 
    # ! operasi perbandingan dijalankan dari paling kanan ke kiri maka kedua bit perlu di reverse
    # ! bit baru juga di reverse untuk menunjukkan bit sebenarnya
    # todo : ketika bit baru telah berisi nilai bit dia dalam keadaan terbalik dan perlu di reverse
    # todo : sebelum direverse 011[bukan bit sebenarnya] setelah direverse 110[bit sebenarnya]
    # ? kenapa di reverse ? karena di perulangannya dari index ke 0 yakni dari paling
    # ? kiri ke kanan perulangan paling kecil ke paling besar
    # ? jadi operasinya akan memeriksa bit paling kiri sedangkan operasi perbandingannya dari paling kanan makanya perlu direverse 
    # ? agar operasinya dimulai dari index paling kiri [untuk ngakalin programnya]
    # ! program ini hanya menunjukkan cara kerja dari operasi biner xor or and  negate
    # ! program ini sengaja dibikin ngebug karena admin gak tahu cara fixingnya
    perbandingan={
        'bit1':len(data_bit1),
        'bit2':len(data_bit2)
    }
    data_bit1.reverse()
    data_bit2.reverse()
    number_bit_1_reversed=data_bit1
    number_bit_2_reversed=data_bit2
    if(perbandingan['bit1']>=perbandingan['bit2']):
        for bit1_idx in range(perbandingan['bit1']):
            try:
             if number_bit_1_reversed[bit1_idx] =='1' and number_bit_2_reversed[bit1_idx]=='1':
                # todo kalau sama maka dia true misal 1==1 hasilnya 1
                bit_baru.append(number_bit_1_reversed[bit1_idx])
             else:
                # todo kalau beda 1==0 maka hasilnya 0
                bit_baru.append(0)
            except IndexError:
               # ! kalau bit 2 null atau kosong maka ambil bit1 karena perbandingannya sudah out bit1=1110 & bit2=110
               bit_baru.append(number_bit_1_reversed[len(number_bit_1_reversed)-1])       

    if(perbandingan['bit1']<perbandingan['bit2']):
        print("oke bit 2")
        for bit2_idx in range(perbandingan['bit2']):
            try:
             if number_bit_1_reversed[bit2_idx] == '1' and number_bit_2_reversed[bit2_idx] == '1':
                # todo kalau sama maka dia true misal 1==1 hasilnya 1
                bit_baru.append(number_bit_1_reversed[bit2_idx])
             else:
                # todo kalau beda 1==0 maka hasilnya 0
                bit_baru.append(0)
            except IndexError:
               # ! kalau bit 2 null atau kosong maka ambil bit1 karena perbandingannya sudah out bit1=1110 & bit2=110
               # ! ambil yang terakhir 
               bit_baru.append(number_bit_2_reversed[len(number_bit_2_reversed)-1])
    bit_baru.reverse()           
    print(bit_baru)           

try:
    number_bit_1='110'
    number_bit_2='1110'
    and_bitwise(number_bit_1,number_bit_2)
except KeyError as err:
    print(err)