data = {"nama": "ayu", "nilai": 85, "kelas": "A"}

print("--- Menelusuri Key ---")
for key in data:
    print(key)

print("\n--- Menelusuri Value ---")
for value in data.values():
    print(value)

print("\n--- Menelusuri Key dan Value (Items) ---")
for key, value in data.items():
    print(f"{key}: {value}")