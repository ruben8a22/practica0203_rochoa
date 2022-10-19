#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por
# pantalla el número de euros y el número de céntimos del precio introducido.

precioProducto = input("Introduce el precio del producto")
euros=precioProducto[:precioProducto.find(".")]
centimos=precioProducto[precioProducto.find(".")+1:]
print(euros + "euros y" +  centimos+ "centimos.")