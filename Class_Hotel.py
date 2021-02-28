class Resto:
    def veg_menu(s):
        veg_menu= {"Palak Paneer" :350, "Paneer Masala" :300, "Shahi Paneer" :350, "Kolhapuri" :200, 
                   "Paneer Tikka" :150, "Mutter Paneer" :300, "Kaju Masala" :400, "Baigan Fry" :100, 
                   "Daal Tadka" :150, "Daal Makhani" :200}
        print("Please enter the following dish quantity ")
        Palak_Paneer = int(input("Palak Paneer [Rs. 350] :"))
        Palak_Paneer_Cost = veg_menu["Palak Paneer"] * Palak_Paneer
        Paneer_Masala = int(input("Paneer Masala [Rs. 300] :"))
        Paneer_Masala_Cost = veg_menu["Paneer Masala"] * Paneer_Masala
        Shahi_Paneer = int(input("Shahi Paneer [Rs. 350] :"))
        Shahi_Paneer_Cost = veg_menu["Shahi Paneer"] * Shahi_Paneer
        kolhapuri = int(input("kolhapuri [Rs. 200] :"))
        kolhapuri_Cost = veg_menu["Kolhapuri"] * kolhapuri
        Paneer_Tikka = int(input("Paneer Tikka [Rs. 150] :"))
        Paneer_Tikka_Cost = veg_menu["Paneer Tikka"] * Paneer_Tikka
        Mutter_Paneer = int(input("Mutter Paneer [Rs. 300] :"))
        Mutter_Paneer_Cost = veg_menu ["Mutter Paneer"] * Mutter_Paneer
        Kaju_Masala = int(input("Kaju Masala [Rs. 400] :"))
        Kaju_Masala_Cost = veg_menu ["Kaju Masala"] * Kaju_Masala
        Baigan_Fry = int(input("Baigan Fry [Rs. 100] :"))
        Baigan_Fry_Cost = veg_menu ["Baigan Fry"] * Baigan_Fry
        Daal_Tadka = int(input("Daal Tadka [Rs. 150] :"))
        Daal_Tadka_Cost = veg_menu ["Daal Tadka"] * Daal_Tadka
        Daal_Makhani = int(input("Daal Makhani [Rs. 200] :"))
        Daal_Makhani_Cost = veg_menu ["Daal Makhani"] * Daal_Makhani
        cost_of_all = Palak_Paneer_Cost + Paneer_Masala_Cost + Shahi_Paneer_Cost + kolhapuri_Cost + Paneer_Tikka_Cost + Mutter_Paneer_Cost +Kaju_Masala_Cost +Baigan_Fry_Cost +Daal_Tadka_Cost + Daal_Makhani_Cost
        s.Veg_Menu_Cost = (cost_of_all) + ((cost_of_all)  * 18 // 100)
        non_vegalso = int(input("Do you Want Non Veg Too !! Enter 1 for YES or 2 for NO!!"))
        if non_vegalso == 1:
            s.nonveg_menu()
            s.total_cost = s.Veg_Menu_Cost + s.Nonveg_Menu_Cost
        else:
            s.total_cost = s.Veg_Menu_Cost    

    def nonveg_menu(s):
        nonveg_menu = {"Chicken" :250, "Chicken Special" :300 , "Chicken Tikka" :300, "Fish Masala" :400,
                       "Fish Fry" :200, "Pomfret Fry" :500, "Plain Prawn" :200, "Prawn Curry" :250}
        print("Please enter the following dish quantity ")
        Chicken = int(input("Chicken [Rs. 250] :"))
        Chicken_Cost = nonveg_menu["Chicken"] * Chicken
        Chicken_Special = int(input("Chicken Special [Rs. 300] :"))
        Chicken_Special_Cost = nonveg_menu ["Chicken Special"] * Chicken_Special
        Chicken_Tikka = int(input("Chicken Tikka [Rs. 300] :"))
        Chicken_Tikka_Cost = nonveg_menu ["Chicken Tikka"] * Chicken_Tikka
        Fish_Masala = int(input("Fish Masala [Rs. 400] :"))
        Fish_Masala_Cost = nonveg_menu["Fish Masala"] * Fish_Masala
        Fish_Fry = int(input("Fish Fry [Rs. 200] :"))
        Fish_Fry_Cost = nonveg_menu ["Fish Fry"] * Fish_Fry
        Pomfret_Fry = int(input("Pomfret Fry [Rs. 500] :"))
        Pomfret_Fry_Cost = nonveg_menu ["Pomfret Fry"] * Pomfret_Fry
        Plain_Prawn = int(input("Plain Prawn [Rs. 200] :"))
        Plain_Prawn_Cost = nonveg_menu ["Plain Prawn"] * Plain_Prawn
        Prawn_Curry = int(input("Prawn Curry [Rs. 250] :"))
        Prawn_Curry_Cost = nonveg_menu ["Prawn Curry"] * Prawn_Curry
        cost_of_all = Chicken_Cost + Chicken_Special_Cost + Chicken_Tikka_Cost + Fish_Masala_Cost + Fish_Fry_Cost + Pomfret_Fry_Cost + Plain_Prawn_Cost + Prawn_Curry_Cost
        s.Nonveg_Menu_Cost = (cost_of_all) + ((cost_of_all)  * 18 // 100)
        vegalso = int(input("Do you Want Veg Too !! Enter 1 for YES or 2 for NO!!"))
        if vegalso == 1:
            s.veg_menu()
            s.total_cost = s.Veg_Menu_Cost + s.Nonveg_Menu_Cost
        else:
            s.total_cost = s.Nonveg_Menu_Cost      
        
    def Menu(s):
        print("1. veg_menu")
        print("2. nonveg_menu")
        print("3. Quit")
        while True:
            try:
                selection = int(input("Enter your chioce: "))
                if selection == 1:
                    s.veg_menu()
                    print("The total amount is :", s.total_cost )
                    break
                elif selection == 2:
                    s.nonveg_menu()
                    print("The total amount is :", s.total_cost )
                    break
                else:
                    print("Enter the valid choice, Enter 1-3")
                    s.Menu()
            except ValueError:
                print("Invalid choice. Enter 1-3")
        exit

hotel = Resto()
hotel.Menu()
