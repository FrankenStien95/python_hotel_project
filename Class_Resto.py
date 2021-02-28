class Resto:
    tax = 0.18
    veg_menu = {"Palak Paneer" :350, "Paneer Masala" :300, "Shahi Paneer" : 350 , "Kolhapuri" :200, "Paneer Tikka" :150,
                "Mutter Paneer" :300, "Kaju Masala" :400, "Baigan Fry" :100, "Daal Tadka" :150, "Daal Makhani" :200,
                "Plain Daal" :100, "Fry Papad" : 20}

    nonveg_menu = {"Chicken" :250, "Butter Chicken" :300, "Chicken Special" :350, "Chicken Tikka" :300,"Fish Masala" :400,
                    "Fish Fry" :200, "Pomfret Fry" :500, "Plain Prawn" :200, "Prawn Curry" :250, "Prawn Pulao" :200,
                    "Lamb" :700, "Steak" :400}

    print("Welcome To Shaikh's Restaurant")

    menu_type = input("Enter the type of the menu :")

    Veg_Menu_Cost = 0

    Nonveg_Menu_Cost = 0

    if menu_type == "veg":
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
        Plain_Daal = int(input("Plain Daal [Rs. 100] :"))
        Plain_Daal_Cost = veg_menu ["Plain Daal"] * Plain_Daal
        Fry_Papad = int(input("Fry Papad [Rs. 20] :"))
        Fry_Papad_Cost = veg_menu ["Fry Papad"] * Fry_Papad
        cost_of_all = Palak_Paneer_Cost + Paneer_Masala_Cost + Shahi_Paneer_Cost + kolhapuri_Cost + Paneer_Tikka_Cost + Mutter_Paneer_Cost + Kaju_Masala_Cost + Baigan_Fry_Cost + Daal_Tadka_Cost + Daal_Makhani_Cost + Plain_Daal_Cost + Fry_Papad_Cost
        Veg_Menu_Cost = (cost_of_all) + ((cost_of_all)  * 18 // 100)
        nonvegalso = input("Do you Want Non Veg Too !!")
        if nonvegalso == "yes":
            print("Please enter the following dish quantity ")
            Chicken = int(input("Chicken [Rs. 250] :"))
            Chicken_Cost = nonveg_menu["Chicken"] * Chicken
            Chicken_Special = int(input("Chicken Special [Rs. 350] :"))
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
            Prawn_Pulao = int(input("Prawn Pulao [Rs. 200] :"))
            Prawn_Pulao_Cost = nonveg_menu ["Prawn Pulao"] * Prawn_Pulao
            Lamb = int(input("Lamb [Rs. 700] :"))
            Lamb_Cost = nonveg_menu ["Lamb"] * Lamb
            Steak = int(input("Steak [Rs. 400] :"))
            Steak_Cost = nonveg_menu ["Steak"] * Steak
            cost_of_all = Chicken_Cost + Chicken_Special_Cost + Chicken_Tikka_Cost + Fish_Masala_Cost + Fish_Fry_Cost + Pomfret_Fry_Cost + Plain_Prawn_Cost + Prawn_Curry_Cost + Prawn_Pulao_Cost + Lamb_Cost + Steak_Cost
            Nonveg_Menu_Cost = (cost_of_all) + ((cost_of_all)  * 18 // 100)
            total_cost = Veg_Menu_Cost + Nonveg_Menu_Cost
            print("The total amount is :", total_cost )
        else:
            total_cost = Veg_Menu_Cost  
            print("The total amount is :", total_cost )
            print("Thankyou Please Visit Again...")
        

    elif menu_type == "nonveg":
        print("Please enter the following dish quantity ")
        Chicken = int(input("Chicken [Rs. 250] :"))
        Chicken_Cost = nonveg_menu["Chicken"] * Chicken
        Chicken_Special = int(input("Chicken Special [Rs. 350]"))
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
        Prawn_Pulao = int(input("Prawn Pulao [Rs. 200] :"))
        Prawn_Pulao_Cost = nonveg_menu ["Prawn Pulao"] * Prawn_Pulao
        Lamb = int(input("Lamb [Rs. 700] :"))
        Lamb_Cost = nonveg_menu ["Lamb"] * Lamb
        Steak = int(input("Steak [Rs. 400] :"))
        Steak_Cost = nonveg_menu ["Steak"] * Steak
        cost_of_all = Chicken_Cost + Chicken_Special_Cost + Chicken_Tikka_Cost + Fish_Masala_Cost + Fish_Fry_Cost + Pomfret_Fry_Cost + Plain_Prawn_Cost + Prawn_Curry_Cost + Prawn_Pulao_Cost + Lamb_Cost + Steak_Cost
        Nonveg_Menu_Cost = (cost_of_all) + ((cost_of_all)  * 18 // 100)
        vegalso = input("Do you Want Veg Too !!")
        if vegalso == "yes":
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
            Plain_Daal = int(input("Plain Daal [Rs. 100] :"))
            Plain_Daal_Cost = veg_menu ["Plain Daal"] * Plain_Daal
            Fry_Papad = int(input("Fry Papad [Rs. 20] :"))
            Fry_Papad_Cost = veg_menu ["Fry Papad"] * Fry_Papad
            cost_of_all = Palak_Paneer_Cost + Paneer_Masala_Cost + Shahi_Paneer_Cost + kolhapuri_Cost + Paneer_Tikka_Cost + Mutter_Paneer_Cost + Kaju_Masala_Cost + Baigan_Fry_Cost + Daal_Tadka_Cost + Daal_Makhani_Cost + Plain_Daal_Cost + Fry_Papad_Cost
            Veg_Menu_Cost = (cost_of_all) + ((cost_of_all)  * 18 // 100)
            total_cost = Nonveg_Menu_Cost + Veg_Menu_Cost
            print("The total amount is :", total_cost )
        else:
            total_cost = Nonveg_Menu_Cost  
            print("The total amount is :", total_cost )
            print("Thankyou Please Visit Again...")
    else:
        print("Please enter the correct menu")


b = Resto()