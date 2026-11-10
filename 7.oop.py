import string
import datetime
data={
    'name':'jaka'
}
print('nama testing ','name' in data )
class Human:
    def __init__(self,name:str,sex:str):
        self.name=name
        self.sex=sex

    def __str_template(self,msg,props)->str:
        return string.Template(msg).substitute(props)
   
    def aisatsu(self,time):
        clocks=datetime.datetime.now()
        now_clock=clock.hour
        tanggal=now_clock.date()
        waktu=now_clock.time()
        type_time={
            'asa':now_clock>1 or now_clock<8,# ? pagi
            'siang':now_clock>8 or now_clock>=12,# ? siang
            "konban":now_clock>=15 and now_clock<18, # ? sore
            "yoru": now_clock>=18 and now_clock<1# ? malam
        }
        aisatsu_msg:str=""
        if type_time['asa']:
            aisatsu_msg=self.__str_template(msg='gutto morningu $name chan sama',props={'name':self.name})
        if type_time['siang']:
            aisatsu_msg=self.__str_template(msg="konichiwa watashi no $waifu chan kyou wa utsukushi ne $waifu chan",props={'waifu':"makima"})
        if type_time['konban']:
            aisatsu_msg=self.__str_template(msg="konbanwa watashi no $waifu chan kyou wa utsukushi ne $waifu chan",props={'waifu':"makima"})
        if type_time['yoru']:
            aisatsu_msg=self.__str_template(msg="konbanwa watashi no $waifu chan kyou wa utsukushi ne $waifu chan",props={'waifu':"makima"})
        print(aisatsu_msg) 
    
    def simple_condition(self)->bool:
        # ? for documentation like jsdocs
        """ simple condition for simple sintaks if else
            :param self : mirip seperti js this
            :type self: none
            :return: bool
            :rtype: bool
        """
        condition={
            'male':[True] ,
            'female':[True]
        }
        if self.sex not in condition:
            print("error must be male or female")
            return False
        return condition[self.sex][0]

    def get_message(self)->None:
        sexs={
            'male':'you are male',
            'female':string.Template('you are female ohayou $waifu chan sama').safe_substitute({'waifu':self.name})
        }

        is_male=self.sex.lower() in sexs
        if not is_male: print("error")
        print(sexs[self.sex])

jaka:Human=Human(name="jaka",sex='male') 
is_male=jaka.simple_condition()
print(is_male)
if is_male : jaka.get_message()

even_numb="even" if 10%2==0 else 'odd'
print(even_numb)            

datas={
    'benar':print("sekai desu"),
    'hampir_benar':print("chotto chigaimasu desu"),
}

matching='benar'
datas[matching] if matching in datas else print("error")


def hitung_pajak(harga: float, diskon: float = 0.0) -> float:
    """Menghitung total pajak dari harga barang setelah diskon.

    :param harga: Harga asli barang sebelum diskon.
    :type harga: float
    :param diskon: Persentase diskon (0.0 - 1.0), defaults to 0.0
    :type diskon: float, optional
    :returns: Total nilai pajak yang harus dibayar.
    :rtype: float
    """
    return (harga - (harga * diskon)) * 0.11


hitung_pajak(12.2,0.1)