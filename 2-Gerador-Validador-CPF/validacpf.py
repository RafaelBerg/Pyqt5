import re

def valida_cpf(cpf):
    cpf = str(cpf)
    cpf = re.sub(r'[^0-9]', '', cpf)


    i = 10
    novo_valor = 0
    for numero in cpf:
        valor = int(numero) * i
        i -= 1
        novo_valor += valor
        if i < 2:
            break
    calculo1 = 11 - (novo_valor % 11)
    if calculo1 > 9:
        calculo1 = 0


    i2 = 11
    novo_valor2 = 0
    for numero2 in cpf:
        valor2 = int(numero2) * i2
        i2 -= 1
        novo_valor2 += valor2
        if i2 < 3:
            novo_valor2 += (calculo1 * i2)
            break
    calculo2 = 11 - (novo_valor2 % 11)


    novo_cpf = cpf[:9] + str(calculo1) + str(calculo2)
    sequencia = novo_cpf == str(novo_cpf[0]) * len(cpf)


    if cpf == novo_cpf and not sequencia:
        return True
    else:
        return False


if __name__ == "__main__":
    cpf = input("Digite um cpf:")
    valida_cpf(cpf)
