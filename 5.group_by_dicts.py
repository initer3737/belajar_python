# birth_years=[2002]
datas=[
    {'name':'yukinoshita yukino chan','age':20, 'role':'designer'},
    {'name':'yui','age':20 ,'role':'designer'},
    {'name':'zura','age':19 ,'role':'web developer'},
]
grouped={}
# todo grouped harus dibikinkan keynya misal gruped['age]=[]
for data in datas:
    if isinstance(data,dict):
        key=data['role']
        if not key in grouped:
            grouped[key]=[]
    grouped[key].append(data)      

print(grouped)            