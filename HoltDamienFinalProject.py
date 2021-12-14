import tkinter as tk
#Program
def CafeCalculator():
    #GUI
    window1 = tk.Tk() #Creates the first window
    window1.title("CoffeeCafe Calculator") #Names it
    window1.geometry=("800x800") #Sets the size
        #Creates the Window for the program.
    #Declarations
    global Price #Makes the Starting Price Global
    Price = 0 #Sets the starting Price to 0
        #Sets up the delcarations for the Prices.

    #Labels
    StartingLabel = tk.Label(window1, text="Enter the Drink Type: Coffee, Latte, or Iced Coffee")
    PriceLabel = tk.Label(window1, text=Price)
    TextLabel = tk.Label(window1, text="The current Price is: ")
        #Creates the Labels within the Program
    
    #Drink and Add-Ons
    def CoffeePrice():
        global Price
        Price = float(1.00)
        PriceLabel.configure(text= (float(Price)))
    def LattePrice():
        global Price
        Price = float(2.00)
        PriceLabel.configure(text= (float(Price)))
    def IcedCoffeePrice():
        global Price
        Price = float(1.25)
        PriceLabel.configure(text= (float(Price)))
    def MilkPrice():
        global Price
        Price = Price + 0.25
        PriceLabel.configure(text= (float(Price)))
    def CreamerPrice():
        global Price
        Price = Price + 0.35
        PriceLabel.configure(text= (float(Price)))
    def ExpressoPrice():
        global Price
        Price = Price + 0.40
        PriceLabel.configure(text= (float(Price)))
    def CinnamonPrice():
        global Price
        Price = Price + 0.30
        PriceLabel.configure(text= (float(Price)))
        #Creates the Functions for the Drinks and Add-Ons that sets and modifies prices.
    #Exit Button
    def Exit():
        window1.destroy()
        #Creates the Exit Button
    #Buttons
    CoffeeButton = tk.Button(window1, text="Coffee", command=CoffeePrice)
    LatteButton = tk.Button(window1, text="Latte", command=LattePrice)
    IcedCoffeeButton = tk.Button(window1, text="IcedCoffee", command=IcedCoffeePrice)
    MilkButton = tk.Button(window1, text="Milk", command=MilkPrice)
    CreamerButton = tk.Button(window1, text="Creamer", command=CreamerPrice)
    ExpressoButton = tk.Button(window1, text="Expresso", command= ExpressoPrice)
    CinnamonButton = tk.Button(window1, text="Cinnamon", command=CinnamonPrice)
    ExitButton = tk.Button(window1, text="EXIT", command=Exit) 
        #Creates the Buttons for the GUI
    #GUI Placement
    StartingLabel.place(x= 80, y=50)
    CoffeeButton.place(x= 80, y= 100)
    LatteButton.place(x= 150,y= 100)
    IcedCoffeeButton.place(x= 200, y=100)
    MilkButton.place(x = 80, y= 175)
    CreamerButton.place(x= 125, y= 175)
    ExpressoButton.place(x = 195, y= 175)
    CinnamonButton.place(x= 275, y= 175)
    TextLabel.place(x = 75, y = 250)
    PriceLabel.place(x = 195, y=250)
    ExitButton.place(x = 15, y = 15)
        #Places the GUI Elements in the appropriate areas.
    window1.mainloop()
CafeCalculator()