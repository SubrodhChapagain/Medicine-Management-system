
"""
It connects all the other modules together and controls the main program loop.
The program keeps running until the user types 'exit'.

"""
from read import read_medical_data
from write import save_report,save_to_database
from prints import print_stock_data
from operation import sell_medicine, restock_med


#path 
inputPath = "medical_data.txt"
outputPath = "medical_output.txt"
#outputPath = "medical_output.txt"


#get the values from read.py 
processed_data = read_medical_data(inputPath)


#display actual stock before use
print_stock_data(processed_data)



print("\nWelcome to MedStore Pvt. Ltd. Wholesale System")

while True:
    print("\n" + "=" * 50)
    print(" OPTIONS: sell | restock | exit")
    print("=" * 50)
    
    #for invoice generation
    choice = input("Enter your choice: ").lower().replace(" ", "")

    if choice == "sell":
        sell_medicine(processed_data)

    elif choice == "restock":
        restock_med(processed_data)

    elif choice == "exit":
        print("\nSaving stock and exiting.")
        save_to_database(inputPath, processed_data)
        save_report(outputPath , processed_data)
        break

    else:
        print("Invalid choice")
        continue
    
    #save after every transaction
    save_to_database(inputPath, processed_data)
    save_report(outputPath , processed_data)

    #now show the updated stock 
    print_stock_data(processed_data)

    

