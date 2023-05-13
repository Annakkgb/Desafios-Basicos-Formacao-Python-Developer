# O desafio trata de resolver o seguinte: Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.
n = int(input())  # Quantidade de casos de teste

for _ in range(n):
    a, b = input().split()  # Lê os valores A e B separados por espaço

    if a.endswith(b):
        print("encaixa")
    else:
        print("nao encaixa")
