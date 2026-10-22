
# Task 6 - Code Refactoring

## Refactoring 1: Improve Variable Names

Before:
    def calculate(p):
        x = p * 0.05
        return p + x

After:
    def calculate_total(subtotal):
        gst_amount = subtotal * 0.05
        return subtotal + gst_amount

Improvement:
Meaningful names make the code easier to understand.

## Refactoring 2: Replace Magic Numbers

Before:
    def can_accept_order(n):
        return n < 40

After:
    MAX_ORDERS_PER_SLOT = 40

    def can_accept_order(current_orders):
        return current_orders < MAX_ORDERS_PER_SLOT

Improvement:
A named constant explains why the number 40 is used.

## Refactoring 3: Simplify Conditional Logic

Before:
    def check(n):
        if n < 40:
            return True
        else:
            return False

After:
    def can_accept_order(current_orders):
        return current_orders < 40

Improvement:
The shorter code produces the same result for the same input.
