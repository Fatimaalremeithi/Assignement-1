from datetime import datetime

class Customer:
    def __init__(self, customerID, name, email, phoneNumber, address):
        self.__customerID = customerID
        self.__name = name
        self.__email = email
        self.__phoneNumber = phoneNumber
        self.__address = address

    def getCustomerID(self):
        return self.__customerID

    def getName(self):
        return self.__name

    def getEmail(self):
        return self.__email

    def getPhoneNumber(self):
        return self.__phoneNumber

    def getAddress(self):
        return self.__address

    def displayCustomerDetails(self):
        print("Customer Details:")
        print(f"ID: {self.__customerID}")
        print(f"Name: {self.__name}")
        print(f"Email: {self.__email}")
        print(f"Phone: {self.__phoneNumber}")
        print(f"Address: {self.__address}")


class Order:
    def __init__(self, orderID, customerID, deliveryAddress, items, totalPrice):
        self.__orderID = orderID
        self.__customerID = customerID
        self.__deliveryAddress = deliveryAddress
        self.__items = items
        self.__totalPrice = totalPrice

    def getOrderID(self):
        return self.__orderID

    def getCustomerID(self):
        return self.__customerID

    def getDeliveryAddress(self):
        return self.__deliveryAddress

    def getItems(self):
        return self.__items

    def getTotalPrice(self):
        return self.__totalPrice

    def setTotalPrice(self, totalPrice):
        self.__totalPrice = totalPrice

    def displayOrderDetails(self):
        print("Order Details:")
        print(f"Order ID: {self.__orderID}")
        print(f"Customer ID: {self.__customerID}")
        print(f"Delivery Address: {self.__deliveryAddress}")
        print(f"Items: {self.__items}")
        print(f"Total Price: {self.__totalPrice}")


class DeliveryStaff:
    def __init__(self, staffID, name, contactNumber, vehicleType, availability):
        self.__staffID = staffID
        self.__name = name
        self.__contactNumber = contactNumber
        self.__vehicleType = vehicleType
        self.__availability = availability

    def getStaffID(self):
        return self.__staffID

    def getName(self):
        return self.__name

    def getContactNumber(self):
        return self.__contactNumber

    def getVehicleType(self):
        return self.__vehicleType

    def getAvailability(self):
        return self.__availability

    def displayStaffDetails(self):
        print("Delivery Staff Details:")
        print(f"Staff ID: {self.__staffID}")
        print(f"Name: {self.__name}")
        print(f"Contact Number: {self.__contactNumber}")
        print(f"Vehicle Type: {self.__vehicleType}")
        print(f"Availability: {self.__availability}")


class Item:
    def __init__(self, itemID, description, unitPrice, quantity, category):
        self.__itemID = itemID
        self.__description = description
        self.__unitPrice = unitPrice
        self.__quantity = quantity
        self.__category = category

    def getItemID(self):
        return self.__itemID

    def getDescription(self):
        return self.__description

    def getUnitPrice(self):
        return self.__unitPrice

    def getQuantity(self):
        return self.__quantity

    def getCategory(self):
        return self.__category

    def displayItemDetails(self):
        print("Item Details:")
        print(f"Item ID: {self.__itemID}")
        print(f"Description: {self.__description}")
        print(f"Unit Price: {self.__unitPrice}")
        print(f"Quantity: {self.__quantity}")
        print(f"Category: {self.__category}")


# Create a Customer object
customer = Customer(
    customerID=1,
    name="Fatima ALremeithi",
    email="Fatimaalremeithii@gmail.com",
    phoneNumber="055-550-3075",
    address="31 MBZ, 10, UAE"
)

# Create Item objects
item1 = Item(
    itemID="ITM200",
    description="WaterBottle",
    unitPrice=10.00,
    quantity=1,
    category="Object"
)

item2 = Item(
    itemID="ITM500",
    description="Shorts",
    unitPrice=100.00,
    quantity=5,
    category="Fashion"
)

item3 = Item(
    itemID="ITM399",
    description="Shirts",
    unitPrice=100.00,
    quantity=5,
    category="Fashion"
)

item4 = Item(
    itemID="ITM400",
    description="PJ's",
    unitPrice=100.00,
    quantity=10,
    category="Fashion"
)

# Create an Order object
order = Order(
    orderID="101",
    customerID=1,
    deliveryAddress="Shein",
    items=[item1, item2, item3, item4],
    totalPrice=0  # Will be calculated later
)

# Create a DeliveryStaff object
delivery_staff = DeliveryStaff(
    staffID=201,
    name="Ahmed",
    contactNumber="050-555-5555",
    vehicleType="Truck",
    availability="Available"
)

# Function to calculate the total price of the order
def calculate_total_price(order):
    total = 0
    for item in order.getItems():
        total += item.getUnitPrice() * item.getQuantity()
    return total

# Set the total price of the order
order.setTotalPrice(calculate_total_price(order))

# Function to generate and display the delivery note
def generate_delivery_note(customer, order, delivery_staff):
    print("Delivery Note")
    print("Thank you for using our delivery service! Please print your delivery receipt and present it upon receiving your items.\n")

    # Recipient Details
    print("Recipient Details:")
    print(f"Name: {customer.getName()}")
    print(f"Contact: {customer.getEmail()}")
    print(f"Delivery Address: {customer.getAddress()}\n")

    # Delivery Information
    print("Delivery Information:")
    print(f"Order Number: {order.getOrderID()}")
    print(f"Reference Number: DN-2025-001")
    print(f"Delivery Date: {datetime.now().strftime('%B %d, %Y')}")
    print(f"Delivery Method: Courier\n")

    # Package Dimensions
    print("Package Dimensions:")
    print(f"Total Weight: 7 kg\n")

    # Summary of Items Delivered
    print("Summary of Items Delivered:")
    print(f"{'Item Code':<10} {'Description':<25} {'Quantity':<10} {'Unit Price (AED)':<15} {'Total Price (AED)':<15}")
    for item in order.getItems():
        total_price = item.getUnitPrice() * item.getQuantity()
        print(f"{item.getItemID():<10} {item.getDescription():<25} {item.getQuantity():<10} {item.getUnitPrice():<15.2f} {total_price:<15.2f}")

    # Subtotal, Taxes, and Total Charges
    subtotal = order.getTotalPrice()
    taxes = subtotal * 0.05  # Assuming 5% tax
    total_charges = subtotal + taxes

    print(f"\nSubtotal: AED {subtotal:.2f}")
    print(f"Taxes and Fees: AED {taxes:.2f}")
    print(f"Total Charges: AED {total_charges:.2f}")

# Generate and display the delivery note
generate_delivery_note(customer, order, delivery_staff)