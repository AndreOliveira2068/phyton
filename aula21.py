"""TODO: Imprimir a saída no padrão definido no enunciado deste desafio."""
"""Dica: Para simplificar a formatação, utilize o conceito de interpolação de strings."""

nomeRestaurante = input("Insira o nome do restaurante: ")
tempoEstimadoEntrega = int(input("Insira o tempo estimado de entrega (em minutos): "))

mensagem = f"O restaurante {nomeRestaurante} estima um tempo de entrega de {tempoEstimadoEntrega} minutos."
print(mensagem)