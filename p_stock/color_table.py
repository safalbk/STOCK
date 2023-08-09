
from prettytable import PrettyTable
RESET = "\033[0m"
GREEN = "\033[92m"
BOLD = "\033[1m"
RESET = "\033[0m"
RED = "\033[91m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
# Create a PrettyTable instance

def green_table(headers,row):
    table = PrettyTable()

    # Define the field names (headers)
    # field_names = ["Header 1", "Header 2", "Header 3"]
    field_names=headers
    # Add field names to the table
    table.field_names = field_names
    for r in row:
    # Add data rows to the table
        table.add_row(r)

    # Set table formatting options
    table.border = True
    table.header_style = "upper"
    table.horizontal_char = "-"
    table.vertical_char = "|"
    table.junction_char = "+"

    # Print the green-bordered table
    print(table.get_string().replace("-", GREEN + "-" + RESET).replace("|", GREEN + "|" + RESET))

def red_table(headers,row):
    table = PrettyTable()

    # Define the field names (headers)
    # field_names = ["Header 1", "Header 2", "Header 3"]
    field_names=headers
    # Add field names to the table
    table.field_names = field_names
    for r in row:
    # Add data rows to the table
        table.add_row(r)

    # Set table formatting options
    table.border = True
    table.header_style = "upper"
    table.horizontal_char = "-"
    table.vertical_char = "|"
    table.junction_char = "+"

    # Print the green-bordered table
    print(table.get_string().replace("-", RED + "-" + RESET).replace("|", RED + "|" + RESET))