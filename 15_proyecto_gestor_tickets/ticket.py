class Ticket:
    
    def __init__(self, id_ticket, titulo, prioridad):
        self.id_ticket = id_ticket
        self.titulo = titulo
        self.prioridad = prioridad
        self.estado = "Abierto"
    
    