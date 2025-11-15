import json

# Function to append new data to JSON file
def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        # Load existing data into a dictionary
        file_data = json.load(file)
        
        # Append new data to the 'emp_details' list
        file_data["emp_details"].append(new_data)
        
        # Move the cursor to the beginning of the file
        file.seek(0)
        
        # Write the updated data back to the file
        json.dump(file_data, file, indent=4)

# New data to append
new_employee = {
    "emp_name": "Nikhil",
    "email": "nikhil@geeksforgeeks.org",
    "job_profile": "Full Time"
}

# Call the function to append data
write_json(new_employee)