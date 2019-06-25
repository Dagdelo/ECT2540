# -*- coding: utf-8 -*-
"""
ECT/UFRN - POO - Projeto Final
Módulo que contém uma arena
na forma de um Canvas TK.
"""

import tkinter as tk
from robo import *
from itens_tk import *

class ErroArena(Exception):
    """
    Erro base para a classe Arena.
    """
    pass

class ArenaTK(tk.Canvas):
    """
    Classe que representa uma arena.
    Uma arena é um conjunto de larg X alt
    células, tendo cada uma um tamanho fixo.
    Cada célula representa uma posição livre
    ou que contém um obstáculo para os robôs.
    A arena também possui vários robôs.
    """
    pass

if __name__ == "__main__":
    root = tk.Tk()
    root.title('Arena de Robos')

    arena = ArenaTK(root, 'arenas/arena3.txt')
    arena.pack()

    # cria robôs/sensores

    #arena.adiciona_robo(r1)
    #arena.adiciona_robo(r2)

    #arena.ativa_controle_robo(r1.nome)

    root.mainloop()