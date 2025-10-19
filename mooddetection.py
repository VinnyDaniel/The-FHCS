# mood_detection.py
import random
# Simulated wearable data input
def get_wearable_data():
    # In a real app, replace this with data from Bluetooth / wearable API
    heart_rate = random.randint(60, 120)     # bpm
    bp_systolic = random.randint(100, 150)   # mmHg
    bp_diastolic = random.randint(60, 95)    # mmHg
    pulse = random.randint(60, 120)          # bpm
    return heart_rate, bp_systolic, bp_diastolic, pulse
# Mood detection logic
def detect_mood(heart_rate, bp_sys, bp_dia, pulse):
    if heart_rate < 70 and bp_sys < 120 and bp_dia < 80:
        mood = "Relaxed 😌"
    elif heart_rate > 100 or bp_sys > 140 or bp_dia > 90:
        mood = "Stressed 😣"
    elif 70 <= heart_rate <= 90 and 110 <= bp_sys <= 130:
        mood = "Happy 🙂"
    else:
        mood = "Neutral 😐"
    return mood
# App main function
def main():
    heart_rate, bp_sys, bp_dia, pulse = get_wearable_data()

    print("📊 Wearable Data")
    print("----------------")
    print(f"Heart Rate     : {heart_rate} bpm")
    print(f"Blood Pressure : {bp_sys}/{bp_dia} mmHg")
    print(f"Pulse Rate     : {pulse} bpm")

    mood = detect_mood(heart_rate, bp_sys, bp_dia, pulse)

    print("\n🧠 Detected Mood:", mood)
# Run the app
if __name__ == "__main__":
    main()
