import database
import json


def create_whitelist(output_file='whitelist.json'):
    whitelist_data = database.vypis_whitelist()
    
    # Vytvoření seznamu slovníků pro každý záznam
    whitelist_list = [{"uuid": row[0], "name": row[1]} for row in whitelist_data]

    # Uložení do souboru whitelist.json
    with open(output_file, 'w') as file:
        json.dump(whitelist_list, file, indent=2)
