farenheit=0
celsius=0
#2
def f_to_c(farenheit, celsius):
    f=float(input("dijite la cantidad en fahrenheit que desea convertir a grados celsius : "))
    ce=(f-32)*5/9

    print("la temperatura fahrenheit de",f,"° es igual a ",ce,"°"," Celsius")

f_to_c(farenheit, celsius)
#3
f=0
c=0
def c_to_f(f,c):
    c=float(input(" Dijite la cantidad en ° celsius que desea convertir a ° farenheit : "))
    f= c * (9/5) + 32
    print("La Temperatura ° Celsius : ", c,"es  igual A :",f,"°","Farenheit" )
#4
c_to_f(f,c)
#5 
m=0
a=0
fo=0
def get_force(m,a,fo):
    m=float(input("Dijite la masa :"))
    a=float(input("Dijite la aceleracion :"))
    fo+= m*a
    print(fo)
get_force(m,a,fo)