from food import Table,Hall 

def add_food(table):
    menu_num = len(table.menu)
    for num,name in enumerate(table.menu.keys(), 1):    #print main or extra
        print(f"{num}: {name}")    
    menu_food = list(table.menu.keys())      #save main or extra
    
    while True: 
        try:
            choice_menu = int(input("\nchoice menu: ")) - 1      #print main or extra
            if 0 <= choice_menu < len(menu_food):
                break
            else:
                print(f" plz enter num between 1;{menu_num}")
        except ValueError:
            print("Invalid input. Please enter a number.")
        
        
    food = list(table.menu.keys())[choice_menu]         #save main or extra
    for num, item in enumerate(table.menu[food], 1):    #print the food in main or extra
        print(f"{num}: {item}")
    
    while True:
        try:
            item_choice = int(input("choice item: ")) - 1   # print the food in main or extra
            if 0 <= item_choice < len(table.menu[food]):
                break
            else:
                print(f" plz enter num between 1;{len(table.menu[food])}")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    item = Table.menu[food][item_choice]           # save the food in main or extra
    table.add(item.name, item.price)               # add the food to add function in table class

hall_class=[Hall(i) for i in range(1,5)]

def main():

#    1-print  2-choose  3-save 4-show  [hall] 

    print("\n=== welcome to the restaurant===\n")
    for x in range(1,5):
        print(f"|Hall:{x}|")
    while True:
        try:
            choise_hall=int(input("\nENTER HALL: ")) - 1
            if 0 <= choise_hall < len(hall_class):
                break
            else:
                print(f" plz enter num between 1;{len(hall_class)}")
        except ValueError:
            print("Invalid input. Please enter a number.")
    hall_obj=hall_class[choise_hall]       
    print(f"\n===hall:{hall_obj.number}===")   

#    1-print  2-choose  3-save 4-show [table]
    for x in range(1,6):
        print(f"|TABLE:{x}|")
    while True:    
        try:
            choise_table=int(input("\nENTER TABLE: ")) - 1
            if 0 <= choise_table < len(hall_obj.tables):
                break
            else:
                print(f" plz enter num between 1;{len(hall_obj.tables)}")
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    table_obj=hall_obj.tables[choise_table]
    print(f"\n=====Table:{table_obj.number}====")


    while True:
        print("\n1-add food\n2-view order\n3-checkout\n4-vip\n5-exit")
        try:
            action=int(input("\nenter action: "))
            if action not in [1,2,3,4,5]:
                print(f"plz enter num between 1;5")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        actions = {1:lambda: add_food(table_obj),2:lambda: print(table_obj),3:lambda: table_obj.check(),4:lambda: setattr(table_obj, 'vip', True)}
        user_action = actions.get(action)
        if user_action:
            user_action()

        if action == 5:
            print("Thank you for visiting the restaurant. Goodbye!")
            break    
main()



