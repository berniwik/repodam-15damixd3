""" 15. Algorisme que llegeix dos nombres en dues variables i intercanvia el seu valor. """
NUM1 = input('Introdueix un numero (num1) ')
NUM1 = int(NUM1)
NUM2 = input('Introdueix un numero (num2) ')
NUM2 = int(NUM2)

print("Els valors de les variables abants de l'intercanvi són:num1", NUM1, "num2", NUM2)
VARINT = NUM1
NUM1 = NUM2
NUM2 = VARINT
print("Els valors de les variables despres de l'intercanvi són:num1", NUM1, "num2", NUM2)
