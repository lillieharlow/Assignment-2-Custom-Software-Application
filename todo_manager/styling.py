"""Styling for the CLI app using Rich, pyfiglet, and custom print functions
Features:
Console setup: Rich and pyfiglet for colors and ASCII art
print_error(): Red error messages
print_success(): Green success messages
print_info(): Yellow info messages
print_rainbow_text(): Rainbow ASCII art
show_app_title(): Displays app title
create_task_table(): Creates styled task table
print_table(): Prints styled table"""

import os
import pyfiglet
from rich.console import Console
from rich.table import Table

console = Console(style="bold")

# ========= Basic Print Functions =========
def print_error(message):
    """Error messages in red"""
    console.print(f"[bold #ff0000]{message}[bold /#ff0000]", markup=True) # force rich to style all text bold in red

def print_success(message):
    """Success messages in green"""
    console.print(message, style="#00ff84", markup=True)

def print_info(message):
    """Info messages in yellow"""
    console.print(message, style="#ffe600", markup=True)

def red_text(message):
    return f"[bold #ff0000]{message}[bold /#ff0000]" # red text for TDD testing implementation

# ========= ASCII Art Title =========
def print_rainbow_text(text, font='ANSI_Shadow'):
    """Rainbow ASCII art with pyfiglet and Rich"""
    figlet_text = pyfiglet.figlet_format(text, font=font) # Convert input text to ASCII art with pyfiglet

    rich_colors = [   # List rainbow colours
        "#ff7a7a",  # Red
        "#fff27e",  # Yellow
        "#94ffcb",  # Green
        "#9eeaff",  # Blue
        "#d382ff",  # Purple
        "#fe85c2"   # Pink
    ]
    
    lines = figlet_text.splitlines()  # Split the ASCII art into lines for processing
    max_line_length = max(len(line) for line in lines) if lines else 0 # Find length of longest line to set total width for padding
    total_width = max_line_length + 8  # 4 spaces of padding on each side

    for _ in range(2):
        console.print(" " * total_width) # Print 2 empty lines for padding at top

    for i, line in enumerate(lines): # Loop through each line of the ASCII art
        colored_line = ""  # Store the coloured version of the line
        for j, char in enumerate(line): # Loop through each char in the line
            color_index = (j + i) % len(rich_colors) # Pick colour and cycle through rainbow colours
            color = rich_colors[color_index]
            colored_line += f"[bold {color}]{char}[/bold {color}]" # Add Rich markup to bold and colour char

        left_padding = "    " # padding on left
        right_padding = " " * (total_width - len(line) - 4) # padding on right
        padded_line = left_padding + colored_line + right_padding # combine left and right
        console.print(padded_line) # Print padded line

    console.print(" " * total_width) # Bottom padding

# ========= App Title =========
def show_app_title():
    """Display app title/goodbye with rainbow styling"""
    console.print("="*50)
    print_rainbow_text("TO DO.", font='ANSI_Shadow')
    console.print("="*50 + "\n")

# ========= Task Table =========
def create_task_table(username):
    """Display tasks in a table format. Each column has different colour."""
    table = Table(title=f"{username}'s Tasks", style="#00fbff", show_header=True)

    table.add_column("TASK #", width=8, justify="center", header_style="#d382ff") # Purple
    table.add_column("TASK", min_width=30, justify="center", header_style="#fe85c2") # Pink
    table.add_column("DONE", width=8, justify="center", header_style="#ff7a7a") # Red

    return table

# ========= Print Table =========
def print_table(table):
    """Print a table with proper spacing with Rich library"""
    console.print(table)
    
# ========= Clear screen styling =========
    
def clear_screen():
    """Clear screen for better visibility with os"""
    os.system('clear')
    show_app_title()