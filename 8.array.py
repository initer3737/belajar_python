arr=[12,2,2,4,6]

genap_semua=all(x%2==0 for x in arr)
lebih_dari_9_atau=any(x>=9 for x in arr)
print(genap_semua)
print(lebih_dari_9_atau)

image=[]
image.append("jk.png")

print('image ',image)

for idx,data in enumerate(arr):
    print(f"idx:{idx} data:{data}") 