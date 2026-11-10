print('\nprogram konversi tempratur\n')
celcius=float(input('masukkan suhu dalam celcius'))
print('suhu adalah ',celcius,' celcius')

reamur=(4/5)* celcius
print('suhu adalah ',reamur,' reamur')

farenheit=((9/5)*celcius)+32
print('suhu adalah ',farenheit,' farenheit')

kelvin=celcius+273
print('suhu adalah ',kelvin,' kelvin')
# ? FARENHEIT KE KELVIN
print("frenheit ke kelvin")
farenheit=float(input("masukkan suhu farenheit "))
kelvin=(farenheit-32)*(5/9)+273.15
print("suhu dalam kelvin : ",kelvin)
# ? kelvin ke farenheit
kelvin=float(input("masukkan suhu kelvin "))
kelvin_to_farenheit=(kelvin-273.15)*(9/5)+32
print("suhu kelvin to farenheit : ",kelvin_to_farenheit)
