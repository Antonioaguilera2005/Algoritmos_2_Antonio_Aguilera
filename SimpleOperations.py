import functools

class SimpleOperations:
    def apply_discount(self, price, discount):
        """Aplica un descuento al precio dado y retorna el nuevo precio."""
        return price * (1 - discount)

    def calculate_tax(self, price, tax_rate):
        """Calcula y agrega el impuesto al precio dado."""
        return price * (1 + tax_rate)

# Crear una instancia de SimpleOperations
operations = SimpleOperations()

# Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
twenty_percent_discount = functools.partial(operations.apply_discount, discount=0.20)
vat_tax = functools.partial(operations.calculate_tax, tax_rate=0.21)

# Usar las funciones preconfiguradas.
price = 100  # Precio base

# Aplicar descuento del 20%
discounted_price = twenty_percent_discount(price)
print("Precio con descuento del 20%:", discounted_price)

# Calcular impuesto del 21%
price_with_tax = vat_tax(price)
print("Precio con impuesto del 21%:", price_with_tax)
