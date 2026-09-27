import time

sentence = "Python is simple when you practice consistently."

print("TYPE THIS:")
print(sentence)

input("\nPress Enter when you are ready...")

start = time.time()
typed = input("\nStart typing: ")
end = time.time()

time_taken = end - start

correct = 0
for i in range(min(len(sentence), len(typed))):
    if sentence[i] == typed[i]:
        correct += 1

accuracy = (correct / len(sentence)) * 100
words = len(typed.split())
wpm = (words / time_taken) * 60

print("\n--- RESULTS ---")
print(f"Time Taken : {time_taken:.2f} seconds")
print(f"Accuracy   : {accuracy:.2f}%")
print(f"Speed      : {wpm:.2f} WPM")

if accuracy >= 90:
    print("Performance: Excellent!")
elif accuracy >= 70:
    print("Performance: Good!")
else:
    print("Performance: Keep practicing!")