"""
Interável -> str, range, etc
Interador -> quem sabe ebtregar um valor por vez
next ->  me entregue o próximo valor
iter -> me entregue seu interador 
"""
# for letras in texto

texto = ' ANDRE '    # interável
interador  = iter (texto)  # interador

while True:
    try:
        letra = next(interador)
        print(letra)
    except StopIteration:
        break    