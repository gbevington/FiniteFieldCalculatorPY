import tkinter as tk

class NIST_prime_form(tk.Toplevel):  
    def __init__(self, main):
        super().__init__(main)
        self.title("NIST Prime Numbers")
        self._initialize_ui()

    def _initialize_ui(self):
            # Define buttons
            btnP192 = tk.Button(self, text="p192", command=self.btn_p192_click)
            btnP192.grid(row=0, column=0, padx=5, pady=5)
            btnP224 = tk.Button(self, text="p224", command=self.btn_p224_click)
            btnP224.grid(row=1, column=0, padx=5, pady=5)
            btnP256 = tk.Button(self, text="p256", command=self.btn_p256_click)
            btnP256.grid(row=2, column=0, padx=5, pady=5)
            btnP384 = tk.Button(self, text="p384", command=self.btn_p384_click)
            btnP384.grid(row=3, column=0, padx=5, pady=5)
            btnP521 = tk.Button(self, text="p521", command=self.btn_p521_click)
            btnP521.grid(row=4, column=0, padx=5, pady=5)

    def btn_p192_click(self):
        # Define the action for the button click here
        print("Button clicked!")
    
    def btn_p224_click(self):
        # Define the action for the button click here
        print("Button clicked!")

    def btn_p256_click(self):
        # Define the action for the button click here
        print("Button clicked!")

    def btn_p384_click(self):
        # Define the action for the button click here
        print("Button clicked!")
    
    def btn_p521_click(self):
        # Define the action for the button click here
        print("Button clicked!")