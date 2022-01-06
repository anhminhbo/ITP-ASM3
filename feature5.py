def take_id():
    return Customer.customer_counter


def reset_id():
    Customer.customer_counter = 0


class Customer:
    customer_counter = 0

    def __init__(self, name, email_address, shipping_address, phone_number, accumulated_amount=0):
        Customer.customer_counter += 1
        self.id = Customer.customer_counter
        string_lst = name.split(" ")
        self.first_name = string_lst[0]
        self.last_name = string_lst[1]
        self.email_address = email_address
        self.shipping_address = shipping_address
        self.phone_number = phone_number
        self.accumulated_amount = accumulated_amount

    def show_customer_info(self):
        print(f"""
        Customer id: {self.id}
        Name: {self.first_name + ' ' + self.last_name}
        Email address: {self.email_address}
        Shipping address: {self.shipping_address}
        Phone number: {self.phone_number}
        Accumulated amount of spent money: {self.accumulated_amount}""")


customers = []


def refresh_customer_data():
    cust = []
    reset_id()
    cus_data = open("customer.txt", "r")
    lines = cus_data.readlines()
    for line in lines:
        # read properties
        pro = line.split(" | ")
        cust.append(Customer(pro[0], pro[1], pro[2], pro[3], int(pro[4])))
    cus_data.close()
    return cust


def feature_5(customer_list):
    for i in customer_list:
        i.show_customer_info()


customers = refresh_customer_data()


# Make a file to store customer info
# Add 1 one property that is TotalProductsHasBeenBought
