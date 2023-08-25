import tkinter as tk

class AccountingProgram(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Accounting Program")
        self.geometry("400x300")

        self.balance = 0.0
        self.data = {}

        self.create_ui()

    def create_ui(self):
        # Buy Product Section
        buy_frame = tk.LabelFrame(self, text="Buy Product")
        buy_frame.pack(pady=10)

        product_label = tk.Label(buy_frame, text="Product:")
        product_label.grid(row=0, column=0, padx=5, pady=5)
        self.product_entry = tk.Entry(buy_frame)
        self.product_entry.grid(row=0, column=1, padx=5, pady=5)

        price_label = tk.Label(buy_frame, text="Price:")
        price_label.grid(row=1, column=0, padx=5, pady=5)
        self.price_entry = tk.Entry(buy_frame)
        self.price_entry.grid(row=1, column=1, padx=5, pady=5)

        buy_button = tk.Button(buy_frame, text="Buy", command=self.buy_product)
        buy_button.grid(row=2, columnspan=2, padx=5, pady=5)

        # Sell Product Section
        sell_frame = tk.LabelFrame(self, text="Sell Product")
        sell_frame.pack(pady=10)

        sell_product_label = tk.Label(sell_frame, text="Product:")
        sell_product_label.grid(row=0, column=0, padx=5, pady=5)
        self.sell_product_entry = tk.Entry(sell_frame)
        self.sell_product_entry.grid(row=0, column=1, padx=5, pady=5)

        sell_price_label = tk.Label(sell_frame, text="Price:")
        sell_price_label.grid(row=1, column=0, padx=5, pady=5)
        self.sell_price_entry = tk.Entry(sell_frame)
        self.sell_price_entry.grid(row=1, column=1, padx=5, pady=5)

        sell_button = tk.Button(sell_frame, text="Sell", command=self.sell_product)
        sell_button.grid(row=2, columnspan=2, padx=5, pady=5)

        # Balance Section
        balance_frame = tk.LabelFrame(self, text="Balance")
        balance_frame.pack(pady=10)

        self.balance_label = tk.Label(balance_frame, text=f"Current Balance: {self.balance}")
        self.balance_label.pack(padx=5, pady=5)

    def buy_product(self):
        product = self.product_entry.get()
        price = float(self.price_entry.get())

        if product in self.data:
            self.data[product] += price
        else:
            self.data[product] = price

        self.balance += price
        self.update_balance()

    def sell_product(self):
        product = self.sell_product_entry.get()
        price = float(self.sell_price_entry.get())

        if product in self.data:
            self.data[product] -= price
            self.balance -= price
            self.update_balance()

            if self.data[product] <= 0:
                del self.data[product]

    def update_balance(self):
        self.balance_label.config(text=f"Current Balance: {self.balance}")

if __name__ == "__main__":
    app = AccountingProgram()
    app.mainloop()

