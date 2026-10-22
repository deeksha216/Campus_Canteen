
# Campus Canteen Pre-Order System

DISCOUNT_LIMIT = 300
DISCOUNT_RATE = 0.10
GST_RATE = 0.05
MAX_ORDERS_PER_SLOT = 40


def calculate_total(subtotal):
    """Calculate the final bill with discount and GST."""

    if subtotal < 0:
        raise ValueError("Subtotal cannot be negative")

    if subtotal > DISCOUNT_LIMIT:
        subtotal = subtotal * (1 - DISCOUNT_RATE)

    total = subtotal * (1 + GST_RATE)

    return round(total, 2)


def can_accept_order(current_orders):
    """Check whether a pickup slot can accept another order."""

    if current_orders < 0:
        raise ValueError("Order count cannot be negative")

    return current_orders < MAX_ORDERS_PER_SLOT


def process_payment(payment_gateway, amount):
    """Process payment through the supplied payment gateway."""

    if amount < 0:
        raise ValueError("Amount cannot be negative")

    return payment_gateway.charge(amount)


# Test the order module
if __name__ == "__main__":
    print("Bill for ₹200:", calculate_total(200))
    print("Bill for ₹400:", calculate_total(400))
    print("Slot with 39 orders:", can_accept_order(39))
    print("Slot with 40 orders:", can_accept_order(40))

