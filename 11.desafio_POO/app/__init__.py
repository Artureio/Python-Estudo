from .cliente import Cliente
from .vendedor import Vendedor
from .compra import Compra
# A classe Pessoa não foi exposta propositalmente (pois não é necessária)
__all__ = ['Cliente', 'Vendedor', 'Compra']