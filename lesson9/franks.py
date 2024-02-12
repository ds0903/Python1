
currency_exchange_base1 ={
    # "USD":1.14, 
    # "UAH":42.99, #Список курсів наших валют в CHF(Швейцарский франк)
    # "EUR":1.06,  
    "CHF":2

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
            for key,value_CH in currency_exchange_base1.items():
                #if key == "CHF": 
                    return f"Сума переведених в Франки валют {self.value / value_CH + other.value / value_CH} ФРАНКІВ"


    def __sub__(self,other) -> 'Price':
        if self.currency == other.currency:
            return f"Різниця {self.value - other.value}, В валюті {self.currency}"
        elif self.currency != other.currency:        
            for key,value_CH in currency_exchange_base1.items():
                #if key == "CHF": 
                    return f"Різниця переведених в Франки валют {self.value / value_CH - other.value / value_CH} ФРАНКІВ"

flight = Price(2000, "UAH")
hotel = Price(1000, "UAH")
result = flight+hotel
print(result)
