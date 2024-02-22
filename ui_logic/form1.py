import tkinter as tk
from tkinter import messagebox

import math
import sys
import os

# Get the current directory of the script
current_dir = os.path.dirname(os.path.realpath(__file__))

# Get the parent directory (project root) and add it to the Python path
project_root = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.append(project_root)

from ui_logic.nist_prime_form import NIST_prime_form

from business_logic.validation import ValidationMethods
from business_logic.calculation import Calculation

class Form1(tk.Tk):  
    def __init__(self):
        super().__init__()
        self.title("Finite Field Calculator")
        self._initialize_ui()
        self.root = self #!!! for opening nist window

    def _initialize_ui(self):
        # Define labels
        label1 = tk.Label(self, text="Prime # :")
        label1.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        label2 = tk.Label(self, text="A:")
        label2.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        label3 = tk.Label(self, text="B:")
        label3.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        label4 = tk.Label(self, text="R:")
        label4.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        label5 = tk.Label(self, text="Output:")
        label5.grid(row=4, column=0, padx=5, pady=5, sticky=tk.W)

        # Define textboxes
        self.txtPrime = tk.Entry(self)
        self.txtPrime.grid(row=0, column=1, padx=5, pady=5)
        self.txtOp1 = tk.Entry(self)
        self.txtOp1.grid(row=1, column=1, padx=5, pady=5)
        self.txtOp2 = tk.Entry(self)
        self.txtOp2.grid(row=2, column=1, padx=5, pady=5)
        self.txtExpo = tk.Entry(self)
        self.txtExpo.grid(row=3, column=1, padx=5, pady=5)
        self.txtResult = tk.Entry(self)
        self.txtResult.grid(row=4, column=1, padx=5, pady=5)

        # Define buttons
        btnAdd = tk.Button(self, text="A + B", command=self.btn_add_click)
        btnAdd.grid(row=5, column=0, padx=5, pady=5)
        btnSubtract = tk.Button(self, text="A - B", command=self.btn_subtract_click)
        btnSubtract.grid(row=5, column=1, padx=5, pady=5)
        btnMulti = tk.Button(self, text="A * B", command=self.btn_multi_click)
        btnMulti.grid(row=5, column=2, padx=5, pady=5)
        btnDiv = tk.Button(self, text="A / B", command=self.btn_div_click)
        btnDiv.grid(row=5, column=3, padx=5, pady=5)
        btnExponent = tk.Button(self, text="A ^ R", command=self.btn_exponent_click)
        btnExponent.grid(row=5, column=4, padx=5, pady=5)
        btnNIST = tk.Button(self, text="NIST Primes", command=self.btn_nist_click)
        btnNIST.grid(row=0, column=2, rowspan=2, padx=5, pady=5)

        # Disable other input fields initially
        self.txtOp1.config(state="disabled")
        self.txtOp2.config(state="disabled")

        # Wire up the event handler for the TextChanged event of txtPrime
        self.txtPrime.bind("<KeyRelease>", self.check_prime_validity)

    def check_prime_validity(self, event):
        input_value = self.txtPrime.get()
        # color in textbox in coral if number is prime
        try:
            prime_number = int(input_value)
            validator = ValidationMethods()
            is_prime_value = validator.is_prime(prime_number)
            self.txtPrime.config(bg="lightgreen" if is_prime_value else "lightcoral")
            self.txtOp1.config(state="normal" if is_prime_value else "disabled")
            self.txtOp2.config(state="normal" if is_prime_value else "disabled")
        except ValueError:
            self.txtPrime.config(bg="white")
            self.txtOp1.config(state="disabled")
            self.txtOp2.config(state="disabled")

    def btn_add_click(self):
        #get operand values
        primeNum = int(self.txtPrime.get())
        operand1 = int(self.txtOp1.get())
        operand2 = int(self.txtOp2.get())

        #use calculator to perform FF addition
        self.calculator = Calculation(primeNum)  # Create an instance of Calculation class
        result = self.calculator.add(operand1, operand2)

        #display result
        self.txtResult.delete(0, tk.END)#clear result box
        self.txtResult.insert(0, str(result))#insert new result in text box

    def btn_subtract_click(self):
        
        #get operand values
        primeNum = int(self.txtPrime.get())
        operand1 = int(self.txtOp1.get())
        operand2 = int(self.txtOp2.get())

        #use calculator to perform FF subtraction
        self.calculator = Calculation(primeNum)  # Create an instance of Calculation class
        result = self.calculator.subtract(operand1, operand2)

        #display result
        self.txtResult.delete(0, tk.END)#clear result box
        self.txtResult.insert(0, str(result))#insert new result in text box

    def btn_multi_click(self):
        
        #get operand values
        primeNum = int(self.txtPrime.get())
        operand1 = int(self.txtOp1.get())
        operand2 = int(self.txtOp2.get())

        #use calculator to perform FF multiplication
        self.calculator = Calculation(primeNum)  # Create an instance of Calculation class
        result = self.calculator.multiply(operand1, operand2)

        #display result
        self.txtResult.delete(0, tk.END)#clear result box
        self.txtResult.insert(0, str(result))#insert new result in text box

    def btn_div_click(self):
        
        #get input values
        primeNum = int(self.txtPrime.get())
        operand1 = int(self.txtOp1.get())
        operand2 = int(self.txtOp2.get())

        #use calculator to perform FF division
        self.calculator = Calculation(primeNum)  # Create an instance of Calculation class
        result = self.calculator.divide(operand1, operand2)

        #display result
        self.txtResult.delete(0, tk.END)#clear result box
        self.txtResult.insert(0, str(result))#insert new result in text box

    def btn_exponent_click(self):
         #get input values
        primeNum = int(self.txtPrime.get())
        operand1 = int(self.txtOp1.get())
        operand2 = int(self.txtExpo.get())
        
        #use calculator to perform FF exponentiation
        self.calculator = Calculation(primeNum)  # Create an instance of Calculation class
        result = self.calculator.exponentiate(operand1, operand2)

        #display result
        self.txtResult.delete(0, tk.END)#clear result box
        self.txtResult.insert(0, str(result))#insert new result in text box

    def btn_nist_click(self):
        # open NIST primes window
        nist_prime_form = NIST_prime_form(self.root)

if __name__ == "__main__":
    app = Form1()
    app.mainloop()