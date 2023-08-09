import tkinter as tk
from tkinter import ttk

# Sample data (replace this with your data)
data = [
    ["INFY", 1650.0, 1655.0, 1640.0, 1645.5, "IT"],
    ["TCS", 3750.0, 3770.0, 3740.0, 3755.75, "IT"],
    ["HDFCBANK", 1500.0, 1510.0, 1495.0, 1502.25, "Banking"],
    # Add more rows as needed
]

def create_table():
    table = ttk.Treeview(root)

    # Define columns
    table["columns"] = ("Symbol", "Open", "High", "Low", "LTP", "Sector")
    table.column("#0", width=0, stretch=tk.NO)  # For a hidden column (needed for Treeview)
    table.column("Symbol", anchor=tk.CENTER, width=100)
    table.column("Open", anchor=tk.CENTER, width=100)
    table.column("High", anchor=tk.CENTER, width=100)
    table.column("Low", anchor=tk.CENTER, width=100)
    table.column("LTP", anchor=tk.CENTER, width=100)
    table.column("Sector", anchor=tk.CENTER, width=100)

    # Define column headings
    table.heading("#0", text="", anchor=tk.CENTER)
    table.heading("Symbol", text="Symbol", anchor=tk.CENTER)
    table.heading("Open", text="Open", anchor=tk.CENTER)
    table.heading("High", text="High", anchor=tk.CENTER)
    table.heading("Low", text="Low", anchor=tk.CENTER)
    table.heading("LTP", text="LTP", anchor=tk.CENTER)
    table.heading("Sector", text="Sector", anchor=tk.CENTER)

    # Add data to the table
    for row in data:
        table.insert("", tk.END, values=row)

    # Pack the table and make it scrollable
    table.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
    scrollbar = ttk.Scrollbar(root, orient=tk.VERTICAL, command=table.yview)
    table.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create the main Tkinter window
root = tk.Tk()
root.title("Nifty 50 Table")

# Create the table
create_table()

# Start the Tkinter event loop
root.mainloop()
