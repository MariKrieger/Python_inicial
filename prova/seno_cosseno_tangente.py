op = float(input('Digite o valor do cateto oposto: '))
adj = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = float(input('Digite o valor da hipotenusa: '))
def calculo_do_seno():
    return  op/hipotenusa

def calculo_do_cosseno():
    return  adj/hipotenusa

def calculo_da_tangente():
    return  op/adj


seno = calculo_do_seno()
cosseno = calculo_do_cosseno()
tangente = calculo_da_tangente()

print("O seno é {:.2f}".format(seno))
print("O cosseno é {:.2f}".format(cosseno))
print("A tangente é {:.2f}".format(tangente))



