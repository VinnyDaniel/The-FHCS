import json

class Outfit:
    def __init__(self, name, items, occasion=None, season=None):
        self.name = name
        self.items = items  # List of strings representing clothing items
        self.occasion = occasion
        self.season = season

    def to_dict(self):
        return {
            "name": self.name,
            "items": self.items,
            "occasion": self.occasion,
            "season": self.season
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["items"],
            data.get("occasion"),
            data.get("season")
        )

    def __str__(self):
        return (
            f"Outfit: {self.name}\n"
            f"  Items: {', '.join(self.items)}\n"
            f"  Occasion: {self.occasion or 'N/A'}\n"
            f"  Season: {self.season or 'N/A'}"
        )


# ----- In-memory storage -----
outfits_data_json = None


def save_outfits(outfits):
    """Simulate saving outfits (store JSON string in memory)."""
    global outfits_data_json
    data = [outfit.to_dict() for outfit in outfits]
    outfits_data_json = json.dumps(data, indent=4, ensure_ascii=False)
    print("✅ Outfits saved in memory!")


def load_outfits():
    """Simulate loading outfits from memory."""
    global outfits_data_json
    if not outfits_data_json:
        return []
    data = json.loads(outfits_data_json)
    return [Outfit.from_dict(item) for item in data]


# ----- Example Usage -----
if __name__ == "__main__":
    my_outfits = load_outfits()

    # Add sample outfits if "file" (memory) is empty
    if not my_outfits:
        outfit1 = Outfit("Casual Day Out", ["T-shirt", "Jeans", "Sneakers"], "Casual", "Summer")
        outfit2 = Outfit("Office Wear", ["Blouse", "Skirt", "Heels"], "Work", "Autumn")
        my_outfits.extend([outfit1, outfit2])
        save_outfits(my_outfits)

    print("\n--- Current Outfits ---")
    for outfit in my_outfits:
        print(outfit)
        print("-" * 20)

    # Add a new outfit
    new_outfit = Outfit("Evening Dinner", ["Dress", "Jacket", "Boots"], "Formal", "Winter")
    my_outfits.append(new_outfit)
    save_outfits(my_outfits)

    print("\n--- Outfits After Adding a New One ---")
    loaded_outfits = load_outfits()  # Reload to confirm persistence
    for outfit in loaded_outfits:
        print(outfit)
        print("-" * 20)
        
