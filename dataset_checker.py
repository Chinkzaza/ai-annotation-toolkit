import json

def check_dataset(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)

    print("Total records:", len(data))

    empty_entries = 0
    for item in data:
        if not item.get("text"):
            empty_entries += 1

    print("Empty entries:", empty_entries)

if __name__ == "__main__":
    check_dataset("dataset.json")
