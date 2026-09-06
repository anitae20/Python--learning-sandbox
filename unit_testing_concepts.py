from abc import ABC,abstractmethod
#abc is abstract base class


#class house should inherit things from abc


class House(ABC):
    @abstractmethod   #as soon as you do absract function the method below becomes abstract method 
    def BuilderDoor(self):
        print('Door is built in House')

    def BuildWindow(self):
        print("Window is built in the house")


class SmallHouse(House):
    def BuilderDoor(self):
            print('Door is built in small House')
    
    def BuildWindow(self):
            print("Window is built in the Small house")

class BigHouse(House):
    def BuilderDoor(self):
            #print('Door is built in Big House')
        super().BuildDoor
    def BuildWindow(self):
                print("Window is built in  the Big house")


smallHouse = SmallHouse()
smallHouse.BuilderDoor()
smallHouse.BuildWindow()

bighouse = BigHouse()
bighouse.BuildWindow()
bighouse.BuilderDoor()