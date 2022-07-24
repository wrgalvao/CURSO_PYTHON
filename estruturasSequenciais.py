nome = input("Digite o seu nome\n")
idade = input("Digite a sua idade\n")
idade = int(idade)
print("nome digitado: ", nome, type(nome))
print("idade digitada: ", idade, type(idade))
salario_mensal = input("Digite o seu salario mensal\n")
salario_mensal = float(salario_mensal)
gasto_mensal = input("Por favor digite seu gasto mensal\n")
gasto_mensal = float(gasto_mensal)
salario_total = salario_mensal * 12
gasto_total = gasto_mensal * 12
economizado = salario_total - gasto_total
print(nome, "de idade", idade, "pode economizar ao ano o valor total de", economizado)