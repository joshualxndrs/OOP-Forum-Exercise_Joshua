from ProgramExerciseJS import Grocery_listsJS
 
def ItemListJS():
 
 items = []
 
 num_items = int(input("Enter number of items to order: "))
 while (num_items < 1):
    num_items = int(input("\nNumber of items ordered should be greater than 1, please input again:\n"))
 
 for i in range(num_items):
     print("Item#" + str(i+1) + "-")
     name = input("\nItem Name: ")
     amount = float(input("Order Amount (in pounds): "))
     while (amount <= 0):
        amount = float(input("\nAmount must be greater than 0\n"))
     item = Grocery_listsJS(name, amount)
     items.append(item)
 
 return items
 
def DisplayItemListJS(items):
 
 for item in items:
     print(item)
 
def TotalCostOfItemsJS(items):
    total = 0.00
    for item in items:
        total += item.calculatetotalcostJS()
    return total
 
def main():
 
 items = ItemListJS()
 DisplayItemListJS(items)
 print("\nTotal cost of items selected: ", TotalCostOfItemsJS(items))
 
main()