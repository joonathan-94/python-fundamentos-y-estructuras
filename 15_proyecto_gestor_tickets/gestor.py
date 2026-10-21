from ticket import Ticket

def crear_ticket(ticket_list, titulo, prioridad):
    # La fórmula len(ticket_list) + 1 funciona tanto si la lista está vacía como si tiene elementos
    nuevo_id = len(ticket_list) + 1
    ticket = Ticket(nuevo_id, titulo, prioridad)
    ticket_list.append(ticket)
    return ticket

def listar_tickets(ticket_list):
    if len(ticket_list) == 0:
        print("No hay tickets registrados.")
        return
    
    for ticket in ticket_list:
        print(f"ID: {ticket.id_ticket}")
        print(f"Título: {ticket.titulo}")
        print(f"Prioridad: {ticket.prioridad}")
        print(f"Estado: {ticket.estado}")
        print("-" * 25) # Un separador opcional para que se vea más ordenado

def buscar_ticket(ticket_list, id_buscado):
    for ticket in ticket_list:
        if ticket.id_ticket == id_buscado:
            return ticket
    return None

def cambiar_estado(ticket_list, id_buscado, nuevo_estado):
    ticket = buscar_ticket(ticket_list, id_buscado)
    if ticket is None:
        return False
    else:
        ticket.estado = nuevo_estado
        return True