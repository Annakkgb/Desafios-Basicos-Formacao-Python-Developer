# O desafio trata de resolver o seguinte: O microblog Twitter é conhecido por limitar as postagens em 140 caracteres. Conferir se um texto vai caber em um tuíte é sua tarefa.
texto = input()

if len(texto) <= 140:
    print("TWEET")
else:
    print("MUTE")