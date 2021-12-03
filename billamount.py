print(" sharing is caring ;)\n ")
def bill():
    try:
        amt= int(input('enter the bill amount\n'))
        totper =  int(input('total persons?\n'))
        print('if u r not interseted to pay tips enter number => 0')
        tips = int(input('tips ? 0,  10,11,12 Percentage\n'))
        total = (tips/100)*(amt) + (amt)
        print(round(total/totper,2))
    except:
        print('something went wrong! please try again,\nuse input as numbers (int) not letters (str) and %')
        bill()

bill()

