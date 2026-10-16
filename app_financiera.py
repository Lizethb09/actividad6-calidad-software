
"""Ejemplo académico de gestión financiera para analizar con SonarQube."""

def calcular_saldo(saldo_inicial, ingresos, gastos):
    """Calcula el saldo disponible de una cuenta."""
    saldo = saldo_inicial

    for ingreso in ingresos:
        saldo = saldo + ingreso

    for gasto in gastos:
        saldo = saldo - gasto

    return saldo


def procesar_transferencia(saldo, monto):
    """Simula la validación básica de una transferencia."""
    if monto > 0:
        if saldo >= monto:
            nuevo_saldo = saldo - monto
            return nuevo_saldo, "Transferencia procesada"

        return saldo, "Saldo insuficiente"

    return saldo, "El monto debe ser mayor que cero"


def mostrar_resumen(saldo, estado):
    """Muestra el resultado de una operación."""
    print("Saldo disponible:", saldo)
    print("Estado de la operación:", estado)


if __name__ == "__main__":
    saldo_actual = calcular_saldo(
        100000,
        [25000, 15000],
        [10000, 5000],
    )

    nuevo_saldo, mensaje = procesar_transferencia(
        saldo_actual,
        20000,
    )

    mostrar_resumen(nuevo_saldo, mensaje)
