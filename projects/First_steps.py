import tkinter as tk
    
def submit_data():
    data = entry.get()
    print(f"Data entered: {data}")
    
# Create the main window
root = tk.Tk()
root.title("Data Entry")
    
# Create a label and entry widget
label = tk.Label(root, text="Enter data:")
label.pack(pady=10)
entry = tk.Entry(root)
entry.pack(pady=10)
    
    # Create a submit button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.pack(pady=10)
    
    # Run the application
root.mainloop()