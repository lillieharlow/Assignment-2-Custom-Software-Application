# # ========== todo_manager/styling.py =========
"""Styling for the CLI app using Rich, pyfiglet, and custom print functions.
Features:
Console setup: Rich and pyfiglet for colors and ASCII art.
print_error(): Red error messages.
print_success(): Green success messages.
print_info(): Pink info messages.
print_warning(): Yellow warnings.
print_welcome(): Blue welcome messages.
print_rainbow_text(): Rainbow ASCII art.
show_app_title(): Displays app title.
create_task_table(): Creates styled task table.
print_table(): Prints styled table."""

import os
import pyfiglet
from rich.console import Console
from rich.table import Table

console = Console(style="bold")

# ========= Basic Print Functions =========
def print_error(message):
    """Highlights error messages in light red"""
    console.print(message, style="on #ffb5b5")

def print_success(message):
    """Highlights success messages in light green"""
    console.print(message, style="on #c9ffe5")

def print_info(message):
    """Highlights info messages in light yellow"""
    console.print(message, style="on #fff27e")

# ========= ASCII Art Title =========
def print_rainbow_text(text, font='ANSI_Shadow'):
    """Fun ASCII art with bright rainbow colors on black background"""
    figlet_text = pyfiglet.figlet_format(text, font=font) # Generate ASCII art text
    
    rich_colors = ["#ff7a7a", "#fff27e", "#94ffcb", "#9eeaff", "#d6aeff", "#ff9bcd"]  # Colours for rainbow effect

    lines = figlet_text.splitlines()  # Split the text into lines
    max_line_length = max(len(line) for line in lines) if lines else 0  # Find the longest line to calculate proper padding
    total_width = max_line_length + 8  # 4 spaces on each side
    
    for _ in range(2):  # 2 lines of top padding
        console.print(" " * total_width, style="on black") # prints empty lines with black background
    
    for i, line in enumerate(lines): # Iterate through each line
        colored_line = ""
        for j, char in enumerate(line): # Iterate through each character in the line
            color_index = (j + i) % len(rich_colors) # Cycle through colours(colors)
            color = rich_colors[color_index] # Use Rich markup
            colored_line += f"[bold {color}]{char}[/bold {color}]" # Add color to each character

        left_padding = "    "  # 4 spaces on left (proper padding to remove white space)
        right_padding = " " * (total_width - len(line) - 4)  # Fill remaining space
        padded_line = left_padding + colored_line + right_padding  # Add padding to the line
        console.print(padded_line, style="on black") # Print the padded line with black background
    
    for _ in range(2):  # 2 lines bottom padding
        console.print(" " * total_width, style="on black")

# ========= App Title Display =========
def show_app_title():
    """Display app title/goodbye with rainbow styling"""
    console.print("="*50)
    print_rainbow_text("TO DO.", font='ANSI_Shadow')
    console.print("="*50 + "\n")

# ========= Task Table =========
def create_task_table(username):
    """Display tasks in a table format. Each column has different colour."""
    table = Table(title=f"{username}'s Tasks", show_header=True)
    
    table.add_column("Task Number", width=15, justify="center", style="on #F8E1FF")  # light purple
    table.add_column("Task", min_width=30, justify="center", style="on #D9F9FF")  # light blue
    table.add_column("Done", width=6, justify="center", style="on #fff27e")  # light yellow
    
    return table

# ========= Print Table =========
def print_table(table):
    """Print a table with proper spacing"""
    console.print(table)
    
# ========= Clear screen styling =========
    
def clear_screen():
    """Clear screen for better visibility"""
    os.system('clear')  # Clear terminal
    show_app_title()