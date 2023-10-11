my_clients = [("cliente1", "5", "1234.5", "calle1"),("cliente1", "6", "12.5", "calle1"), ("cliente2", "5", "134.5", "calle2"), ("cliente3", "6", "12300", "calle3") ]
def return_adress(clients):
    adresses = []
    for client in clients:
        adresses.append(client[3])
    adresses = list(set(adresses))
    for adress in adresses:
        print(adress)
return_adress(my_clients)