from conta import Conta

conta = Conta(1,"Gustavo",1000,5000)

#print(conta.cod_banco())
#bancos = conta.cod_bancos()
#print(bancos["Caixa"])

conta.sacar(10000)
print(conta.getSaldo())



#None é igual a null
conta = None