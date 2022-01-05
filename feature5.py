def take_id():
    return Customer.customer_counter


class Customer:
    customer_counter = 0

    def __init__(self, name, email_address, shipping_address, phone_number):
        Customer.customer_counter += 1
        self.id = Customer.customer_counter
        string_lst = name.split(" ")
        self.first_name = string_lst[0]
        self.last_name = string_lst[1]
        self.email_address = email_address
        self.shipping_address = shipping_address
        self.phone_number = phone_number

    def show_customer_info(self):
        print(f"""
        Customer id: {self.id}
        Name: {self.first_name + ' ' + self.last_name}
        Email address: {self.email_address}
        Shipping address: {self.shipping_address}
        Phone number: {self.phone_number}""")


customers = [
    Customer("Minh Nguyen", "s3931605@rmit.edu.vn", "ABCS", "9334378563485"),
    Customer("Minh Nguyen", "s3931605@rmit.edu.vn", "ABCS", "9334378563485")
]


def feature_5(customer_list):
    for i in customer_list:
        i.show_customer_info()

