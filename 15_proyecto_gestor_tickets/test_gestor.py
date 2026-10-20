from gestor import crear_ticket, buscar_ticket


def test_crear_ticket():
    lista_tickets = []

    ticket = crear_ticket(
        lista_tickets,
        "Error en el sistema de inicio de sesión",
        "Alta"
    )

    assert len(lista_tickets) == 1
    assert ticket.id_ticket == 1
    assert ticket.titulo == "Error en el sistema de inicio de sesión"
    assert ticket.prioridad == "Alta"
    assert ticket.estado == "Abierto"


def test_buscar_ticket():
    lista_tickets = []

    crear_ticket(
        lista_tickets,
        "Primer ticket de soporte",
        "Alta"
    )

    crear_ticket(
        lista_tickets,
        "Segundo ticket de soporte",
        "Media"
    )

    ticket_encontrado = buscar_ticket(
        lista_tickets,
        2
    )

    assert ticket_encontrado is not None
    assert ticket_encontrado.id_ticket == 2
    assert ticket_encontrado.titulo == "Segundo ticket de soporte"
    assert ticket_encontrado.prioridad == "Media"