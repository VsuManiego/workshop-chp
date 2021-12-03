


import csv

from datetime import date

item_name = ''
item_quantity = ''

def main():
    impfile = "workshop_inventory.csv"
    impfile2 = "borrowed_items.csv"
    impfile3 = "records.csv"
    
    while True:
        print('''

--------------------------------------------------------------
--------------------------------------------------------------
              Welcome to the Workshop Inventory! 

--------------------------------------------------------------
                         Main Menu
--------------------------------------------------------------

  1 - Add New Item/s to the Workshop Inventory
  2 - Remove item/s from the Workshop Inventory
  3 - Borrow Item/s from the Workshop Inventory
  4 - Return Item/s to the Workshop Inventory
  5 - Display Workshop Inventory
  6 - Display Borrowed Item/s from the Workshop Inventory
  7 - Display Workshop Inventory Log Records
  0 - Exit Program\n
        ''')
        try:
            action = int(input("What would you like to do? (Please choose from 0 - 7): "))
            nice = (0, 1, 2, 3, 4, 5, 6, 7)
            if action in nice:
                if action == 1:
                    enter_name()
                    enter_quantity()
                    add_inventory(impfile, impfile3)
                elif action == 2:
                    enter_name()
                    enter_quantity()
                    remove_inventory(impfile, impfile3)
                elif action == 3:
                    enter_name()
                    enter_quantity()
                    borrow_inventory(impfile, impfile2, impfile3)
                elif action == 4:
                    enter_name()
                    enter_quantity()
                    return_inventory(impfile, impfile2, impfile3)
                elif action == 5:
                    display_inventory(impfile)
                elif action == 6:
                    display_borrowed(impfile2)
                elif action == 7:
                    display_records(impfile3)
                else:
                    break
        except:
            print("\nInvalid input. Please choose from 0 - 7.")



def enter_name():
    global item_name
    while True:
        item_name = str(input(f"Name of item: "))
        if item_name == str():
            print(f"Error: Please input proper item name")
        else:
            break
    return
        


def enter_quantity():
    global item_quantity
    good = False
    while not False:
        try:
            item_quantity = int(input("Number of {item_name}/s: "))  
            good = True
            break  
                    
        except ValueError:
            print("Please input proper quantity.")
    return




def load_inventory(impfile):
    with open(impfile, "r", encoding="utf-8") as file:
        read = csv.reader(file)
        readgo = list(read)
        return readgo


            
def load_borrowed(impfile2):
    with open(impfile2, "r", encoding="utf-8") as file2:
        read2 = csv.reader(file2)
        readgo2 = list(read2)
        return readgo2



def load_records(impfile3):
    with open(impfile3, "r", encoding="utf-8") as file3:
        read3 = csv.reader(file3)
        readgo3 = list(read3)
        return readgo3


        

def save_inventory(impfile, inventory):
    with open(impfile, "w+", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        for item in inventory:
             writer.writerow(item)



def save_borrowed(impfile2, borrowed):
    with open(impfile2, "w+", encoding="utf-8", newline="") as file2:
            writer = csv.writer(file2)
            for item in borrowed:
                writer.writerow(item)



def save_records(impfile3, records):
    with open(impfile3, "w+", encoding="utf-8", newline="") as file3:
            writer = csv.writer(file3)
            for item in records:
                writer.writerow(item)



        
def display_inventory(impfile):
    inventory = sorted(load_inventory(impfile))
    print('''
--------------------------------------------------------------
                     Workshop Inventory
--------------------------------------------------------------
           [Item]                       [Quantity]
''')
    for item in inventory:
        item_name = item[0]
        item_quantity = item[1]
        print(f"       {item_name:15s}                   {item_quantity} pc/s")
     


def display_borrowed(impfile2):
    borrowed = sorted(load_borrowed(impfile2))
    print('''
---------------------------------------------------------------
                         Borrowed Items
---------------------------------------------------------------
           [Item]                       [Quantity]
''')
    for item in borrowed:
        item_name = item[0]
        item_quantity = item[1]
        print(f"       {item_name:15s}                   {item_quantity} pc/s")



def display_records(impfile3):
    records = load_records(impfile3)
    print('''
---------------------------------------------------------------
                          Log Records
---------------------------------------------------------------
''')
    for item in records:
        item_name = item[0]
        item_quantity = item[1]
        log_date = item[2]
        status = item[3]
        print(f"  Date: {log_date:12s} | '{status}' {item_quantity} pc/s of {item_name}")
    


    


def add_inventory(impfile, impfile3):
    inventory = load_inventory(impfile)
    records = load_records(impfile3)
    added = [item_name, item_quantity]
    action_date = date.today()
    action_date_record = f'[{action_date.month}/{action_date.day}/{action_date.year}]'
    status = 'Added'   
    record_added = [item_name, item_quantity, action_date_record, status]
    for item in inventory:
        if item[0] == item_name:
            item[1] = int(item[1])
            item[1] += item_quantity
            item[1] = str(item[1])
            break
    else:
        inventory.append(added)
    save_inventory(impfile, inventory)
    print(f"'{item_quantity}' pc/s of '{item_name}' is/are added to the workshop inventory.")
    records.append(record_added)              
    save_records(impfile3, records)





    
def remove_inventory(impfile, impfile3):
    inventory = load_inventory(impfile)
    records = load_records(impfile3)
    removed = [item_name, item_quantity]
    action_date = date.today()
    action_date_record = f'[{action_date.month}/{action_date.day}/{action_date.year}]'
    status = 'Removed'
    record_added = [item_name, item_quantity, action_date_record, status]  
    for item in inventory:
        if item[0] == item_name:
            item[1] = int(item[1])
            if item_quantity < item[1]:
                item[1] -= item_quantity
                item[1] = str(item[1])
                save_inventory(impfile, inventory)
                print(f"'{item_quantity}' pc/s of '{item_name}' is/are removed from the inventory.")
                records.append(record_added)
                save_records(impfile3, records)
                break
            elif item_quantity == item[1]:
                inventory.remove(removed)
                save_inventory(impfile, inventory)
                print(f"'{item_quantity}' pc/s of '{item_name}' is/are removed from the workshop inventory.")
                records.append(record_added)               
                save_records(impfile3, records)
                break
            else:
                print(f"Not enough '{item_name}' in the workshop inventory to remove.")
                break
    else:
        print(f"'{item_name}' is not in the workshop inventory")
        
              



    

def borrow_inventory(impfile, impfile2, impfile3):
    inventory = load_inventory(impfile)
    borrowed = load_borrowed(impfile2)
    records = load_records(impfile3)
    removed = [item_name, item_quantity]
    save_borrowed(impfile2, borrowed)
    action_date = date.today()
    action_date_record = f'[{action_date.month}/{action_date.day}/{action_date.year}]'
    status = 'Borrowed'   
    record_added = [item_name, item_quantity, action_date_record, status]
    added = [item_name, item_quantity]
    for item in inventory:
        if item[0] == item_name:
            item[1] = int(item[1])
            if item_quantity < item[1]:
                item[1] -= item_quantity
                item[1] = str(item[1])
                save_inventory(impfile, inventory)
                print(f"'{item_quantity}' pc/s of '{item_name}' is/are borrowed from the workshop inventory.")
                for item in borrowed:
                    if item[0] == item_name:
                        item[1] = int(item[1])
                        item[1] += item_quantity
                        item[1] = str(item[1])
                        break
                else:
                    borrowed.append(added)
                save_borrowed(impfile2, borrowed)
                records.append(record_added)               
                save_records(impfile3, records)
                break
            elif item_quantity == item[1]:
                inventory.remove(removed)
                save_inventory(impfile, inventory)
                print(f"'{item_quantity}' pc/s of '{item_name}' is/are borrowed from the workshop inventory.")
                for item in borrowed:
                    if item[0] == item_name:
                        item[1] = int(item[1])
                        item[1] += item_quantity
                        item[1] = str(item[1])
                        break
                else:
                    borrowed.append(added)
                save_borrowed(impfile2, borrowed)
                records.append(record_added)               
                save_records(impfile3, records)
                break
            else:
                print(f"Not enough '{item_name}' in the workshop inventory to borrow.")
                break
    else:
        print(f"'{item_name}' is not in the workshop inventory")






def return_inventory(impfile, impfile2, impfile3):
    inventory = load_inventory(impfile)
    borrowed = load_borrowed(impfile2)
    records = load_records(impfile3)
    removed = [item_name, item_quantity]
    added = [item_name, item_quantity]
    action_date = date.today()
    action_date_record = f'[{action_date.month}/{action_date.day}/{action_date.year}]'
    status = 'Returned'   
    record_added = [item_name, item_quantity, action_date_record, status]
    for item in borrowed:
        if item[0] == item_name:
            item[1] = int(item[1])
            if item_quantity < item[1]:
                item[1] -= item_quantity
                item[1] = str(item[1])
                save_borrowed(impfile2, borrowed)
                print(f"'{item_quantity}' pc/s of '{item_name}' is/are returned to the workshop inventory.")
                
                for item in inventory:
                    if item[0] == item_name:
                        item[1] = int(item[1])
                        item[1] += item_quantity
                        item[1] = str(item[1])
                        break
                else:
                    inventory.append(added)
                save_inventory(impfile, inventory)
                records.append(record_added)              
                save_records(impfile3, records)
                break
            elif item_quantity == item[1]:
                borrowed.remove(removed)
                save_borrowed(impfile2, borrowed)
                print(f"'{item_quantity}' pc/s of '{item_name}' is/are returned to the workshop inventory.")
                for item in inventory:
                    if item[0] == item_name:
                        item[1] = int(item[1])
                        item[1] += item_quantity
                        item[1] = str(item[1])
                        break
                else:
                    inventory.append(added)
                save_inventory(impfile, inventory)
                records.append(record_added)              
                save_records(impfile3, records)
                break
            else:
                print(f"Excess quantity of '{item_name}' to return based on the borrowed items.")
                break
    else:
        print(f"'{item_name}' is not borrowed from the workshop inventory")





        
if __name__ == "__main__":
    main()





