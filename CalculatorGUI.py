import tkinter as tk
from tkinter import font
import tkinter.ttk as ttk


'''**************************************************************************************************************'''


#FORMATING
windowBg = "#deede9"
globalFont = "helvetica"
h1Size = 25
h2Size = 10
h2Color = "#2b393b"
inputSize = 15
dropdownColor = "#98c8bc"
errorColor="#b30000"
noteColor="grey"
calculateColor = "#9898c8"
eraseColor = "#bddbd4"


'''**************************************************************************************************************'''


#FUNCTIONS

#check if the inputs are valid to enable the calculation option
def enableCalculation(var, index, mode):
	try:
		float(entry1.get())								#check if entry1 is a float
		float(entry2.get())								#check if entry2 is a float
		if(operator.get()!="?"): 						#check if an operator is chosen
			calculateButton.configure(state="normal")
			message.configure(text="")
		else:
			calculateButton.configure(state="disabled")
			message.configure(text="Note: Choose an operator to proceed", foreground=noteColor)
	except:
		calculateButton.configure(state="disabled")
		message.configure(text="Note: Insert 2 numbers to proceed with the calculation", foreground=noteColor)

#******************************************************************************************************************#

#Calculate button actions
def calculateResult():
	#remove message
	message.configure(text="")

	#get value from entries
	num1 = float(entry1.get())
	num2 = float(entry2.get())

	switch={
			"+": addition,
			"-": subtraction,
			"x": multiplication,
			"/": division,
		}

	#set the value of equation as the result
	result = switch.get(operator.get())(num1, num2)
	if(result!="Error"):
		if(result.is_integer()):equation.set(str(int(result)))	#if the result is integer ➡ convert float to integer
		else:
			equation.set(str(round(result, 3)))					#if the result is float ➡ round with 3 decimals
			message.configure(text="Note: Float numbers are rounded to 3 decimal places", fg=noteColor)
	else: equation.set(str(result))								#the result is "Error"

def addition(num1, num2):
	return num1 + num2

def subtraction(num1, num2):
	return num1 - num2

def multiplication(num1, num2):
	return num1 * num2

def division(num1, num2):
	#check for incorrect entry (division by 0)
	if num2 == 0:
		message.configure(text="Error: You cannot divide by 0", foreground=errorColor)
		return "Error"
	return num1 / num2

#******************************************************************************************************************#

#Reset button actions
def clear():
	#remove message
	message.configure(text="")
	#remove input entries
	entry1.set("")
	entry2.set("")
	#remove the result
	equation.set("")
	#remove operator
	dropDown.set("?")


'''**************************************************************************************************************'''


# MAIN CODE
if __name__ == "__main__":

#GUI setup
	calculator = tk.Tk()								# create window
	calculator.configure(bg=windowBg, padx=80, pady=50)	# set the background colour
	calculator.title("Simple Calculator")				# set the title
	calculator.resizable(False, False)					#non-resizable window

#******************************************************************************************************************#

#Calculator style for TTK objects
	style = ttk.Style()
	style.theme_create('calculatorStyle')
	style.theme_use('calculatorStyle')
	
	#style for instructions (style is applied to all ttk.Label)
	style.configure("TLabel", font=(globalFont, h2Size), foreground=h2Color, background=windowBg)
	

	#style for dropdown (style is applied to all ttk.TCombobox)
	style.configure("TCombobox",
		#font color
		selectforeground="black",   
		#background colors
		selectbackground=dropdownColor, fieldbackground=dropdownColor, background= dropdownColor,
		padding=2)

	#style Listbox (dropdown options)
	calculator.option_add("*TCombobox*Listbox*Background", dropdownColor)
	calculator.option_add("*TCombobox*Listbox*Foreground", h2Color)
	calculator.option_add("*TCombobox*Listbox*Font", globalFont+' '+str(inputSize-1))
	calculator.option_add("*TCombobox*Listbox*Justify", "center")

#******************************************************************************************************************#

#Row 0: header
	tk.Label(calculator,text="Simple Calculator", font=(globalFont, h1Size), bg=windowBg
	).grid(row=0, columnspan=5, sticky="ew", pady=(0,20))

#Row 1-4: instructions  //allign:left
	ttk.Label(calculator,text="1. Choose operator").grid(row=1, columnspan=5, sticky="w")
	ttk.Label(calculator,text="2. Insert two intengers").grid(row=2, columnspan=5, sticky="w")
	ttk.Label(calculator,text="3. Press the \"Calculate\" button").grid(row=3, columnspan=5, sticky="w")
	ttk.Label(calculator,text="4. Press the \"Erase\" button to clear your inputs"
	).grid(row=4, columnspan=5, sticky="w", pady=(0, 30))

#Row 5: input number fields
	entry1 = tk.StringVar()
	entry1Box = tk.Entry(calculator, text=entry1, font=(globalFont, inputSize), justify="center", width=5, selectbackground=windowBg)
	entry1Box.grid(row=5, column=0, padx=3, pady=3, ipady=10, ipadx=10)

	entry2 = tk.StringVar()
	entry2Box = tk.Entry(calculator, text=entry2, font=(globalFont, inputSize), justify="center", width=5, selectbackground=windowBg)
	entry2Box.grid(row=5, column=2, padx=3, pady=3, ipady=10, ipadx=10)

#Row 5: dropdown menu for operator
	operator=tk.StringVar()											#chosen operator value

	dropDown = ttk.Combobox(calculator, textvariable=operator,		#create dropdown
	font=(globalFont, inputSize), width=3, justify="center")
	dropDown['values'] = ["+", "-", "x", "/"]						#add values to dropdown
	dropDown['state'] = 'readonly'									#cannot type other values
	dropDown.set("?")												#set "?" as the default value

	dropDown.grid(row=5, column=1, padx=3, pady=3, ipady=3)			#add dropdown to grid

#Row 5: result field
	tk.Label(calculator, text="=", font=(globalFont, inputSize), bg=windowBg
	).grid(row=5, column=3)
	equation = tk.StringVar()
	resultBox = tk.Entry(calculator, text=equation, font=(globalFont, inputSize), justify="center", width=7, selectbackground=windowBg, state="disabled"
	).grid(row=5, column=4, padx=3, pady=3, ipady=10, ipadx=10)
 
#Row 6: message text (used for note and error messages)
	message = tk.Label(calculator, text="Note: Insert 2 numbers to proceed with the calculation", fg=noteColor, bg=windowBg)
	message.grid(row=6, column=0, columnspan=5, pady=(10,60), sticky="w")

#Row 7: calculate button
	calculateButton = tk.Button(calculator, text="CALCULATE", command=calculateResult, state="disabled")	#calculation button is pre-disabled
	calculateButton.grid(row=7, columnspan=3, column=0, padx=(0,5), sticky="ew")
	calculateButton.configure(bg=calculateColor, activebackground=calculateColor, padx=10, pady=10, font=(globalFont, h2Size), justify="center")
	#check if we can enable the calculation button
	operator.trace("w", enableCalculation)
	entry1.trace("w", enableCalculation)
	entry2.trace("w", enableCalculation)

#Row 7: erase button
	eraseButton = tk.Button(calculator, text="Erase", command=clear)
	eraseButton.grid(row=7, columnspan=2, column=3, padx=(5,0), sticky="ew")
	eraseButton.configure(bg=eraseColor, activebackground=eraseColor, padx=10, pady=10, font=(globalFont, h2Size), justify="center")

#******************************************************************************************************************#

# start the GUI
	calculator.mainloop()