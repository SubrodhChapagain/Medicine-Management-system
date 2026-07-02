
from invoice import generate_invoice

def sell_medicine(processed_data):
    """
    This file contains the two main operations of the MedStore system:
    selling medicines to customers and restocking medicines from vendors.
    It allows multiple transaction at once and generate single invoice.

    """
    try:
        customer_name = input("Enter customer name: ").lower()

        cart = []
        grand_total = 0 #to find to total price of multiple transaction

        while True:
            med_name = input("Enter medicine name: ").lower().replace(" ", "")

            found = False

            for each in processed_data:
                if med_name == each["Medicine Name"].lower().replace(" ", ""):
                    found = True

                    choice = input("Tablet or strip: ").lower()

                    if choice == "tablet":
                        qty = int(input("Enter number of tablets: "))

                        if qty <= each["No of tablets"]:
                            #each["No of tablets"] -= qty
                            price = each["Rate tablet"] * qty
                            
                            """provide 5% for strip, if user gives tablet compare with no.
                                of strip per tablet and provide discount thinking it as strip"""
                            
                            if qty % each["Tablets per strip"] == 0:
                                strip = qty // each["Tablets per strip"]

                                if strip>=2:
                                    discount = 0.05 * price

                                else:
                                    discount = 0
    
                            else:
                                discount = 0
                            
                            each["No of tablets"] -= qty
                            
                            price_after_dis = price - discount
                            
                            cart.append((each, "Tablet", qty, price_after_dis , discount))
                            
                            grand_total += price_after_dis
                        else:
                            print("Not enough stock!")

                    elif choice == "strip":
                        qty = int(input("Enter number of strips: "))

                        # to find the available stock of strip
                        available = each["No of tablets"] // each["Tablets per strip"]

                        if qty <= available:
                            each["No of tablets"] -= qty * each["Tablets per strip"]

                            price = each["Rate Strip"] * qty
                            
                            discount = 0.05 * price if qty >= 2 else 0
                            final_price = price - discount
                            
                            #Store data in cart for easier access for invoice
                            cart.append((each, "Strip", qty, final_price, discount))
                            
                            grand_total += final_price
                        else:
                            print("Not enough stock!")

                    else:
                        print("Invalid choice")

                    break

            if not found: #data handling for medicine name
                print("Medicine not found!")
                
            #Multiple medicine
            more = input("Add another medicine? (yes/no): ").lower()

            if more != "yes": 
                break

        generate_invoice("SALE", cart, grand_total, customer_name)

    except ValueError:
        print("Invalid input!")
    except ZeroDivisionError:
        print("Error: Tablets per strip cannot be zero!")




def restock_med(processed_data):
    """
    First I check if the medicine already exists in the stock list.
    If it EXISTS   : I just increase the tablet count and generate a restock invoice.
    If it does NOT : I ask for all the details (brand, rate, strip size) and add it
    as a new entry in processed_data, then generate a restock invoice.

    """
    try:
        vendor_name = input("Enter vendor name: ").lower()

        cart = []
        grand_total = 0

        while True:
            med_name = input("Enter medicine name: ").lower().replace(" ", "")
            found = False

            for each in processed_data:
                if med_name == each["Medicine Name"].lower().replace(" ", ""):
                    found = True

                    tablets = int(input("Enter number of tablets to restock: "))

                    each["No of tablets"] += tablets
                    price = tablets * each["Rate tablet"]

                    cart.append((each, "Tablet", tablets, price, 0))
                    grand_total += price

                    break

            if not found:
                print("Medicine not in stock! Adding as new medicine")

                brand = input("Enter brand name: ")
                tablets= int(input("Enter number of tablets: "))
                rate_tab = int(input("Enter rate per tablet: "))
                rate_strip= int(input("Enter rate per strip: "))
                per_strip= int(input("Enter tablets per strip: "))

                new_med = {
                    "Medicine Name": med_name,
                    "Brand Name": brand,
                    "No of tablets": tablets,
                    "Rate tablet": rate_tab,
                    "Rate Strip": rate_strip,
                    "Tablets per strip": per_strip
                }

                processed_data.append(new_med)

                price = tablets * rate_tab

                cart.append((new_med, "Tablet", tablets, price, 0))
                grand_total += price

            more = input("Add another medicine to restock? (yes/no): ").lower()
            if more != "yes":
                break

        #ONE invoice for whole transaction
        generate_invoice("RESTOCK", cart, grand_total, vendor_name)

    except ValueError:
        print("Invalid input!")
    except ZeroDivisionError:
        print("Error: Tablets per strip cannot be zero!")




