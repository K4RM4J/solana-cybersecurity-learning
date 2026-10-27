
print("=== CALCULADORA DE MARKET CAP ===")

precio = float(input("Precio del token en USD: "))
tokens = float(input("Tokens en circulacion: "))

market_cap = precio * tokens

print("----------------------------")
print(f"Market Cap: ${market_cap:,.2f}")
