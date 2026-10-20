from gestor import crear_ticket, listar_tickets

def main():
    # 1. Crear lista vacía
    tickets = []

    # 2. Crear los 2 tickets de prueba solicitados
    crear_ticket(tickets, "Error al iniciar sesión", "Alta")
    crear_ticket(tickets, "Actualizar navegador", "Baja")

    # 3. Listar tickets para verificar la salida por consola
    listar_tickets(tickets)

if __name__ == "__main__":
    main()