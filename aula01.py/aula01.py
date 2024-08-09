##REVISÃO RAPIDA 
## strigng = para definir nome, texto etc...
## int = para numeros inteiros (20)
## float = para numeros decimas (30,2)
### booleano = para definir TRUE (verdadeiro) ou FALSE (falso)
####################
## ESTRUTURA DE CONDIÇÂO
# Faça um programa que calcule a média de alunos com 3 notas, e verifica se o aluno foi APROVADO, se está em RECUPERAÇÃO ou se foi REPROVADO!!


nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3
print("A media do aluno é: " + str(media))
###Quando  exibir uma mensagem na tela a tem  numero, precisamos colocar o str, pois ele vai  converte a variavel numero em texto, se não colocamos, vai dar errado

if(media >= 7):
    print(f"aluno APROVADO!! com media de: {media}") 
    if(media > 5):
        print(f"Aluno em RECUPERAÇÃO! {media}")
else:
    print("Aluno está REPROVADO! com medía de: " + str(media))  
    