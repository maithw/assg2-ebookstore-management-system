# Importing all classes from Assg2
from Assg2 import EBookStore, Catalog, Customer, EBook, ShoppingCart, Order, Invoice, Discount

# Test Case 1: Initialize EBookStore and Add Catalog
store = EBookStore("The Great E-books Store", "123 Book Street")
catalog = store._EBookStore__catalog  # Accessing catalog through private attribute for testing
print("Initialized EBookStore:", store)

# Test Case 2: Add, Modify, and Remove a New E-Book in the Catalog
ebook1 = EBook("Python Programming", "Ahmed Alshehi", 30.0, "Education", "2023-01-01")
catalog.add_ebook(ebook1)

# Print catalog to confirm e-book addition
print("Catalog after adding eBook:", catalog)

# Modify the e-book details
ebook1.set_price(25.0)
ebook1.set_title("Advanced Python Programming")
print("Modified EBook:", ebook1)

# Remove the e-book from the catalog
catalog.remove_ebook(ebook1)
print("Catalog after removing eBook:", catalog)

# Test Case 3: Add, Modify, and Remove Customer Account
customer = Customer("Maitha Alteneiji", "maitha@example.com")
store.register_customer(customer)

# Modify customer details
customer.set_name("Malaak Alsuwaidi")
customer.set_contact_info("malaak@example.com")
print("Modified Customer:", customer)

# Test Case 4: Add and Remove E-Books in the Shopping Cart
ebook2 = EBook("Data Science Basics", "Saif Alshehi", 45.0, "Education", "2022-07-15")
ebook3 = EBook("Machine Learning Guide", "Hamdan Alketbi", 50.0, "Education", "2022-11-20")

# Add e-books to catalog and then to the shopping cart
catalog.add_ebook(ebook2)
catalog.add_ebook(ebook3)
customer.get_shopping_cart().add_item(ebook2)
customer.get_shopping_cart().add_item(ebook3)

# Print the shopping cart to confirm addition
print("Customer's Shopping Cart after adding eBooks:", customer.view_cart())

# Remove an e-book from the shopping cart
customer.get_shopping_cart().remove_item(ebook2)
print("Customer's Shopping Cart after removing an eBook:", customer.view_cart())

# Test Case 5: Search for an E-Book in the Catalog
searched_ebook = catalog.search_ebook("Machine Learning Guide")
print("Searched EBook:", searched_ebook)

# Test Case 6: Applying Discounts (Loyalty and Student Discounts)
discount = Discount(loyalty_discount=0.1, student_discount=0.15)

# Apply loyalty discount to an e-book price
loyalty_price = discount.apply_loyalty_discount(ebook3.get_price())
print("Price after loyalty discount:", loyalty_price)

# Apply student discount to an e-book price
student_price = discount.apply_student_discount(is_student=True, price=ebook3.get_price())
print("Price after student discount:", student_price)

# Test Case 7: Generate an Order and Invoice
order = Order()
order.add_item(ebook2)
order.add_item(ebook3)

# Calculate and print total before discounts
order_total_before_discount = order.calculate_total()
print("Order Total before any discounts:", order_total_before_discount)

# Apply loyalty discount to the order's total and calculate the final amount
order_total_with_loyalty_discount = discount.apply_loyalty_discount(order_total_before_discount)
print("Order Total with loyalty discount:", order_total_with_loyalty_discount)

# Generate an invoice based on the discounted total
invoice = Invoice(order_total_with_loyalty_discount)
print("Generated Invoice with loyalty discount:", invoice.generate_invoice_details())

# Test Case 8: Shopping Cart Functionality - Update Quantity (simulated as add/remove for single items)
cart = customer.get_shopping_cart()
cart.add_item(ebook2)
print("Shopping Cart after adding same item twice (for quantity simulation):", cart)
cart.remove_item(ebook2)
print("Shopping Cart after removing one instance (quantity simulated):", cart)



