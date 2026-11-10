hero={
    'name':'phantom assassin',
    'level':25,
    'rank':'mmr',
    'type':'carry'
}
dicari='level'
keys,_=zip(*hero.items())
print("my hero ",hero.keys())
dicarikan=any(dicari in key for key in keys)
print('dicarikan ',dicarikan)
name,level,rank,type=hero.values()
# print(keys,val)
key_hero,value_hero=zip(*hero.items())
for key,val in hero.items():
    print(key,val) 
print(name,level,rank,type)
# ? spill doksli
#https://www.geeksforgeeks.org/python/python-unpack-dictionary/