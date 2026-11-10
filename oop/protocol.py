from typing import Protocol
from abc import abstractmethod,ABC
# ? protocol bekerja seperti interface jika fungsi supperclass tidak akan protes jika fungsi method tidak di wariskan atau fungsinya dioveride karena python memiliki filosofi duck typing jika class bersuara seperti bebek maka dia adalah bebek
# ? protocol
class Human(Protocol):
    def __init__(self):
        pass
    def speak(self):
        print("default aisatsu")

class Jaka(Human):
    def __init__(self):
        pass
    # def aisatsu(self)->int:
    #     print("watashi jaka desu yoroshiku ne!!")
    #     return 1


jaka:Jaka=Jaka()
jaka.speak()