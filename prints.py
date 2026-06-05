def print_stock_data(processed_data):
    """
    Prints the current medicine stock to the terminal in a proper table format.
    The number of strips is calculated automatically from tablets divided by
    tablets-per-strip — it is not stored separately.
    """
    try:
        # column widths
        c1, c2, c3, c4, c5, c6, c7 = 4, 22, 16, 9, 8, 10, 11
        total = c1 + c2 + c3 + c4 + c5 + c6 + c7 + 6  # 6 for spaces between cols

        print("\n" + "=" * total)
        print(f"{'MEDICAL STOCK REPORT':^{total}}")
        print(f"{'MedStore Pvt. Ltd.':^{total}}")
        print("=" * total)

        # header row
        print(f"{'S.N':<{c1}}  {'Medicine':<{c2}}{'Brand':<{c3}}{'Tablets':>{c4}}{'Strips':>{c5}}{'Rate/Tab':>{c6}}{'Rate/Strip':>{c7}}")
        print("-" * total)

        i = 1
        for each in processed_data:
            strips = each["No of tablets"] // each["Tablets per strip"]
            print(f"{i:<{c1}}  {each['Medicine Name']:<{c2}}{each['Brand Name']:<{c3}}{each['No of tablets']:>{c4}}{strips:>{c5}}{each['Rate tablet']:>{c6}}{each['Rate Strip']:>{c7}}")
            i += 1

        print("-" * total)
        print(f"  Total Records: {len(processed_data)}")
        print("=" * total + "\n")

    except ZeroDivisionError:
        print("Error: Tablets per strip cannot be zero!")
