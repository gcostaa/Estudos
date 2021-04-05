from conta import Conta

conta = Conta(1,"Gustavo",100.0,5.000)

print(conta.cod_banco())
bancos = conta.cod_bancos()
print(bancos["Caixa"])



#None é igual a null
conta = None