currency_exchange_base1 ={
     "USD":1.14, 
     "UAH":42.99, #Список курсів наших валют в CHF(Швейцарский франк)
     "EUR":1.06,  
     "CHF":1

}
       

class Price:
    def __init__(self, value: int, currency: str) -> None:
      self.value: int = value
      self.currency: str = currency
      self.currency_base = currency_exchange_base1
        

    def __add__(self,other) -> 'Price':
        if self.currency == other.currency:
            return f"Сумма {self.value + other.value}, В валюті {self.currency}"
        elif self.currency != other.currency:
      
            for key1,value1 in currency_exchange_base1.items():
                if self.currency == key1:
                    plus1 =  self.value / value1
            for key2,value2 in currency_exchange_base1.items():
                if other.currency == key2:
                    plus2 = other.value / value2 
                    return f"Сума переведених в Франки валют {plus1 + plus2} ФРАНКІВ"


    def __sub__(self,other) -> 'Price':
        if self.currency == other.currency:
            return f"Різниця {self.value - other.value}, В валюті {self.currency}"
        elif self.currency != other.currency:
      
            for key1,value1 in currency_exchange_base1.items():
                if self.currency == key1:
                    minus1 =  self.value / value1
            for key2,value2 in currency_exchange_base1.items():
                if other.currency == key2:
                    minus2 = other.value / value2 
                    return f"Різниця переведених в Франки валют {minus1 - minus2} ФРАНКІВ"

flight = Price(2000, "USD")
hotel = Price(1000, "UAH")
oleg = flight+hotel
print(oleg)
