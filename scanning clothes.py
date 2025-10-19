import numpy as np
import os
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing.image import img_to_array

# ===== Load Pre-trained Model =====
# MobileNetV2 is pre-trained on ImageNet (general object categories)
model = MobileNetV2(weights='imagenet')

# ===== Function to classify a single image =====
def classify_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = cv2.resize(img, (224, 224))  # MobileNetV2 input size
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    preds = model.predict(img_array)
    decoded = decode_predictions(preds, top=1)[0][0]  # Get top prediction
    label, confidence = decoded[1], decoded[2]
    return label, confidence

# ===== Function to scan wardrobe folder =====
def scan_wardrobe(folder_path='wardrobe_images'):
    inventory = {}
    for filename in os.listdir(folder_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(folder_path, filename)
            label, confidence = classify_image(image_path)
            inventory[filename] = {'category': label, 'confidence': confidence}
            print(f"{filename} → {label} ({confidence*100:.2f}%)")
    return inventory

# ===== Main Program =====
if __name__ == "__main__":
    folder = input("Enter wardrobe folder path (default: 'wardrobe_images'): ") or 'wardrobe_images'
    inventory = scan_wardrobe(folder)
    print("\n✅ Wardrobe Scanning Complete:")
    for item, info in inventory.items():
        print(f"{item}: {info['category']} ({info['confidence']*100:.2f}%)")
