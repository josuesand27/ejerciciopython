hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]
"""1 Carly quiere poder comercializar sus precios bajos. Queremos saber cuál es el precio medio de un corte.
Primero, resumamos todos los precios de los cortes de pelo. Cree una variable total_price y configúrela en 0.
"""
#2
Total_price=0
for i in prices:
    Total_price+=i
    

#3-Después de su bucle, cree una variable llamada average_price que sae total_price divida por el número de precios.
#Puede obtener el número de precios utilizando la len()función.
Total_Elements=len(prices)
average_price=Total_price/Total_Elements
#4
print("Promedio de precios")
print("Total revenue:", "<||", average_price, "||>")

#5
#¡Ese precio promedio es más caro de lo que Carly pensó que sería! Ella quiere reducir todos los precios en 5 dólares.
#Use una lista de comprensión para hacer una lista llamada new_prices, que tiene cada elemento en prices menos 5.
new_prices=[n - 5 for n in prices]


print("Nuevos precios:", "<||",new_prices, "||>")

#7 Carly realmente quiere asegurarse de que Carly's Clippers sea un esfuerzo rentable. 
#Primero quiere saber cuántos ingresos se generaron la semana pasada.
#Cree una variable llamada total_revenue y configúrela en 0.
total_revenue=0

#8. Use un forbucle para crear una variable i que vaya de 0 a len(hairstyles) #Sugerencia:¡Puedes usar range()para hacer esto!
for j in range(0,len(hairstyles)+1):
    print(prices[j], last_week[j]) 

    
    
print("Cantidad De Estilos De Cortes:","<",j,">")
#9. Agregue el producto de prices[i] (el precio del corte de cabello en la posición i)
#y last_week[i] (el número de personas que se cortaron el cabello en la posición i) total_revenueb en cada paso.

for t in n:
    t+= last_week 
    

#10. Después de su ciclo, imprima el valor de total_revenue, para que la salida se vea así:

print(total_revenue)


#11.¿Qué pasa con una compra anticipada? Nuestros últimos invitados pidieron el plato de salumeria y 
# los raviolis veganos de champiñones. Calcula la factura con calculate_bill().

average_daily_revenuee=total_revenue//7
print(average_daily_revenuee)

#12.Basta Fazoolin' with my Heart ha tenido un éxito tremendo en el mercado familiar, lo cual es fantástico porque cuando estás en Basta Fazoolin' with my Heart with family, ¡es fantástico!
# Hemos decidido crear más de un restaurante para ofrecer nuestros fantásticos menús, servicios y ambiente en todo el país.
#Primero, vamos a crear una Franchise class.

