from gestor import crear_ticket, listar_tickets, buscar_ticket, cambiar_estado

def main():
    # Crear lista vacía
    tickets = []

    # Crear los 2 tickets de prueba
    crear_ticket(tickets, "Error al iniciar sesión", "Alta")
    crear_ticket(tickets, "Actualizar navegador", "Baja")

    print("--- LISTA INICIAL ---")
    listar_tickets(tickets)

    # 1 y 2. Buscar el ticket ID 1 y mostrar sus datos si existe
    print("\n--- BUSCANDO TICKET ID 1 ---")
    ticket_buscado = buscar_ticket(tickets, 1)
    if ticket_buscado:
        print(f"¡Ticket encontrado!")
        print(f"ID: {ticket_buscado.id_ticket}")
        print(f"Título: {ticket_buscado.titulo}")
        print(f"Prioridad: {ticket_buscado.prioridad}")
        print(f"Estado: {ticket_buscado.estado}")

    # 3. Cambiar el ticket ID 1 a "En progreso"
    cambiar_estado(tickets, 1, "En progreso")

    # 4. Volver a listar los tickets para comprobar el cambio
    print("\n--- LISTA DESPUÉS DEL CAMBIO DE ESTADO ---")
    listar_tickets(tickets)

if __name__ == "__main__":
    main()