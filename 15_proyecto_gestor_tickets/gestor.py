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