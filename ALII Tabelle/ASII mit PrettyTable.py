from prettytable import PrettyTable

# Create a PrettyTable object
table = PrettyTable()

# Define column headers
table.field_names = ["Dec", "Char", "Dec", "Char", "Dec", "Char", "Dec", "Char"]

# ASCII values range from 32 to 255
for i in range(32, 256, 4):
    row = [
        i, chr(i),
        i+1, chr(i+1),
        i+2, chr(i+2),
        i+3, chr(i+3)
    ]
    table.add_row(row)

# Print the table
print(table)
