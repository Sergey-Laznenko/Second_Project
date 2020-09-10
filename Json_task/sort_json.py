#дан файл json со списком работников, необходимо его открыть, добавить нового члена команды, отсортировать файл по опыту работников и открыть новый файл
import json
with open ("clients.json", encoding="utf8") as f:
    clients = json.load(f)

y = {"Имя":'Олег', 
         "должность": "Стажер", 
         "опыт": "0 лет"
        } 

clients.append(y)
clients = sorted(clients, key = lambda s: s['опыт'])  #в квадратных скобках пишешь ключ по которому надо отсортировать список
#print (clients)
with open('/home/dasha/Documents/QA/18 block/clients_1.json', 'w') as f:
    json.dump(clients, f, ensure_ascii=False)
with open ('/home/dasha/Documents/QA/18 block/clients_1.json') as f:
    print(f.read())
