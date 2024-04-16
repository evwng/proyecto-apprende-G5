from googlesearch import search 

# Consulta de búsqueda más específica para comprar galletas
query = "comprar galletas online"

# Realizar la búsqueda y obtener solo el primer resultado
for j in search(query, tld="co.in", num=1, stop=1, pause=2):
    print(j)
