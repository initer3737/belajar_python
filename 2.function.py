list_jajans=['marimas',['jajan',['jajan2'],'japanable',['japanese','jaka']]]
list_found=[]
def deep_search(datas,search):
    if(isinstance(datas,list)):
        for data in datas:
            if deep_search(data,search):
                return True
    elif(isinstance(datas,str)):return search in datas
    return False
if(deep_search(list_jajans,'ja')):
    print("data valid")
else:
    print("data tidak ditemukan")    

def searching(datas,keyword):
    #kalau dia adalah array
    if isinstance(datas,list):
        for data in datas:
            searching(data,keyword)
    # kalau dia adalah str 
    if isinstance(datas,str):
        if keyword in datas:
            list_found.append(datas)
searching(list_jajans,'ja')
print("found ",list_found)
     #belajar recursion untuk melakukan deep search atau pakai itu untuk algoritma search  
def recursive_math(num):
    if(num == 1):
        return num
    else:
       return num*recursive_math(num-1)
print(recursive_math(5)) 



urutan=[0,1,4,5,2]    

def buble_short(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            nilai_saat_ini=arr[j]
            nilai_selanjutnya=arr[j+1]
            if(nilai_saat_ini>nilai_selanjutnya):#12 3
                arr[j+1],arr[j]=nilai_saat_ini,nilai_selanjutnya#3,12=12,3
    return arr     

print(buble_short(urutan))               
      