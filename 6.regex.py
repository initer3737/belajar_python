import re

sintaks = 'select price , name from products where id is 12 group by type'
# ? kalau tanpa , dia akan jadi string dan akan diconcate oleh python
# ? kalau ada , maka dia adalah tuple 
regex_pattern = (
    r"(select)\s+"
    r"([\w\s,]+?)\s+"             
    r"(from)\s+"
    r"(\w+)\s*"                   
    r"(?:(where)\s+([^\n]+?))?\s*"    
    r"(?:(group\s+by)\s+(\w+))?$"  
)

datas = re.findall(pattern=regex_pattern, string=sintaks, flags=re.IGNORECASE)
print(datas)