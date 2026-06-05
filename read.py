

def read_medical_data(inputPath):
    """
    This module is responsible for reading the medicine data from the text file
    and converting it into a list of dictionaries i.e. formatted data and  rest of the program
    can work with it which make program easier.

    store each medicine details from (medical_data.txt) in a dictionary.
    All dictionaries are collected into a list called 'stock' which is returned at the end.

    """
    stock = []
    try:
        with open(inputPath, "r") as file:
            lines = file.readlines()
            #print(lines)
            for each in lines:
                eachLine = each.replace("\n","").split(',')
                #print(eachLine)
                #dictionary use to store the data
                medical_dic = {#new dictionary each time
                    "Medicine Name": eachLine[0],
                    "Brand Name": eachLine[1],
                    "No of tablets": int(eachLine[2]),  #tablet
                    "Rate tablet": int(eachLine[3]),  #rate per tablet
                    "Rate Strip": int(eachLine[4]),
                    "Tablets per strip": int(eachLine[5])}  #number of tablets in one strip

                stock.append(medical_dic)
            return stock
        
    except FileNotFoundError:
        print("File not found")
        return [] # for handling when file path is wrong
        #print(stock)
