from unittest.mock import Mock

from TicketService import TicketService
from inventarioSpy import InventarioSpy
from RepositorioFake import RepositorioFake
from UsuarioDummy import UsuarioDummy


def test_flujo_completo_compra():

    inventario = InventarioSpy()

    repositorio = RepositorioFake()

    email = Mock()

    service = TicketService(
        inventario,
        repositorio,
        email
    )

    resultado = service.comprar(
        UsuarioDummy(),
        2
    )

    assert resultado is True

    assert inventario.veces_consultado == 1

    assert len(repositorio.compras) == 1

    email.enviar_confirmacion.assert_called_once()