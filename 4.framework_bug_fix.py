from string import Template
import re  
"""
todo pecahkan problem dengan algoritma
  agar mudah dalam mengerjakan soalnya
 ==========================
 1. bikin variable penampung lalu jadikan keduanya sebagai list agar kita bisa mudah 
 mengambil data berdasarkan indexnya
2.buat jadi fungsional atau module-module
3.search in db based on params with logic and
4.implementing deep search
"""
path="product/:id"
data_product_request="product/4"
def convert_to_object_and_get_datas(data_product_request,path):
    data_product_regexs=re.findall(':\\w+',path)
    data_products={}
    list_data_path=path.split('/')
    data_product_list=data_product_request.split("/")
    for data in data_product_regexs:
        data_cleaning_coma=data.replace(":","")
        data_products[data_cleaning_coma]=data_product_list[list_data_path.index(data)]
    return data_products
# kriteria_query_sql={'select':'id,name',filters:'where id=4'}
# query_sql=Template("select $select from $table $filters").substitute(kriteria_query_sql)                
database_shops=[
    {'meta':{'db_table':"products"}},
    {"id":1,'name':"rolex",'price':12_000,'type':"pakaian" },
    {"id":2,'name':"ssd 1 tb",'price':12_500,'type':"electronic"},
    {"id":3,'name':"ram 8gb",'price':12_700,'type':"electronic"},
    {"id":4,'name':"clothes",'price':12_950,'type':"pakaian"},
]


get_data_params=convert_to_object_and_get_datas(data_product_request=data_product_request,path=path)
# todo util for deepsearch
# todo gunakkan logika and dengan menunpack key dan value
# todo gunakkan pencarian id 4 in key value
# todo buat jadi error jika key yang dicari tidak di mention misal 
# todo ids maka eror karena key tidak ada di database
data_found=[]
def deepsearch(keyword,datas):
    if isinstance(datas,dict):
        for key,val in datas.items():
            if deepsearch(keyword=keyword,datas=(key,val)):return True
    if isinstance(datas,list):
        for data_str in datas:
            if deepsearch(keyword=keyword,datas=data_str):return True 
    if isinstance(datas,tuple):
            for data in datas:
                # print("tupple level",data)
                if deepsearch(keyword=keyword,datas=data):return True             
    if isinstance(datas,str):
        return keyword in datas                
    if isinstance(datas,int):
        return keyword in str(datas)                
    return False    
# ? and logic
def and_logic_param(params,datas):
    # ? param id:4
    if isinstance(params,dict):
        for key,value in params.items():
            # ! jika key tidak ada
            if key not in datas:raise KeyError("error key tidak ditemukan")

       # ? jika value tidak ditemukan
        if not deepsearch(keyword=str(value),datas=datas[key]):return False
       # ? jika value ada dan key ada 
        return True 

def raw_sql(sql_query,datas,table_name):
    is_error=False
    # ! bug kalau ada spasi di selected field maka akan error example error{name ,price,type}
    sintaks='select name,price,type from products group by type'
    pattern=(
        # ? ?i flag i di regex 
        r"(?i)\b(\w+)\b\s+([*,\w\s]+?)\s+"     # ? 1 & 2: select dan kolom
        r"\b(from)\b\s+([\w]+)\s*"                 # ? 3 & 4: from dan nama tabel (hanya nama tabel)
        r"(?:\b(where)\b\s+([^group]+))?\s*"             # ? 5 & 6: where dan kondisinya , memilih field key dari dict yang akan ditampilkan ke user
        r"(?:\b(group\s+by)\b\s+(\w+))?"
    )
    validate_sql_sintaks=re.findall(pattern=pattern,string=sintaks,flags=re.IGNORECASE)[0]
    print("test ",validate_sql_sintaks)
    # ! check for sequence group by itu optional
    # ? agar terurut select di index 0 2 dst
    # ! check for non regex sintaks ex:select where etc apakah sesuai urutan 
    # ? select from where group by    
    # ! check for error
    select_sintak=validate_sql_sintaks[0]
    selected_field_sintak=validate_sql_sintaks[1]
    from_sintak=validate_sql_sintaks[2]
    group_by_sintak=validate_sql_sintaks[-1]
    # todo matching the table name
    # todo selected field sintaks if * exist but user with comma , show the error
    pattern_selected_field=(
            r"[a-zA-Z,]+"
        )
    select_all_sintak_pattern=(
        r"[\*]+"
    )   
    # ? kalau ada * dan select field ada  maka error
    # ! validate potensi error
    # ? 
    ada_select_star=bool(re.search(pattern=select_all_sintak_pattern,string=sintaks,flags=re.IGNORECASE)) 
    ada_select_multiple=bool(re.search(pattern=pattern_selected_field,string=sintaks,flags=re.IGNORECASE)) 
    if '*' in selected_field_sintak:
        datas=datas     
    if ('*' in selected_field_sintak ) and (',' in selected_field_sintak):
        is_error=True
        err_message="select must be * or selected columns"
        # todo regex dibawah untuk check apakah * dan selected field 
        # ? select * ada dan (select * dan select fields tidak ada)    
    if bool(re.search(flags=re.IGNORECASE,pattern=pattern_selected_field,string=sintaks) and not (ada_select_multiple and ada_select_star)):
        print("salam ahoi ")
        _selected_feield={}
        # todo check selected field!! 
        # todo split jadi list lalu skip beberapa key dicts yang diskip
        # ? yang tidak dipilih harus diskip/continue
        selected_fields=re.findall(flags=re.IGNORECASE,pattern=pattern_selected_field,string=sintaks)[1].split(",")
        print("permisi bang ",selected_fields )
        # ! todo perlu pengecekan every di python @skiping_field 
        # ! kalau field yang diselect tidak ada didalam datas
        # ! kalau select field tidak ada , maka tambahi comma agar bisa dijadikan list
        data_keys=list(datas[0].keys())
        print("selected fields ",selected_fields)
        print('converted to list ',data_keys)
        print('checks datas ',datas)

        skiping_field=all(data in datas[0] for data in selected_fields )#selected_fields in datas
        print("chekibngs ",skiping_field)
        # ? kalau skipping field or selected field is not match 
        if skiping_field == False:
            err_message="error selected field is not match"
            is_error=True
        # todo field is match or data key of dict is exist in data
        # todo and do skipping
        if skiping_field == True :
            skiped_data=datas[0]
            reformat_data:list=[]
            dicts_reformat={}
            for key,data in skiped_data.items():
                # ? kalau tidak ada fieldnya maka skip
                if key not in selected_fields:
                   continue
                dicts_reformat[key]=data    
            print('skipping ----')    
            print("skiping field ",dicts_reformat)
            reformat_data.append(dicts_reformat)
            datas=reformat_data
            if group_by_sintak not in datas[0]:
                err_message=f"error {group_by_sintak} not found in {datas}"
                is_error=True

            # datas=reformat_data
            # print("completed data processing ",datas)
            # print("testing jk ",dicts_reformat)
            # print("type datanya apa ",type(reformat_data)," reformat data isinya ",reformat_data)
            # print("testing jk data ",datas)
    table_name_compare=validate_sql_sintaks[3]
    if table_name_compare.lower()!=table_name.lower():
        is_error=True 
        err_message="table name doesnt exist"
    if select_sintak.lower() != "select".lower():
        is_error=True
        err_message='only select is available in sql look alike'
    if from_sintak.lower() != "from".lower():
        is_error=True
        err_message='from is required in sql look alike'
    grouped={}
    if "group by" in sintaks:
        key=group_by_sintak
        # validate=datas[0]['type']
        # print(validate)
        # ? group by type not in table
        for data in datas:
            if key not in data:
                is_error=True
                # print("checking for adatas ",datas)
                # print("checking for key ",key)
                err_message=Template('error column $column is not in table').safe_substitute({'column':key})
            if is_error ==  True:break
            print("datas db ",data)
            data_key=data[key]
            if  data_key not in grouped:grouped[data_key]=[]
            grouped[data_key].append(data)
    print("ini grouped ",grouped)
    if is_error== True: raise TypeError(err_message)       
try:            
    get_table_name=[]
    for datas in database_shops:
        # todo ambil nama tbl name
        if('meta' in datas):
            get_table_name.append(datas['meta']['db_table'])
            continue
        if and_logic_param(params=get_data_params,datas=datas):
            data_found.append(datas)
            # ? data found itu mengembalikan data dengan field penuh belum 
            # ? di filter dengan query sql misal hanya select id dan name aja
    tabel_name=get_table_name[0]        
    raw_sql_query=raw_sql(sql_query="select * from products",datas=data_found,table_name=tabel_name)
    print(raw_sql_query)
    print("data tabel adalah "+get_table_name[0])
except TypeError as err:
    print("error 405 sql sintaks")        
    print(err)        

