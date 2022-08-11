from calculateAbstract import CalculateBase
import math

class Calculate(CalculateBase):
    def __init__(self) -> None:
        print("1-Toplama\n2-Cikarma\n3-Carpma\n4-Bolme\n5-Mod\n6-Logaritma")
        self.islem=int(input("İslem seciniz: "))
        if self.islem ==6:
            self.a=float(input("Lutfen sayi giriniz: "))
        else:
            self.a = float(input("Birinci degeri giriniz: "))
            self.b = float(input("İkinci degeri giriniz: "))  
        if self.islem==1:
            print(self.add())
        elif self.islem==2:
            print(self.substract())
        elif self.islem==3:
            print(self.multiply())
        elif self.islem==4:
            print(self.divide())
        elif self.islem==5:
            print(self.mod())
        elif self.islem==6:
            print(self.logarithm())
        else:
            print("gecersiz deger")
    def add(self):
        valid_instance_types = (int, float)
        if isinstance(self.a,valid_instance_types) and isinstance(self.b,valid_instance_types):
            if self.a > 0 and self.b > 0:
                return f"Sayilarin toplami {self.a+self.b} ..."
            else:
                return "Pozitif sayi giriniz..."
            
        
        else:
            return "Gecerli bir sayi giriniz..."
    
    def substract(self):
        valid_instance_types= (int,float)
        if isinstance(self.a,valid_instance_types) and isinstance(self.b,valid_instance_types):
            if self.a>0 and self.b>0:
                return f"cikarma sonucu {self.a-self.b}"
            else:
                return "Pozitif sayi giriniz..."
        else:
            return "Gecerli bir sayi giriniz..."
        
    
    def multiply(self):
        valid_instance_types= (int,float)
        if isinstance(self.a,valid_instance_types) and isinstance(self.b,valid_instance_types):
            if self.a>0 and self.b>0:
                return f"Carpma sonucu {self.a*self.b} ..."
            else:
                return "Pozitif sayi giriniz..."
        else:
            return "Gecerli bir sayi giriniz..."
    def divide(self):
        valid_instance_types= (int,float)
        try:
            if isinstance(self.a,valid_instance_types) and isinstance(self.b,valid_instance_types):
                if self.a>0 and self.b>=0:
                    return f"Bolme sonucu {self.a/self.b} ..."
                else:
                    return "Pozitif sayi giriniz..."
            else:
                return "Gecerli bir sayi giriniz..."
        except ZeroDivisionError:
            return "0'a bolemezsiniz"
            
    def mod(self):
        valid_instance_types= (int,float)
        if isinstance(self.a,valid_instance_types) and isinstance(self.b,valid_instance_types):
            
            if self.a>0 and self.b>0:
                return f"Sayilarin modu {round(self.a%self.b)} ..."
            else:
                return "Pozitif sayi giriniz..."
        else:
            return "Gecerli bir sayi giriniz..."
        
    def logarithm(self):
        valid_instance_types= (int,float)
        if isinstance(self.a,valid_instance_types):
            if self.a>0:
                return f"Sayinin logaritmasi {math.log10(self.a)} ..."
            else:
                return "Pozitif sayi giriniz..."
            
        else:
            return "Tam sayi giriniz..."
        
        
       
            
        
        
    
        
    