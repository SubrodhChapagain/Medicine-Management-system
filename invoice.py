
import random, datetime
def generate_invoice(transaction_type, cart, grand_total, customer_name):
    """
    This moudle is used to generate invoice taking the details from operation.py
    the data includes processed data, type of transaction: restock or sell
    grand total price: total price of multiple transation at same time
    and customer name/vendor name
    """
    
    #generate random number between 10000, 99999
    bill_no = random.randint(10000, 99999)
     
    now = datetime.datetime.now() #current date and time 
    timestamp = now.strftime("%Y%m%d_%H%M%S")# format date and time

    prefix = "Sell" if transaction_type == "SALE" else "Restock"
    #for unique invoice name
    filepath = f"{prefix}_{bill_no}_{timestamp}.txt"

    with open(filepath, "w") as file:
        file.write("=" * 75 + "\n")
        file.write(f"{'MedStore Pvt. Ltd':^70}\n")
        file.write("=" * 75 + "\n")

        file.write(f"Bill No : {bill_no}\n")
        file.write(f"Customer: {customer_name}\n")
        file.write(f"Date    : {now.strftime('%Y-%m-%d %H:%M:%S')}\n")
        #file.write("=" * 75 + "\n")
        
        for item, unit, qty, price, discount in cart:
            file.write(f"Medicine : {item['Medicine Name']}\n")
            file.write(f"Unit     : {unit}\n")#type eg: strip or tablet
            file.write(f"Quantity : {qty}\n")

            if discount > 0:
                file.write(f"Discount : Rs. {discount:.2f}\n")

            file.write(f"Price    : Rs. {price:.2f}\n")
            file.write("-" * 50 + "\n")

        file.write(f"\nTOTAL AMOUNT: Rs. {grand_total:.2f}\n")
        file.write("=" * 75 + "\n")
