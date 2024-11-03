# Importing all classes from Assg2
from Assg2 import EBookStore, Catalog, Customer, EBook, ShoppingCart, Order, Invoice, Discount

# Test Case 1: Initialize EBookStore and Add Catalog
store_name = input("Enter the e-book store name: ")
store_address = input("Enter the e-book store address: ")
store = EBookStore(store_name, store_address)
catalog = store._EBookStore__catalog  # Accessing catalog through private attribute for testing
print("Initialized EBookStore:", store)

# Test Case 2: Add, Modify, and Remove a New E-Book in the Catalog
title = input("Enter the title of the e-book: ")
author = input("Enter the author of the e-book: ")
price = float(input("Enter the price of the e-book: "))
genre = input("Enter the genre of the e-book: ")
publication_date = input("Enter the publication date of the e-book (YYYY-MM-DD): ")
ebook1 = EBook(title, author, price, genre, publication_date)
catalog.add_ebook(ebook1)

# Print catalog to confirm e-book addition
print("Catalog after adding eBook:", catalog)

# Modify the e-book details
new_price = float(input("Enter the new price for the e-book: "))
new_title = input("Enter the new title for the e-book: ")
ebook1.set_price(new_price)
ebook1.set_title(new_title)
print("Modified EBook:", ebook1)

# Remove the e-book from the catalog
remove_confirm = input("Do you want to remove this e-book from the catalog? (yes/no): ")
if remove_confirm.lower() == "yes":
    catalog.remove_ebook(ebook1)
print("Catalog after removing eBook:", catalog)

# Test Case 3: Add, Modify, and Remove Customer Account
customer_name = input("Enter the customer's name: ")
customer_contact = input("Enter the customer's contact information: ")
customer = Customer(customer_name, customer_contact)
store.register_customer(customer)

# Modify customer details
new_customer_name = input("Enter the new name for the customer: ")
new_contact_info = input("Enter the new contact information for the customer: ")
customer.set_name(new_customer_name)
customer.set_contact_info(new_contact_info)
print("Modified Customer:", customer)

# Test Case 4: Add and Remove E-Books in the Shopping Cart
ebook2_title = input("Enter the title of another e-book: ")
ebook2_author = input("Enter the author of this e-book: ")
ebook2_price = float(input("Enter the price of this e-book: "))
ebook2_genre = input("Enter the genre of this e-book: ")
ebook2_pub_date = input("Enter the publication date of this e-book (YYYY-MM-DD): ")
ebook2 = EBook(ebook2_title, ebook2_author, ebook2_price, ebook2_genre, ebook2_pub_date)

ebook3_title = input("Enter the title of a third e-book: ")
ebook3_author = input("Enter the author of this e-book: ")
ebook3_price = float(input("Enter the price of this e-book: "))
ebook3_genre = input("Enter the genre of this e-book: ")
ebook3_pub_date = input("Enter the publication date of this e-book (YYYY-MM-DD): ")
ebook3 = EBook(ebook3_title, ebook3_author, ebook3_price, ebook3_genre, ebook3_pub_date)

# Add e-books to catalog and then to the shopping cart
catalog.add_ebook(ebook2)
catalog.add_ebook(ebook3)
customer.get_shopping_cart().add_item(ebook2)
customer.get_shopping_cart().add_item(ebook3)

# Print the shopping cart to confirm addition
print("Customer's Shopping Cart after adding eBooks:", customer.view_cart())

# Remove an e-book from the shopping cart
remove_ebook2 = input("Do you want to remove the second e-book from the shopping cart? (yes/no): ")
if remove_ebook2.lower() == "yes":
    customer.get_shopping_cart().remove_item(ebook2)
print("Customer's Shopping Cart after removing an eBook:", customer.view_cart())

# Test Case 5: Search for an E-Book in the Catalog
search_title = input("Enter the title of the e-book you want to search for in the catalog: ")
searched_ebook = catalog.search_ebook(search_title)
print("Searched EBook:", searched_ebook)

# Test Case 6: Applying Discounts (Loyalty and Student Discounts)
loyalty_discount = float(input("Enter the loyalty discount rate (as a decimal): "))
student_discount = float(input("Enter the student discount rate (as a decimal): "))
discount = Discount(loyalty_discount=loyalty_discount, student_discount=student_discount)

# Apply loyalty discount to an e-book price
loyalty_price = discount.apply_loyalty_discount(ebook3.get_price())
print("Price after loyalty discount:", loyalty_price)

# Apply student discount to an e-book price
is_student = input("Is the customer a student? (yes/no): ").lower() == "yes"
student_price = discount.apply_student_discount(is_student=is_student, price=ebook3.get_price())
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


