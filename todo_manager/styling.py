# # ========== todo_manager/styling.py =========
"""Styling for the CLI app using Rich, pyfiglet, and custom print functions.
Features:
Console setup: Rich and pyfiglet for colors and ASCII art.
print_error(): Red error messages.
print_success(): Green success messages.
print_info(): Pink info messages.
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
    """Error messages in red"""
    console.print(message, style="#ff0000", markup=True)

def print_success(message):
    """Success messages in green"""
    console.print(message, style="#00ff84", markup=True)

def print_info(message):
    """Info messages in yellow"""
    console.print(message, style="#ffe600", markup=True)

# ========= ASCII Art Title =========
def print_rainbow_text(text, font='ANSI_Shadow'):
    """
    Print text as rainbow-coloured ASCII art using pyfiglet and Rich.
    Steps:
    1. Convert the input text to ASCII art using pyfiglet.
    2. Colour each character in the ASCII art with a cycling rainbow palette.
    3. Add padding above, below, and on the sides for a neat look.
    """
    # Step 1: Generate ASCII art from the input text
    figlet_text = pyfiglet.figlet_format(text, font=font)

    # Step 2: Define a list of hex colour codes for the rainbow effect
    rich_colors = [
        "#ff7a7a",  # Red
        "#fff27e",  # Yellow
        "#94ffcb",  # Green
        "#9eeaff",  # Blue
        "#d382ff",  # Purple
        "#fe85c2"   # Pink
    ]

    # Split the ASCII art into lines for processing
    lines = figlet_text.splitlines()

    # Find the length of the longest line to set the total width for padding
    max_line_length = max(len(line) for line in lines) if lines else 0
    total_width = max_line_length + 8  # 4 spaces of padding on each side

    # Step 3: Print 2 empty lines at the top for vertical padding
    for _ in range(2):
        console.print(" " * total_width)

    # Loop through each line of the ASCII art
    for i, line in enumerate(lines):
        colored_line = ""  # This will store the coloured version of the line
        # Loop through each character in the line
        for j, char in enumerate(line):
            # Pick a colour from the rainbow palette, cycling through the list
            color_index = (j + i) % len(rich_colors)
            color = rich_colors[color_index]
            # Add Rich markup to make the character bold and coloured
            colored_line += f"[bold {color}]{char}[/bold {color}]"

        # Add 4 spaces of padding to the left
        left_padding = "    "
        # Add enough spaces to the right to fill the total width
        right_padding = " " * (total_width - len(line) - 4)
        # Combine left padding, coloured line, and right padding
        padded_line = left_padding + colored_line + right_padding
        # Print the padded, coloured line
        console.print(padded_line)

    # Step 4: Print 2 empty lines at the bottom for vertical padding
    for _ in range(2):
        console.print(" " * total_width)

# ========= App Title Display =========
def show_app_title():
    """Display app title/goodbye with rainbow styling"""
    console.print("="*50)
    print_rainbow_text("TO DO.", font='ANSI_Shadow')
    console.print("="*50 + "\n")

# ========= Task Table =========
def create_task_table(username):
    """Display tasks in a table format. Each column has different colour."""
    table = Table(title=f"{username}'s Tasks", style="#00fbff", show_header=True)

    table.add_column("TASK #", width=8, justify="center", header_style="#d382ff")
    table.add_column("TASK", min_width=30, justify="center", header_style="#fe85c2")
    table.add_column("DONE", width=8, justify="center", header_style="#ff7a7a")

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