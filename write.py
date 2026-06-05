 

def save_report(outputPath, processed_data):
    """
    This file handles saving the data back to the files after each transaction.

    This is just for display. I format everything with proper columns and
    headings so it looks like a proper stock table. This file is overwritten
    every time so it always shows the latest stock.

    """ 

    with open(outputPath, "w") as file:

        # Header
        file.write("=" * 90 + "\n")
        file.write(f"{'MEDICAL STOCK':^60}\n")
        file.write(f"{'MedStore Pvt. Ltd.':^60}\n")
        file.write("=" * 90 + "\n\n")

        # Column headings
        file.write(f"{'S.N':<5}{'Medicine':<25}{'Brand':<15}{'No of tablets':>10}{'Rate(Tab)':>15}{'Rate(Strip)':>15}\n")
        file.write("-" * 90 + "\n")

        # Data rows
        i = 1
        for each in processed_data:
            file.write(f"{i:<5}"
                       f"{each['Medicine Name']:<25}"
                       f"{each['Brand Name']:<15}"
                       f"{each['No of tablets']:>10}"#no of tablets
                       f"{each['Rate tablet']:>15}"
                       f"{each['Rate Strip']:>15}\n")
            i += 1

        # Footer of the file
        file.write("\n" + "-" * 90 + "\n")
        file.write(f"Total Records: {len(processed_data)}\n") # total number of record in the stock
        


def save_to_database(path, data): # update the medical_data.txt
    """
    Saves the current stock back to the medical_data.txt.
    Without this, all changes would be lost when the program closed.

    """
    with open(path, "w") as file:
        for each in data:
            file.write(
                f"{each['Medicine Name']},"
                f"{each['Brand Name']},"
                f"{each['No of tablets']},"
                f"{each['Rate tablet']},"
                f"{each['Rate Strip']},"
                f"{each['Tablets per strip']}\n"
            )
