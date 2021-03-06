#Ryan Nguyen PSID: 1805277

#making imports
import csv
from datetime import datetime

#making the class for the inventory
class OutputInventory:
    def __init__(self, item_list):
        #providing a list of all items to create new files
        self.item_list = item_list

    def full(self):
        #creating a csv output file for entire inventory
        # items are sorted alphabetically by manufacturer
        # 1 item per row of the file
        # item ID, manu name, item type, price, service date, damaged
        with open('FullInventory.csv', 'w') as file:
            items = self.item_list
            #get the order of keys to write to file based on manu
            keys = sorted(items.keys(), key=lambda x: items[x]['manufacturer'])
            for item in keys:
                id = item
                manu_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                file.write('{},{},{},{},{},{}\n'.format(id, manu_name, item_type, price, service_date, damaged))

    def by_type(self):
        # creating a csv output file for items based by type
        # each type gets their own file. Type is reflected in name of the file
        # - item sorted by item ID
        # - one item per row of the file
        # each row of the file contains:
        # item ID, manu name, price, service date, damaged
        items = self.item_list
        types = []
        keys = sorted(items.keys())
        for item in items:
            item_type = items[item]['item_type']
            if item_type not in types:
                types.append(item_type)
        for type in types:
            file_name = type.capitalize() + 'Inventory.csv'
            with open(file_name, 'w') as file:
                for item in keys:
                    id = item
                    manu_name = items[item]['manufacturer']
                    price = items[item]['price']
                    service_date = items[item]['service_date']
                    damaged = items[item]['damaged']
                    item_type = items[item]['item_type']
                    if type == item_type:
                        file.write('{},{},{},{},{}\n'.format(id, manu_name, price, service_date, damaged))

    def past_service(self):
        # creating a cvs output file for items which are past their service date (expiration is date executed)
        # - items sorted from oldest to recent
        # - one item per row of the file
        # item info:
        # item ID, manu name, item type, price, service date, damage
        items = self.item_list
        keys = sorted(items.keys(), key=lambda x: datetime.strptime(items[x]['service_date'], "%m/%d/%Y").date(), reverse = True)
        with open('PastServiceDateInventory.csv', 'w') as file:
            for item in keys:
                id = item
                manu_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                today = datetime.now().date()
                service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                expired = service_expiration < today
                if expired:
                    file.write('{},{},{},{},{},{}\n'.format(id, manu_name, item_type, price, service_date, damaged))

    def damaged(self):
        # creating a csv output file for all items that are damaged
        # - items sorted from most expensive to least expensive
        # - one item per fow of the file
        # item information:
        # item ID, manufacturer name, item type, price, service date
        items = self.item_list
        # get order of keys to write to file based on price
        keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse=True)
        with open('DamagedInventory.csv', 'w') as file:
            for item in keys:
                id = item
                manu_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                if damaged:
                    file.write('{},{},{},{},{}\n'.format(id, manu_name, item_type, price, service_date))
if __name__ == '__main__':
    items = {}
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    manu_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = manu_name.strip()
                    items[item_id]['item_type'] = item_type.strip()
                    items[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    service_date = line[1]
                    items[item_id]['service_date'] = service_date

    inventory = OutputInventory(items)
    #create all the output files
    inventory.full()
    inventory.by_type()
    inventory.past_service()
    inventory.damaged()

    #getting the different manu and types in list form
    types =[]
    manufactuters = []
    for item in items:
        checked_manufacturer = items[item]['manufacturer']
        checked_type = items[item]['item_type']
        if checked_manufacturer not in types:
            manufactuters.append(checked_manufacturer)
        if checked_type not in types:
            types.append(checked_type)

    #asking user for input
    user_input = None
    while user_input != 'q':
        user_input = input("\nPlease enter an item manufacturer and item type (ex: Apple laptop) or enter 'q' to quit:\n")
        if user_input == 'q':
            break
        else:
            #checking each word from user to see if there is a match in manu and item type
            selected_manufacturer = None
            selected_type = None
            user_input = user_input.split()
            bad_input = False
            for word in user_input:
                if word in manufactuters:
                    if selected_manufacturer:
                        #only one manu
                        bad_input = True
                    else:
                        selected_manufacturer = word
                elif word in types:
                    if selected_type:
                        #only one type
                        bad_input = True
                    else:
                        selected_type = word
            if not selected_manufacturer or not selected_type or bad_input:
                print("No such item in inventory")
            else:
                #order list of keys to iterate through based on highest price first
                keys = sorted(items.keys(), key=lambda x: items[x]['price'], reverse = True)

                #getting the matching list of items based on user input
                matching_items = []

                #storing items with same type but diff manu
                # - items type MUST match
                # - item must be in inventory and not damaged or in past service csv
                similar_items = {}
                for item in keys:
                    if items[item]['item_type'] == selected_type:
                        #do not add damaged items or past service to matched list or similar list
                        today = datetime.now().date()
                        service_date = items[item]['service_date']
                        service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                        expired = service_expiration < today
                        if items[item]['manufacturer'] == selected_manufacturer:
                            if not expired and not items[item]['damaged']:
                                matching_items.append((item, items[item]))
                        else:
                            if not expired and not items[item]['damaged']:
                                similar_items[item] = items[item]

                #output the item if matched correctly
                if matching_items:
                    item = matching_items[0]
                    item_id = item[0]
                    manu_name = item[1]['manufacturer']
                    item_type = item[1]['item_type']
                    price = item[1]['price']
                    print("Your item is: {}, {}, {}, {}\n".format(item_id, manu_name, item_type, price))

                    #output item from diff manu that is closest in price to matched item
                    if similar_items:
                        matched_price = price
                        #getting the similar item w/ the closest price to the OG item
                        closest_item = None
                        closest_price_diff = None
                        for item in similar_items:
                            if closest_price_diff == None:
                                closest_item = similar_items[item]
                                closest_price_diff = abs(int(matched_price) - int(similar_items[item]['price']))
                                item_id = item
                                manu_name   = similar_items[item]['manufacturer']
                                item_type = similar_items[item]['item_type']
                                price = similar_items[item]['price']
                                continue
                            price_diff = abs(int(matched_price) - int(similar_items[item]['price']))
                            if price_diff < closest_price_diff:
                                closest_item = item
                                closest_price_diff = price_diff
                                item_id = item
                                manu_name = similar_items[item]['manufacturer']
                                item_type = similar_items[item]['item_type']
                                price = similar_items[item]['price']
                        print("You may, also, consider: {}, {}, {}, {}\n".format(item_id, manu_name, item_type, price))
                else:
                    print("No such item in inventory")
