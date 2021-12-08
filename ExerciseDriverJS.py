from ProgramExerciseJS import Grocery_lists
 
def ItemList():
 
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
     item = Grocery_lists(name, amount)
     items.append(item)
 
 return items
 
def DisplayItemList(items):
 
 for item in items:
     print(item)
 
def TotalCostOfItems(items):
    total = 0.00
    for item in items:
        total += item.calculatetotalcost()
    return total
 
def main():
 
 items = ItemList()
 DisplayItemList(items)
 print("\nTotal cost of items selected: ", TotalCostOfItems(items))
 
main()