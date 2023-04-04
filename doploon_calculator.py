import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Define as quantidades de dooplons necessárias para cada tipo de pergaminho
SMALL_DOOPLOONS = 20
MEDIUM_DOOPLOONS = 60
GREAT_DOOPLOONS = 140
POWERFUL_DOOPLOONS = 340

# Recebe a quantidade de dooplons
doploon_quantity = int(input("Digite a quantidade de dooplons: "))

# Recebe o preço de cada tipo de pergaminho
small_price = int(input("Preço do pergaminho pequeno: "))
medium_price = int(input("Preço do pergaminho médio: "))
great_price = int(input("Preço do pergaminho grande: "))
powerful_price = int(input("Preço do pergaminho poderoso: "))

# Calcula a quantidade de cada tipo de pergaminho que pode ser comprado
small_quantity = doploon_quantity // SMALL_DOOPLOONS
medium_quantity = doploon_quantity // MEDIUM_DOOPLOONS
great_quantity = doploon_quantity // GREAT_DOOPLOONS
powerful_quantity = doploon_quantity // POWERFUL_DOOPLOONS

# Calcula o preço total de cada tipo de pergaminho
small_price = {"name": "Pequeno", "price": small_quantity * small_price}
medium_price = {"name": "Médio", "price": medium_quantity * medium_price}
great_price = {"name": "Grande", "price": great_quantity * great_price}
powerful_price = {"name": "Poderoso", "price": powerful_quantity * powerful_price}

# Cria uma lista com todos os tipos de pergaminho e seus preços
parchment_list = [small_price, medium_price, great_price, powerful_price]

# Encontra o pergaminho mais valioso
most_valuable_parchment = max(parchment_list, key=lambda x: x["price"])

# Imprime a quantidade de cada tipo de pergaminho que pode ser comprado e seu preço total
print("\nÉ possível pegar as seguintes quantidades de cada pergaminho:\n")
print(f"Pequeno: {small_quantity} com um valor total de: {small_price['price']:,.0f}K".replace(",", "."))
print(f"Médio: {medium_quantity} com um valor total de: {medium_price['price']:,.0f}K".replace(",", "."))
print(f"Grande: {great_quantity} com um valor total de: {great_price['price']:,.0f}K".replace(",", "."))
print(f"Poderoso: {powerful_quantity} com um valor total de: {powerful_price['price']:,.0f}K".replace(",", "."))

# Imprime o pergaminho mais valioso e seu preço
print(f"\nO valor mais alto é do pergaminho {most_valuable_parchment['name']}: {most_valuable_parchment['price']:,.0f}K".replace(",", "."))
