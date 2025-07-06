import requests
import pprint


list = [['Philip', 'Lily'], ['30', '14']]

def add_to_list():
    new_item = input('what to add?')
    list.append(new_item)
    print(list)
    start_app()
    
def remove_item():
    item = input('Type the item to remove: ')
    if item in list:
        list.remove(item)
        print(f'Removed {item}, new list: {list}')
    else: print('item not found in list')
    start_app()
def add_into_specf_list():
    list_index = input('into which list would you like to add item?')
    new_item = input('what to add?')
    list[int(list_index)-1].append(new_item)
    print(list)
    start_app()
    
def save_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(content)

def start_app(): 
    user_choice = input('add to list(1), see list(2) or reverse list(3) or remove item from list(4)or add new list(5) or add item to into a list(6) to exit and save(7)')
    if user_choice == '1':
        add_to_list()
    elif user_choice == '2':
        print(list)
        start_app()
    elif user_choice == '3':
        list.reverse()
        print(list)
        start_app()
    elif user_choice == '4':
        remove_item()
        
    elif user_choice == '5':
        list.append([])
        print(list)
        start_app()
    elif user_choice == '6':
        add_into_specf_list()

    elif user_choice == '7':
        save_to_file('first coding', str(list))
        exit()
    else: 
        print('unknown command')

start_app()



    
    
