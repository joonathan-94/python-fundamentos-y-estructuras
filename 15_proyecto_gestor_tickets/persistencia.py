import json
from pathlib import Path

from ticket import Ticket


def guardar_tickets(ticket_list, ruta):
    """Guarda una lista de objetos Ticket en formato JSON."""

    ruta = Path(ruta)

    lista_diccionarios = []

    for ticket in ticket_list:
        lista_diccionarios.append({
            "id_ticket": ticket.id_ticket,
            "titulo": ticket.titulo,
            "prioridad": ticket.prioridad,
            "estado": ticket.estado
        })

    with open(
        ruta,
        "w",
        encoding="utf-8"
    ) as archivo:

        json.dump(
            lista_diccionarios,
            archivo,
            indent=4,
            ensure_ascii=False
        )


def cargar_tickets(ruta):
    """Carga tickets desde JSON y los reconstruye como objetos Ticket."""

    ruta = Path(ruta)

    if not ruta.exists():
        return []

    try:
        with open(
            ruta,
            "r",
            encoding="utf-8"
        ) as archivo:

            lista_diccionarios = json.load(archivo)

    except json.JSONDecodeError:
        return []

    ticket_list = []

    for datos_ticket in lista_diccionarios:
        ticket = Ticket(
            datos_ticket["id_ticket"],
            datos_ticket["titulo"],
            datos_ticket["prioridad"]
        )

        ticket.estado = datos_ticket["estado"]

        ticket_list.append(ticket)

    return ticket_list