import os
import csv

# Specify the folder path
folder_path = '/path/to/your/folder'

# Get all the JPEG files in the folder
jpeg_files = [f for f in os.listdir(folder_path) if f.endswith('.jpeg') or f.endswith('.jpg')]

# Create and write to a CSV file
csv_file = 'output.csv'
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    
    # Write the header
    writer.writerow(["File name", "Title", "Keywords", "Prompt", "Model"])
    
    # For simplicity, let's assume we don't have data for "Title", "Keywords", etc.
    # If you have this data, you can modify the code accordingly to fetch it
    for jpeg in jpeg_files:
        writer.writerow([jpeg, "", "", "", ""])

print(f"CSV file saved as {csv_file}")
