from conta import Conta
from cliente import Cliente

cliente_1 = Cliente("Joana da Silva")
conta_1 = Conta(1)
conta_1.depositar(200)

print(f'Cliente: {cliente_1.nome}')
print(f'Saldo: {conta_1.saldo}')
print(f'Limite: {conta_1.limite}')

cliente_2 = Cliente("Carla da Silva")
conta_2 = Conta(2, 300, 200)

print(f'Cliente: {cliente_2.nome}')
print(f'Saldo: {conta_2.saldo}')
print(f'Limite: {conta_2.limite}')

conta_2.transferir(100, conta_1, cliente_1)

print(f'Cliente: {cliente_1.nome}')
print(f'Saldo: {conta_1.saldo}')
print(f'Limite: {conta_1.limite}')

print(f'Cliente: {cliente_2.nome}')
print(f'Saldo: {conta_2.saldo}')
print(f'Limite: {conta_2.limite}')