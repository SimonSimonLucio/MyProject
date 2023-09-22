#remoção de pontuações 
pontuacoes = "!?=,*/:#)($@-+><}{][|\~•`αβ^®©™π¤¥€...`£¢√%_&€¥"
frase = str(input("Digite um texto: ")).upper().strip() #remoção de espaços da direita e esquerda e colocar o texto em maiúsculas
no_point = "" 
for v in frase:
    if v not in pontuacoes:
        no_point += v
#Separando, juntando e invertendo as o texto
palavra = no_point.split()
juncao = ''.join(palavra)
inverso = juncao[:: - 1]
#Imprimindo a texto corretamente e o seu inverso
print(f"O inverso de {juncao} é {inverso}")
#Fazendo verificação no texto digitado pelo usuario para saber se o texto é polindroma 
if juncao == inverso:
    print("O texto digitado é polindroma.")
else:
    print("O texto digitado não é polindroma.")