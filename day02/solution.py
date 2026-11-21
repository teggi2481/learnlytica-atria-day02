
# 1. Custom domain exception
class OrderNotFoundError(Exception):
    """Raised when an order ID is not found."""
    pass


# 2. Look up an order
def lookup_order(orders: list[dict], order_id: str) -> dict:
    """
    Find an order by its ID.

    Raises:
        ValueError: If order_id is not a non-empty string.
        OrderNotFoundError: If the order does not exist.
    """

    # Validate input
    if not isinstance(order_id, str) or not order_id.strip():
        raise ValueError("order_id must be a non-empty string")

    # Search for the order
    for order in orders:
        if order["order_id"] == order_id:
            return order

    # Raise a domain-specific exception
    raise OrderNotFoundError(f"Order {order_id} not found")


# 3. Describe an order
def describe_order(orders: list[dict], order_id: str) -> str:
    """
    Return a readable description of an order.
    """

    try:
        order = lookup_order(orders, order_id)

        return (
            f"{order['status']} order "
            f"{order['order_id']} "
            f"totaling {order['total']}"
        )

    except OrderNotFoundError:
        return f"Order {order_id} not found"


# 4. Check whether an order is missing
def raises_not_found(orders: list[dict], order_id: str) -> bool:
    """
    Return True if lookup raises OrderNotFoundError.
    Otherwise return False.
    """

    try:
        lookup_order(orders, order_id)
        return False

    except OrderNotFoundError:
        return True


# 5. Sample order data
ORDERS = [
    {"order_id": "01", "status": "shipped", "total": 120.0},
    {"order_id": "02", "status": "processing", "total": 75.0},
    {"order_id": "03", "status": "delivered", "total": 299.0},
]


# 6. Run the application
if __name__ == "__main__":

    print(describe_order(ORDERS, "01"))
    print(describe_order(ORDERS, "09"))

    print(raises_not_found(ORDERS, "09"))
    print(raises_not_found(ORDERS, "01"))

    # Demonstrate invalid input
    try:
        lookup_order(ORDERS, "")
    except ValueError as error:
        print("Validation Error:", error)
