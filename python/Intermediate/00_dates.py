### Dates ###
#importamos el objeto "datetime" desde el módulo datetime
from datetime import datetime

#Utilizamos el metodo now() para inicializar la fecha con el momento actual
now= datetime.now()

def print_date():
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
print_date()
