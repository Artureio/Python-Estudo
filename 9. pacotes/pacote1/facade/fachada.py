# centralizando as funções matematicas em um unico arquivo 'fachada'
from pacote1.modulo1 import soma
from pacote1.modulo2 import subtracao
from pacote1.modulo import main

__all__ = ['soma', 'subtracao', 'main']
