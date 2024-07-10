import math
def calculo_da_hipotenusa():
    op = float(input('Digite o valor do cateto oposto: '))
    adj = float(input('Digite o valor do cateto adjacente: '))
    hipotenusa = math.sqrt(op**2 + adj**2)
    return hipotenusa


resultado = calculo_da_hipotenusa()
print("A hipotenusa é {:.2f}".format(resultado))



