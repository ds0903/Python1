
currency_exchange ={
    "currency_USD":{"USD":1.14}, 
    "currency_UAH":{"UAH":42.99}, #Список курсів наших валют в CHF(Швейцарский франк)
    "currency_EUR":{"EUR":1.06},  
    "currency_CHF":{"CHF":1} 
    

}

class calc: 
    def __init__(self, value: int, currency: str, currency_exchange) -> None:
      self.value: int = value
      self.currency: str = currency
      self.currency = currency_exchange

    def __truediv__(self,other):
        """Переводимо всі наші валюти в Швейцарский франк"""
        if self.currency == "UAH":
            for key,value_U in currency_exchange.items():
                if key == "currency_UAH":
                    for value_UAH in value_U.values():
                       return self.value / value_UAH
        if self.currency == "USD":
            for key,value_US in currency_exchange.items():
                if key == "currency_USD":
                    for value_USD in value_US.values():
                       return  self.value / value_USD
        if self.currency == "EUR":
            for key,value_EU in currency_exchange.items():
                if key == "currency_EUR":
                    for value_EUR in value_EU.values():
                       return  self.value / value_EUR
        if self.currency == "CHF":
            for key,value_CH in currency_exchange.items():
                if key == "currency_CHF":
                    for value_CHF in value_CH.values():
                       return self.value / value_CHF        
        else:   
            raise TypeError("ERROR!!! not supported currency")             

class Price(calc):
    def __init__(self, value: int, currency: str) -> None:
      super().__init__(value, currency, None)
      self.value: int = value
      self.currency: str = currency

    """Тепер додаємо та віднімаємо вже в Швейцарский франках"""

    def __add__(self,other) -> 'Price':

        return self.value + other.value, self.currency

    def __sub__(self,other) -> 'Price':
        return self.value - other.value, self.currency


flight = Price(2000, "USD")
hotel = Price(1000, "UAH")
taxi = Price(100,"EUR")

divided_flight = flight / flight
divided_hotel = hotel / hotel   #Проводимо операцію з перерахування всіх валют в Швейцарські франки
divided_taxi = taxi / taxi

result_plus = divided_flight + divided_hotel + divided_taxi #тепер додаємо та віднімаємо наші результати в Швейцарських франках
result_minus = divided_flight - divided_hotel - divided_taxi

print(f"Результат переведення валют до Швейцарського франка:\n(Квитки на літак) {divided_flight}\n(Номер в готелі) {divided_hotel}\n(Ціна на таксі) {divided_taxi}")
print(f"Результат додавання всіх послуг {result_plus}\nА також результат віднімання {result_minus}")
print("ЦІНИ ВКАЗАНІ В ШВЕЙЦАРСЬКИХ ФРАНКАХ!")