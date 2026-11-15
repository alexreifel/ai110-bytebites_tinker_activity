"""ByteBites backend models: customers, menu items, the menu, and orders."""


class MenuItem:
    """A single food or drink item that ByteBites sells."""

    def __init__(self, name, price, category, popularity_rating):
        self.name = name
        self.price = price
        self.category = category
        self.popularity_rating = popularity_rating

    def __repr__(self):
        return (f"MenuItem({self.name!r}, ${self.price:.2f}, "
                f"{self.category!r}, rating={self.popularity_rating})")


class Menu:
    """The full collection of items, with filtering and sorting."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def filter_by_category(self, category):
        """Return the items whose category exactly matches `category`."""
        return [item for item in self.items if item.category == category]

    def sort_by_popularity(self):
        """Return a new list of items, most popular first. `items` is unchanged."""
        return sorted(self.items, key=lambda item: item.popularity_rating, reverse=True)

    def __repr__(self):
        return f"Menu({len(self.items)} items)"


class Order:
    """A single transaction grouping the items a customer selected."""

    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def compute_total(self):
        """Return the sum of item prices, rounded to cents."""
        return round(sum(item.price for item in self.items), 2)

    def __repr__(self):
        return f"Order({len(self.items)} items, total=${self.compute_total():.2f})"


class Customer:
    """A ByteBites user and their past orders."""

    def __init__(self, name):
        self.name = name
        self.purchase_history = []

    def add_purchase(self, order):
        self.purchase_history.append(order)

    def is_verified(self):
        """A customer counts as a real user once they have at least one past order."""
        return len(self.purchase_history) > 0

    def __repr__(self):
        return f"Customer({self.name!r}, {len(self.purchase_history)} past orders)"


if __name__ == "__main__":
    print("== 1. Create and inspect menu items ==")
    burger = MenuItem("Spicy Burger", 8.99, "Burgers", 4.6)
    veggie = MenuItem("Veggie Burger", 7.49, "Burgers", 3.9)
    soda = MenuItem("Large Soda", 2.49, "Drinks", 4.1)
    tea = MenuItem("Iced Tea", 1.99, "Drinks", 3.5)
    brownie = MenuItem("Fudge Brownie", 3.25, "Desserts", 4.8)
    for item in [burger, veggie, soda, tea, brownie]:
        print(f"  {item.name}: price={item.price}, category={item.category}, "
              f"rating={item.popularity_rating}")
    assert burger.name == "Spicy Burger"
    assert burger.price == 8.99
    assert burger.category == "Burgers"
    assert burger.popularity_rating == 4.6

    print("\n== 2. Add items to the menu ==")
    menu = Menu()
    for item in [burger, veggie, soda, tea, brownie]:
        menu.add_item(item)
    print(f"  {menu}")
    assert len(menu.items) == 5

    print("\n== 3. Filter by category ==")
    drinks = menu.filter_by_category("Drinks")
    desserts = menu.filter_by_category("Desserts")
    print(f"  Drinks:   {[item.name for item in drinks]}")
    print(f"  Desserts: {[item.name for item in desserts]}")
    assert [item.name for item in drinks] == ["Large Soda", "Iced Tea"]
    assert [item.name for item in desserts] == ["Fudge Brownie"]
    assert menu.filter_by_category("Salads") == []

    print("\n== 4. Sort by popularity ==")
    original_order = list(menu.items)
    ranked = menu.sort_by_popularity()
    for item in ranked:
        print(f"  {item.popularity_rating}  {item.name}")
    ratings = [item.popularity_rating for item in ranked]
    assert ratings == sorted(ratings, reverse=True)
    assert ranked[0] is brownie
    assert menu.items == original_order, "sorting should not change menu.items"

    print("\n== 5. Build an order and compute the total ==")
    order = Order()
    assert order.compute_total() == 0
    order.add_item(burger)
    order.add_item(soda)
    order.add_item(brownie)
    print(f"  Items: {[item.name for item in order.items]}")
    print(f"  Total: ${order.compute_total():.2f}")
    assert order.compute_total() == 14.73  # 8.99 + 2.49 + 3.25

    print("\n== 6. Customer purchase history and verification ==")
    alex = Customer("Alex")
    print(f"  Before purchase: {alex}, verified={alex.is_verified()}")
    assert alex.is_verified() is False
    alex.add_purchase(order)
    print(f"  After purchase:  {alex}, verified={alex.is_verified()}")
    assert alex.is_verified() is True
    assert alex.purchase_history == [order]

    print("\nAll checks passed.")
