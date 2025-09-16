import tkinter as tk

root = tk.Tk()
root.title("Character Formatting Demo")

# Create Text widget
text_widget = tk.Text(root, height=5, width=40)
text_widget.pack(padx=10, pady=10)

# Insert sample text
sample_text = "Hello World!"
text_widget.insert(tk.END, sample_text)

# Apply different formatting to each character
for i, char in enumerate(sample_text):
    # Create unique tag for each character
    tag_name = f"char_{i}"
    
    # Add tag to character
    start_idx = f"{1}.{i}"
    end_idx = f"{1}.{i+1}"
    text_widget.tag_add(tag_name, start_idx, end_idx)
    
    # Configure tag properties randomly
    import random
    
    # Random color selection
    colors = ["red", "blue", "green", "purple", "orange"]
    text_widget.tag_config(
        tag_name,
        foreground=random.choice(colors),
        font=("Arial", 12, random.choice(["normal", "bold", "italic"]))
    )

# Make text read-only
text_widget.config(state="disabled")

root.mainloop()