
def tabuada(num):
    tabuada = [f"{num} x {i} = {num * i}" for i in range(1, 11)]
    return f"Tabuada de {num}:
" + "\n".join(tabuada)
