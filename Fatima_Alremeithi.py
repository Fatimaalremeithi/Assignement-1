class Customer:
    def __init__(self, customerID, name, email, phoneNumber, address):
        """
        Constructor for the Customer class.
        :param customerID: Unique identifier for the customer.
        :param name: Name of the customer.
        :param email: Email address of the customer.
        :param phoneNumber: Contact number of the customer.
        :param address: Delivery address of the customer.
        """
        self.__customerID = customerID  # Private attribute
        self.__name = name              # Private attribute
        self.__email = email            # Private attribute
        self.__phoneNumber = phoneNumber # Private attribute
        self.__address = address        # Private attribute

    # Getters
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

    # Setters
    def setName(self, name):
        self.__name = name

    def setEmail(self, email):
        self.__email = email

    def setPhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    def setAddress(self, address):
        self.__address = address

    # Other Functions
    def placeOrder(self):
        """
        Place a delivery order.
        """
        pass  # To be implemented

    def trackDelivery(self):
        """
        Track the status of a delivery.
        """
        pass  # To be implemented

    def displayCustomerDetails(self):
        """
        Display all customer details.
        """
        print("Customer Details:")
        print(f"ID: {self.__customerID}")
        print(f"Name: {self.__name}")
        print(f"Email: {self.__email}")
        print(f"Phone: {self.__phoneNumber}")
        print(f"Address: {self.__address}")


class Order:
    def __init__(self, orderID, customerID, deliveryAddress, items, totalPrice):
        """
        Constructor for the Order class.
        :param orderID: Unique identifier for the order.
        :param customerID: ID of the customer who placed the order.
        :param deliveryAddress: Address where the order will be delivered.
        :param items: List of items in the order.
        :param totalPrice: Total price of the order.
        """
        self.__orderID = orderID          # Private attribute
        self.__customerID = customerID    # Private attribute
        self.__deliveryAddress = deliveryAddress # Private attribute
        self.__items = items              # Private attribute
        self.__totalPrice = totalPrice    # Private attribute

    # Getters
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

    # Setters
    def setDeliveryAddress(self, deliveryAddress):
        self.__deliveryAddress = deliveryAddress

    def setItems(self, items):
        self.__items = items

    def setTotalPrice(self, totalPrice):
        self.__totalPrice = totalPrice

    # Other Functions
    def calculateTotalPrice(self):
        """
        Calculate the total price of the order.
        """
        pass  # To be implemented

    def generateDeliveryNote(self):
        """
        Generate a delivery note for the order.
        """
        pass  # To be implemented

    def displayOrderDetails(self):
        """
        Display all order details.
        """
        print("Order Details:")
        print(f"Order ID: {self.__orderID}")
        print(f"Customer ID: {self.__customerID}")
        print(f"Delivery Address: {self.__deliveryAddress}")
        print(f"Items: {self.__items}")
        print(f"Total Price: {self.__totalPrice}")


class DeliveryStaff:
    def __init__(self, staffID, name, contactNumber, vehicleType, availability):
        """
        Constructor for the DeliveryStaff class.
        :param staffID: Unique identifier for the delivery staff.
        :param name: Name of the delivery staff.
        :param contactNumber: Contact number of the delivery staff.
        :param vehicleType: Type of vehicle used for delivery.
        :param availability: Availability status of the staff.
        """
        self.__staffID = staffID          # Private attribute
        self.__name = name                # Private attribute
        self.__contactNumber = contactNumber # Private attribute
        self.__vehicleType = vehicleType # Private attribute
        self.__availability = availability # Private attribute

    # Getters
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

    # Setters
    def setName(self, name):
        self.__name = name

    def setContactNumber(self, contactNumber):
        self.__contactNumber = contactNumber

    def setVehicleType(self, vehicleType):
        self.__vehicleType = vehicleType

    def setAvailability(self, availability):
        self.__availability = availability

    # Other Functions
    def updateDeliveryStatus(self):
        """
        Update the status of a delivery.
        """
        pass  # To be implemented

    def displayStaffDetails(self):
        """
        Display all staff details.
        """
        print("Delivery Staff Details:")
        print(f"Staff ID: {self.__staffID}")
        print(f"Name: {self.__name}")
        print(f"Contact Number: {self.__contactNumber}")
        print(f"Vehicle Type: {self.__vehicleType}")
        print(f"Availability: {self.__availability}")


class Item:
    def __init__(self, itemID, description, unitPrice, quantity, category):
        """
        Constructor for the Item class.
        :param itemID: Unique identifier for the item.
        :param description: Description of the item.
        :param unitPrice: Price per unit of the item.
        :param quantity: Quantity of the item in stock.
        :param category: Category of the item (e.g., electronics, furniture).
        """
        self.__itemID = itemID            # Private attribute
        self.__description = description  # Private attribute
        self.__unitPrice = unitPrice      # Private attribute
        self.__quantity = quantity        # Private attribute
        self.__category = category        # Private attribute

    # Getters
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

    # Setters
    def setDescription(self, description):
        self.__description = description

    def setUnitPrice(self, unitPrice):
        self.__unitPrice = unitPrice

    def setQuantity(self, quantity):
        self.__quantity = quantity

    def setCategory(self, category):
        self.__category = category

    # Other Functions
    def updateQuantity(self):
        """
        Update the quantity of the item in stock.
        """
        pass  # To be implemented

    def displayItemDetails(self):
        """
        Display all item details.
        """
        print("Item Details:")
        print(f"Item ID: {self.__itemID}")
        print(f"Description: {self.__description}")
        print(f"Unit Price: {self.__unitPrice}")
        print(f"Quantity: {self.__quantity}")
        print(f"Category: {self.__category}")

if __name__ == "__main__":
    # Create a Customer object
    customer = Customer(1, "Fatima Alremeithi", "Fatimaalremeithii@gmail.com", "0555503075", "37 MBZ,10,UAE")
    customer.displayCustomerDetails()

    # Create an Order object
    order = Order(101, 1, "Shein", ["WaterBottle","shorts","Shirts","PJ's"], 175.00)
    order.displayOrderDetails()

    # Create a DeliveryStaff object
    delivery_staff = DeliveryStaff(201, "Ahmed", "05055555", "Truck", "Available")
    delivery_staff.displayStaffDetails()

    # Create an Item object
    item = Item(300, "WaterBottle", 10.00, 1, "Object")
    item.displayItemDetails()
    item = Item(500, "Shorts", 100.00, 5, "Fashion")
    item.displayItemDetails()
    item = Item(399, "Shirts", 100.00, 5, "Fashion")
    item.displayItemDetails()
    item = Item(400, "PJ's", 100.00, 10, "Fashion")
    item.displayItemDetails()