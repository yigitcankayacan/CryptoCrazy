import requests


def get_crypto_data():
    response = requests.get(url="https://raw.githubusercontent.com/atilsamancioglu/K21-JSONDataSet/master/crypto.json")
    return response.json()


crypto_response = get_crypto_data()
user_input = input("Enter your favorite crypto: ")
for crypto in crypto_response:
    if crypto["currency"] == user_input:
        print(crypto["price"])
