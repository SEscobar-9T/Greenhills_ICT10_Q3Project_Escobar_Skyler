from pyscript import display, document

def player_list(e):
    document.getElementById('output').innerHTML = ''
    
    topaz = ["Abdullah", "Abeleda", "Arce", "Arias", "Bonzon", "Cajucom", "Catimbang", "Choi", "Cotioco", "Daradal", "Enriquez", "Escobar", "Espina", "Gano", "Garcia", "Kaur", "Ong", "Rufo", "Santos", "Sanchez", "Tan", "Vilale", "Yao", "Zosa"]
    for index in range(len(topaz)):
        display(topaz[index], target='output')