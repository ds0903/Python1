import requests,json,time
start_time = time.time()

currency_exchange_base1 ={'CHF': '1'}
exchange_CHF_to_USD ={}
currency_exchange_base1 ={}
try:    #API connect
    API="JIJGS3BPJY3RYS4X"
    """Долари в Франки"""
    url_USD = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=CHF&apikey={API}"
    responce = requests.get(url_USD) 
    USD_EX=responce.json()
    USD_kurs=USD_EX["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    currency_exchange_base1["USD"] = USD_kurs

    file_name = "log_USD_to_CHF.json"
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


    """Гривні в Франки"""
    url_UAH = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=UAH&to_currency=CHF&apikey={API}"
    responce = requests.get(url_UAH) 
    UAH_EX=responce.json()
    UAH_kurs=UAH_EX["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    currency_exchange_base1["UAH"] = UAH_kurs

    file_name = "log_UAH_to_CHF.json"
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

    """Євро в Франки"""
    url_EUR = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=EUR&to_currency=CHF&apikey={API}"
    responce = requests.get(url_EUR) 
    EUR_EX=responce.json()
    EUR_kurs=EUR_EX["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    currency_exchange_base1["EUR"] = EUR_kurs
    
    file_name = "log_EUR_to_CHF.json"
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

    
    #
    """Франки в долари"""
    url_CHF = f"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=CHF&to_currency=USD&apikey={API}"
    responce = requests.get(url_CHF) 
    CHF_EX=responce.json()
    CHF_kurs=CHF_EX["Realtime Currency Exchange Rate"]["5. Exchange Rate"]
    exchange_CHF_to_USD["CHF"] = CHF_kurs
    #

    file_name = "log_CHF_to_USD.json"
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
    plus1,plus2 = 0,0
    for key1,value1 in currency_exchange_base1.items():
        if self.currency == key1:
            plus1 =  self.value * float(value1)
    for key2,value2 in currency_exchange_base1.items():
        if other.currency == key2:
            plus2 = other.value * float(value2) 
            p_1 = plus1 + plus2
            for value_1 in exchange_CHF_to_USD.values():    
                p_2 = p_1 * float(value_1) #CHF to USD
            return f"Сума валют переведених в Доларах США {p_2} "

def shotakoe_minus(self,other):        
    minus1,minus2 = 0,0
    for key1,value1 in currency_exchange_base1.items():
        if self.currency == key1:
            minus1 =  self.value * float(value1)
    for key2,value2 in currency_exchange_base1.items():
        if other.currency == key2:
            minus2 = other.value * float(value2) 
            m_1 = minus1 - minus2 
            for value_2 in exchange_CHF_to_USD.values():
                m_2 = m_1 * float(value_2) #CHF to USD
            return f"Різниця вал.т переведених в Доларах США {m_2} "

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
oleg = flight+hotel
print(oleg)
end_time = time.time()
execution_time = end_time - start_time
print(f"Програма зайняла {execution_time} секунд твого часу")    