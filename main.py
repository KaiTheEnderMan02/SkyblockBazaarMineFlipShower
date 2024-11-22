import requests
from tabulate import tabulate

def get_bazaar_data(api_key):
    url = f"https://api.hypixel.net/skyblock/bazaar?key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error fetching data: {response.status_code}")
        return None

def extract_mining_items(bazaar_data):
    # Define mining-related item IDs
    mining_items = {
        "COBBLESTONE", "COAL", "IRON_INGOT", "GOLD_INGOT", "DIAMOND", 
        "EMERALD", "REDSTONE", "LAPIS_LAZULI", "QUARTZ", "OBSIDIAN", 
        "MITHRIL_ORE", "TITANIUM_ORE", "GEMSTONE", "FLINT", "SAND"
    }

    extracted_items = []
    if 'products' in bazaar_data:
        for item_id, item_data in bazaar_data['products'].items():
            if item_id in mining_items and 'quick_status' in item_data:
                quick_status = item_data['quick_status']
                buy_price = quick_status['buyPrice']
                sell_price = quick_status['sellPrice']
                buy_volume = quick_status['buyVolume']
                sell_volume = quick_status['sellVolume']

                extracted_items.append([
                    item_id, 
                    f"{buy_price:.2f}", 
                    f"{sell_price:.2f}", 
                    buy_volume, 
                    sell_volume
                ])
    return extracted_items

def main():
    api_key = "502582ab-b217-46ad-a8c5-e21b57f310e8"  # Your Hypixel API key

    print("Fetching Hypixel Skyblock Bazaar data...")
    bazaar_data = get_bazaar_data(api_key)

    if bazaar_data:
        print("Extracting mining items...")
        mining_items = extract_mining_items(bazaar_data)

        if mining_items:
            # Print results in a table
            headers = ["Item ID", "Buy Price", "Sell Price", "Buy Order Volume", "Sell Order Volume"]
            print(tabulate(mining_items, headers=headers, tablefmt="grid"))
        else:
            print("No mining items found in the Bazaar data.")

if __name__ == "__main__":
    main()
