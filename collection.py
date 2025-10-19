# Digital Wardrobe / Clothing Collection
class ClothingItem:
    def __init__(self, name, category, color, season, occasion):
        self.name = name
        self.category = category  # e.g., 'Top', 'Bottom', 'Footwear'
        self.color = color
        self.season = season      # e.g., 'Summer', 'Winter'
        self.occasion = occasion  # e.g., 'Casual', 'Formal'

    def __str__(self):
        return (f"{self.name} ({self.category}) - Color: {self.color}, "
                f"Season: {self.season}, Occasion: {self.occasion}")


class Wardrobe:
    def __init__(self):
        self.clothes = []

    def add_item(self, item):
        self.clothes.append(item)
        print(f"✅ Added: {item.name}")

    def view_all(self):
        if not self.clothes:
            print("🧺 Wardrobe is empty.")
        else:
            print("\n👗 Your Wardrobe Collection:")
            for i, item in enumerate(self.clothes, start=1):
                print(f"{i}. {item}")

    def search_by_category(self, category):
        results = [item for item in self.clothes if item.category.lower() == category.lower()]
        if results:
            print(f"\n🔍 Clothes in category '{category}':")
            for item in results:
                print(f"- {item}")
        else:
            print(f"⚠️ No clothes found in category '{category}'.")

    def remove_item(self, name):
        for item in self.clothes:
            if item.name.lower() == name.lower():
                self.clothes.remove(item)
                print(f"🗑 Removed: {item.name}")
                return
        print(f"⚠️ No item named '{name}' found.")

# Example usage
if __name__ == "__main__":
    wardrobe = Wardrobe()

    # Add some sample clothes
    wardrobe.add_item(ClothingItem("T-shirt", "Top", "Blue", "Summer", "Casual"))
    wardrobe.add_item(ClothingItem("Jeans", "Bottom", "Black", "All", "Casual"))
    wardrobe.add_item(ClothingItem("Jacket", "Outerwear", "Brown", "Winter", "Casual"))
    wardrobe.add_item(ClothingItem("Shirt", "Top", "White", "All", "Formal"))

    # View all clothes
    wardrobe.view_all()

    # Search by category
    wardrobe.search_by_category("Top")

    # Remove an item
    wardrobe.remove_item("Jeans")

    # View again after removal
    wardrobe.view_all()
