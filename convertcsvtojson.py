def extend_json_with_csv(csv_path, json_path):

    # Validate CSV file existence
    if not os.path.isfile(csv_path):
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    # Read CSV into DataFrame
    df = pd.read_csv(csv_path)

    # Convert DataFrame to list of dicts (JSON-like)
    new_data = df.to_dict(orient="records")

    # If JSON file exists, load it; otherwise start with empty list
    if os.path.isfile(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            try:
                existing_data = json.load(f)
                if not isinstance(existing_data, list):
                    raise ValueError("Existing JSON is not a list.")
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    # Append new data
    extended_data = existing_data + new_data

    # Save back to JSON
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(extended_data, f, ensure_ascii=False, indent=4)

    print(f"JSON file '{json_path}' successfully updated with {len(new_data)} new records.")
