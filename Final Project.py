"""
Marcus Behr
CSCI 2061.70
Final Project

"""
import pickle #import the pickle module for data retrival/storage

data = {} #data dictonary to hold portfolio data
prompt = "(A)dd/(D)elete stocks, (L)oad file, (U)pdate prices, (R)eport, or (Q)uit? "

def add():
    """add a new stock to the portfolio(data dictionary)"""
    print("Add a stock to your portfolio...") #let user know what's goin on
    print() #blank line
    ticker = input("Ticker: ")
    companyName = input("Company name: ")
    numberOfShares = int(input("Number of shares: "))
    purchasePricePerShare = float(input("Purchase price per share: $"))

    value = numberOfShares * purchasePricePerShare #determine total value
    value = int(value) #convert to int
    latest = numberOfShares #no change in numberOfShares
    data[companyName] = [ticker,companyName,numberOfShares,latest,purchasePricePerShare,value]
    #create the dictionary entry
    print() #another blank line

def load():
    """loads contents from portfolio.dat into data dictionary"""
    print("Load file: portfolio.dat") #let user know what's goin on
    print() #blank line
    loadedData= pickle.load(open("portfolio.dat", "rb")) #add file contents from portfolio.dat to loadedData
    #iterating through loadedData variable and adding them to data variable(probably easier way to do this)
    for i in loadedData:
        data[loadedData[i][1]] = [loadedData[i][0], loadedData[i][1], loadedData[i][2]
                                  , loadedData[i][3], loadedData[i][4], loadedData[i][5]]
                
def update():
    """update the purchase price of stocks in portfolio"""
    print("Update stock prices (<Return> to keep current value)...")
    print() #blank line

    for i in data:
        update = input(data[i][0] + ":" )
        if update == "":
            continue
        else:
            update = int(update) #cast to int
            data[i][4] = update #work with gain/loss variable here
            data[i][5] = data[i][2] * data[i][4] #update value
            
            


def report():
    """ display all stock information using formatte strings"""
    choice = input("Sort output on (N)ame, or (V)alue? ")
    print() #blank line
    print("%s%25s%10s%10s%10s%10s" % ("Company", "Shares","Pur.","Latest","Value","G/L"))
    print("=" * 75)
    if choice.lower() == 'n':
        for i in sorted(data):
            print("%s%s%15d%10d%10.2f%10.2f" % (data[i][1],"(" + data[i][0] + ")",data[i][2],data[i][3],data[i][4],data[i][5]))
    elif choice.lower() == 'v':
        import operator
        sorted_values = sorted(data.items(), key = operator.itemgetter(0))
        for i in sorted_values:
            print("%s%s%15d%10d%10.2f%10.2f" % (data[i][1],"(" + data[i][0] + ")",data[i][2],data[i][3],data[i][4],data[i][5]))
            
            
    print() #blank line

def delete():
    """
    check if the ticker symbol corresponds to anything in the dictionary
    and delete if it does, if it doesn't tell the user and ask them
    to try again
    """
    tickerSymbol = input("Enter the ticker symbol of the stock to remove: ")
    for i in data.copy():
        if tickerSymbol==data[i][0]:
            data.pop(i)
    print() #blank line

def main():
    while True:
        selection = input(prompt)
        selection = selection.lower() #convert seletion to lower case

        if selection == 'a':
            add()
        elif selection == 'd':
            delete()
        elif selection == 'l':
            load()
        elif selection == 'u':
            update()
        elif selection == 'r':
            report()
        elif selection == 'q':
            pickle.dump(data, open("portfolio.dat", "wb"))
            print("Bye.") #goodbye message to user
            break; #exit loop and program
        else:
            print("Please enter a valid selection") #error input checking
            print() #blank line
            
if __name__ == "__main__":
    main()
    
