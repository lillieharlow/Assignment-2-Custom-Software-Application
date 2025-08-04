# Styling for the CLI app using Rich

from rich.console import Console
import pyfiglet
from rich.table import Table

console = Console()

# ========= Basic Print Functions =========

def print_error(message):
    console.print(message, style="bold #ff0000")

def print_success(message):
    console.print(message, style="bold #69f0ae")

def print_info(message):
    console.print(message, style="bold #ff1493")

def print_warning(message):
    console.print(message, style="bold #ffeb3b")

def print_welcome(message):
    console.print(message, style="bold #40c4ff")

# ========= ASCII Art Title =========

def print_rainbow_text(text, font='ANSI_Shadow'):
    """Main title - ASCII art with bright rainbow colors on black background"""
    figlet_text = pyfiglet.figlet_format(text, font=font)
    
    rich_colors = ["#ff7979", "#fff27e", "#94ffcb", "#9eeaff", "#d6aeff", "#ff9bcd"]  # Colours for rainbow effect

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
    for _ in range(3):  # 3 lines of padding below
        console.print(" " * total_width, style="on black")

# ========= App Title Display =========
def show_app_title():
    """Display the app title with rainbow styling"""
    print("\n" + "="*50)
    print_rainbow_text("TO DO.", font='ANSI_Shadow')
    print("="*50 + "\n")
    print_info("A TASK MANAGEMENT APP THAT HELPS YOU STAY ON TRACK")

# ========= Task Table =========
def create_task_table(username):
    """Create a beautifully styled task table"""
    table = Table(
        title=f"[bold cyan]{username}'s Task Manager[/bold cyan]", 
        show_header=True, 
        header_style="bold magenta"
    )
    table.add_column("#", style="cyan", width=4, justify="center")
    table.add_column("Status", style="magenta", width=8, justify="center")
    table.add_column("Task", style="green", min_width=20)
    
    return table