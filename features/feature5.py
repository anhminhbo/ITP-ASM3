class Customer:
    def __init__(self, name, email_address, shipping_address, phone_number):
        self.name = name
        self.email_address = email_address
        self.shipping_address = shipping_address
        self.phone_number = phone_number

    def show_customer_info(self):
        print(f"""
        Name: {self.name}
        Email address: {self.email_address}
        Shipping address: {self.shipping_address}
        Phone number: {self.phone_number}
        """)


customers = [Customer("Minh", "s3931605@rmit.edu.vn", "ABCS", "9334378563485")]


def feature_5(customer_list):
    for i in customer_list:
        i.show_customer_info()
