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
        # creatin a cvs output file for items which are past their service date (expiration is date executed)
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






