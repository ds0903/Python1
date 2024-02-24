import requests
import json
import time
start_time = time.time()

currency_exchange_base1 ={}
def info(from_="CHF",to_="CHF"):
    name_from=from_ #from 
    name_to=to_   #to  
    try:    #API connect
        API="JIJGS3BPJY3RYS4X"
        """Конвертація"""
        url = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={name_from}&to_currency={name_to}&apikey={API}"
        responce = requests.get(url) 
        EX=responce.json()
        kurs=EX["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
        currency_exchange_base1[name_from] = kurs #курс обміну по порядку з валюти до валюти

        file_name = "loging.json"
        log_info = responce.json()
        try:
            with open(file_name, "a") as a:
                a.write("\n")
                a.write(json.dumps(log_info))
                # print(log_info)
        except FileNotFoundError:
            with open(file_name, "w") as w:
                a.write("\n")
                w.write(json.dumps(log_info))
                # print("Файл успішно створений")
    except KeyError:
        print("No conection, try use new API or VPN")
        

def shotakoe_plus(self,other):
    currency1=self.currency
    currency2=other.currency
    info(currency1) 
    info(currency2)
    info(to_="USD")
    plus1,plus2 = 0,0
    for key1,value1 in currency_exchange_base1.items():
            if self.currency == key1:
                plus1 =  self.value * float(value1)
    for key2,value2 in currency_exchange_base1.items():
            if other.currency == key2:
                plus2 = other.value * float(value2) 
                p_1 = plus1 + plus2
    for key3,value3 in currency_exchange_base1.items():
        if key3 == "USD":        
            p_2 = p_1 * float(value3) #CHF to USD
    return f"Різниця валют переведених в Доларах США {p_2} "

def shotakoe_minus(self,other):
    currency1=self.currency
    currency2=other.currency
    info(currency1) 
    info(currency2)
    info(to_="USD")        
    minus1,minus2 = 0,0
    for key1,value_1 in currency_exchange_base1.items():
        if self.currency == key1:
            minus1 =  self.value * float(value_1)
    for key2,value_2 in currency_exchange_base1.items():
        if other.currency == key2:
            minus2 = other.value * float(value_2) 
            m_1 = minus1 - minus2 
    for key3,value_3 in currency_exchange_base1.items():
        if key3 == "USD":        
            m_2 = m_1 * float(value_3) #CHF to USD
    return f"Різниця валют переведених в Доларах США {m_2} "

class Price:
    def __init__(self, value: int, currency: str) -> None:
      self.value: int = value
      self.currency: str = currency
        
    def __add__(self,other) -> 'Price':
        
        if self.currency == other.currency:
            return f"Сумма {self.value + other.value}, В валюті {self.currency}"
        elif self.currency != other.currency:
            return shotakoe_plus(self,other)

    def __sub__(self,other) -> 'Price':

        if self.currency == other.currency:
            return f"Різниця {self.value - other.value}, В валюті {self.currency}"
        elif self.currency != other.currency:
            return shotakoe_minus(self,other)

flight = Price(2000, "USD")
hotel = Price(1000, "EUR")
oleg = flight-hotel
print(oleg)
end_time = time.time()
execution_time = end_time - start_time
print(f"Програма зайняла {execution_time} секунд твого часу")    