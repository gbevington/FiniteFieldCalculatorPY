import tkinter as tk

from business_logic.nist_prime_generator import NISTPrimesGenerator

class NIST_prime_form(tk.Toplevel):  
    def __init__(self, main):
        super().__init__(main)
        self.title("NIST Prime Numbers")
        self._initialize_ui()

        self.main = main

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
        #use NIST generator
        self.generator = NISTPrimesGenerator()  # Create an instance of NISTPrimesGenerator class
        result = self.generator.get_p192()

        #display result
        self.main.txtPrime.delete(0, tk.END)#clear result box
        self.main.txtPrime.insert(0, str(result))#insert new result in text box

    
    def btn_p224_click(self):
        #use NIST generator
        self.generator = NISTPrimesGenerator()  # Create an instance of NISTPrimesGenerator class
        result = self.generator.get_p224()

        #display result
        self.main.txtPrime.delete(0, tk.END)#clear result box
        self.main.txtPrime.insert(0, str(result))#insert new result in text box

    def btn_p256_click(self):
        #use NIST generator
        self.generator = NISTPrimesGenerator()  # Create an instance of NISTPrimesGenerator class
        result = self.generator.get_p256()

        #display result
        self.main.txtPrime.delete(0, tk.END)#clear result box
        self.main.txtPrime.insert(0, str(result))#insert new result in text box

    def btn_p384_click(self):
        #use NIST generator
        self.generator = NISTPrimesGenerator()  # Create an instance of NISTPrimesGenerator class
        result = self.generator.get_p384()

        #display result
        self.main.txtPrime.delete(0, tk.END)#clear result box
        self.main.txtPrime.insert(0, str(result))#insert new result in text box
    
    def btn_p521_click(self):
        #use NIST generator
        self.generator = NISTPrimesGenerator()  # Create an instance of NISTPrimesGenerator class
        result = self.generator.get_p251()

        #display result
        self.main.txtPrime.delete(0, tk.END)#clear result box
        self.main.txtPrime.insert(0, str(result))#insert new result in text box