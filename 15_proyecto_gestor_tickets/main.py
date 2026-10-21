from pathlib import Path

from gestor import crear_ticket, listar_tickets, buscar_ticket, cambiar_estado
from persistencia import guardar_tickets, cargar_tickets


def main():
    # Ruta del directorio donde se encuentra este archivo
    ruta_base = Path(__file__).resolve().parent

    # El JSON quedará dentro de:
    # 15_proyecto_gestor_tickets/datos/tickets.json
    ruta_archivo = ruta_base / "datos" / "tickets.json"

    # Crear la carpeta datos si todavía no existe
    ruta_archivo.parent.mkdir(parents=True, exist_ok=True)

    # Cargar tickets guardados al iniciar
    tickets = cargar_tickets(ruta_archivo)

    while True:
        print("\n--- GESTOR DE TICKETS ---")
        print("1. Crear ticket")
        print("2. Listar tickets")
        print("3. Buscar ticket")
        print("4. Cambiar estado")
        print("5. Guardar tickets")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == "1":
            titulo = input("Ingrese el título del ticket: ")
            prioridad = input(
                "Ingrese la prioridad (Alta, Media, Baja): "
            )

            crear_ticket(
                tickets,
                titulo,
                prioridad
            )

            print("¡Ticket creado con éxito!")

        elif opcion == "2":
            listar_tickets(tickets)

        elif opcion == "3":
            try:
                id_buscado = int(
                    input("Ingrese el ID del ticket a buscar: ")
                )

                ticket = buscar_ticket(
                    tickets,
                    id_buscado
                )

                if ticket:
                    print("\n--- TICKET ENCONTRADO ---")
                    print(f"ID: {ticket.id_ticket}")
                    print(f"Título: {ticket.titulo}")
                    print(f"Prioridad: {ticket.prioridad}")
                    print(f"Estado: {ticket.estado}")

                else:
                    print(
                        "No se encontró ningún ticket con ese ID."
                    )

            except ValueError:
                print(
                    "Error: Debe ingresar un número entero "
                    "válido para el ID."
                )

        elif opcion == "4":
            try:
                id_buscado = int(
                    input("Ingrese el ID del ticket a modificar: ")
                )

                nuevo_estado = input(
                    "Ingrese el nuevo estado "
                    "(Abierto, En progreso, Cerrado): "
                )

                exito = cambiar_estado(
                    tickets,
                    id_buscado,
                    nuevo_estado
                )

                if exito:
                    print("¡Estado actualizado con éxito!")

                else:
                    print(
                        "No se encontró un ticket con ese ID."
                    )

            except ValueError:
                print(
                    "Error: Debe ingresar un número entero "
                    "válido para el ID."
                )

        elif opcion == "5":
            guardar_tickets(
                tickets,
                ruta_archivo
            )

            print(
                "¡Tickets guardados correctamente en JSON!"
            )

        elif opcion == "6":
            guardar_tickets(
                tickets,
                ruta_archivo
            )

            print(
                "Guardando cambios... ¡Hasta luego!"
            )

            break

        else:
            print(
                "Opción inválida. Por favor, "
                "ingrese un número entre 1 y 6."
            )


if __name__ == "__main__":
    main()