# Styling for the CLI app using Rich

import os
import pyfiglet
from rich.console import Console
from rich.table import Table

console = Console(style="bold")

# ========= Basic Print Functions =========
    
def print_error(message):
    console.print(message, style="on #ffc182")

def print_success(message):
    console.print(message, style="on #94ffcb")

def print_info(message):
    console.print(message, style="on #fff200")

# ========= ASCII Art Title =========

def print_rainbow_text(text, font='ANSI_Shadow'):
    """Fun ASCII art with bright rainbow colors on black background"""
    figlet_text = pyfiglet.figlet_format(text, font=font)
    
    rich_colors = ["#ff7a7a", "#fff27e", "#94ffcb", "#9eeaff", "#d6aeff", "#ff9bcd"]  # Colours for rainbow effect

    lines = figlet_text.splitlines()
    max_line_length = max(len(line) for line in lines) if lines else 0  # Find the longest line to calculate proper padding
    total_width = max_line_length + 8  # 4 spaces on each side
    
    for _ in range(3):  # 3 lines of padding above
        console.print(" " * total_width, style="on black")
    
    for i, line in enumerate(lines):
        colored_line = ""
        for j, char in enumerate(line):
            color_index = (j + i) % len(rich_colors)
            color = rich_colors[color_index]
            # Use Rich markup with bright colors
            colored_line += f"[bold {color}]{char}[/bold {color}]"
        
        # Add proper padding to eliminate white space
        left_padding = "    "  # 4 spaces on left
        right_padding = " " * (total_width - len(line) - 4)  # Fill remaining space
        padded_line = left_padding + colored_line + right_padding
        console.print(padded_line, style="on black")
    
    # Add empty lines below (bottom padding)
    for _ in range(2):  # 2 lines of padding below
        console.print(" " * total_width, style="on black")

# ========= App Title Display =========
def show_app_title():
    """Display the app title with rainbow styling"""
    console.print("="*50)
    print_rainbow_text("TO DO.", font='ANSI_Shadow')
    console.print("="*50 + "\n")

# ========= Task Table =========
def create_task_table(username):
    """Table for displaying tasks with proper styling"""
    table = Table(
        show_header=True,
    )
    
    # Each column gets a different color style
    table.add_column(
        "Task Number", 
        width=15, 
        justify="center",
        style="on #EFB4FF"  # light purple
    )
    
    table.add_column(
        "Task", 
        min_width=30, 
        justify="center",
        style="on #B4F2FF" # light blue
    )
    
    table.add_column(
        "Done", 
        width=6, 
        justify="center",
        style="on #ffffa3"  # light yellow
    )
    
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