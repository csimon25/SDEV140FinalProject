# Program name: dollar.py
# Author: Chad Simon
# Date: 5/15/22
# Summary: Converts dollars to pesos and euros, or vice versa

# Import files
from breezypythongui import EasyFrame
import formatPrint

# Declare the dollars and initialize the main screen
class dollars(EasyFrame):
    def __init__ (self):
        
        EasyFrame.__init__(self, title = "Convert Dollars to Pesos")

        # Create the dollars to pesos label and text to people field in the first row
        self.dollarsPesosLabel = self.addLabel(text = "Enter the dollar to pesos:",
                                          row = 0, column = 0,
                                          sticky = "W")

        self.pesosField = self.addTextField(text = "",
                                            row = 0, column = 1)

        # Create the dollars label and euros text field in the second row
        self.dollarsEurosLabel = self.addLabel(text = "Enter the dollar to euros:",
                                           row = 1, column = 0)

        self.eurosField = self.addTextField(text = "",
                                            row = 1, column = 1)

        # Create the buttons in the third row
        self.dollarstopesos_button = self.addButton(text = "Convert dollars to pesos",
                                          row = 2, column = 0,
                                          command = self.convert_dollarstopesos)

        self.dollarstoeuros_button = self.addButton(text = "Convert dollars to euros",
                                          row = 2, column = 1,
                                          command = self.convert_dollarstoeuros)

    # Define functions
    def convert_dollarstopesos(self):
        self.dollars = float(self.pesosField.getText())
        self.pesos = (20.35 * self.dollars)
        self.pesosField.setText(formatPrint.formatPesos(self.pesos))

    def convert_dollarstoeuros(self):
        self.dollars = float(self.eurosField.getText())
        self.euros = self.dollars * 0.96
        self.eurosField.setText(formatPrint.formatEuros(self.euros))


# Start the main loop
def main():
    dollars().mainloop()
main()
        
    



        


