"""Behavior tests for the ByteBites models. Run with: python3 -m pytest"""

from models import Customer, Menu, MenuItem, Order


def make_sample_menu():
    """A small menu with items across three categories."""
    menu = Menu()
    menu.add_item(MenuItem("Spicy Burger", 10.00, "Burgers", 4.6))
    menu.add_item(MenuItem("Large Soda", 5.00, "Drinks", 4.1))
    menu.add_item(MenuItem("Iced Tea", 1.99, "Drinks", 3.5))
    menu.add_item(MenuItem("Fudge Brownie", 3.25, "Desserts", 4.8))
    return menu


# --- Order totals ---

def test_calculate_total_with_multiple_items():
    """A $10 burger plus a $5 soda totals $15."""
    order = Order()
    order.add_item(MenuItem("Spicy Burger", 10.00, "Burgers", 4.6))
    order.add_item(MenuItem("Large Soda", 5.00, "Drinks", 4.1))
    assert order.compute_total() == 15.00


def test_order_total_is_zero_when_empty():
    """An order with no items totals $0 instead of crashing."""
    assert Order().compute_total() == 0


def test_order_total_rounds_to_cents():
    """Prices that don't add up cleanly in floating point still total to the cent."""
    order = Order()
    order.add_item(MenuItem("Iced Tea", 0.10, "Drinks", 3.5))
    order.add_item(MenuItem("Mint", 0.20, "Desserts", 3.0))
    assert order.compute_total() == 0.30


# --- Menu filtering ---

def test_filter_by_category_returns_only_matching_items():
    """Filtering 'Drinks' returns only the drink items."""
    drinks = make_sample_menu().filter_by_category("Drinks")
    assert [item.name for item in drinks] == ["Large Soda", "Iced Tea"]


def test_filter_by_unknown_category_returns_empty_list():
    """Filtering by a category with no items returns an empty list."""
    assert make_sample_menu().filter_by_category("Salads") == []


# --- Menu sorting ---

def test_sort_by_popularity_puts_highest_rated_first():
    """Sorting returns items from highest to lowest popularity rating."""
    ranked = make_sample_menu().sort_by_popularity()
    assert [item.name for item in ranked] == [
        "Fudge Brownie", "Spicy Burger", "Large Soda", "Iced Tea",
    ]


def test_sort_by_popularity_does_not_change_menu():
    """Sorting leaves the menu's own item order unchanged."""
    menu = make_sample_menu()
    before = list(menu.items)
    menu.sort_by_popularity()
    assert menu.items == before


# --- Customers ---

def test_new_customer_is_not_verified():
    """A customer with no purchase history is not verified."""
    assert Customer("Alex").is_verified() is False


def test_customer_is_verified_after_a_purchase():
    """A customer becomes verified once an order is added to their history."""
    customer = Customer("Alex")
    order = Order()
    customer.add_purchase(order)
    assert customer.is_verified() is True
    assert customer.purchase_history == [order]
