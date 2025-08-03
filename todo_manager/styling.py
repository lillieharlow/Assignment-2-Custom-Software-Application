# Styling for the CLI app using import rich

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
import pyfiglet

console = Console()

def print_error(message):
    """Print error message in bold red."""
    console.print(message, style="bold red")

def print_success(message):
    """Print success message in bold green."""
    console.print(message, style="bold green")

def print_info(message):
    """Print info message in bold cyan."""
    console.print(message, style="bold cyan")

def print_warning(message):
    """Print warning message in bold yellow."""
    console.print(message, style="bold yellow")

def print_welcome(message):
    """Print welcome message in bold magenta."""
    console.print(message, style="bold magenta")

def print_panel(title, message, style="bold green"):
    """Print message in a fancy panel."""
    panel = Panel(message, title=title, style=style)
    console.print(panel)

def print_header(text):
    """Print a stylized header."""
    console.print(f"\n{'='*50}", style="bold cyan")
    console.print(text.center(50), style="bold magenta")
    console.print(f"{'='*50}", style="bold cyan")
    
def print_menu():
    """Print the main menu with nice spacing."""
    console.print("\nPlease choose an option:", style="bold white")
    console.print("1. Sign up", style="cyan")
    console.print("2. Log in", style="cyan") 
    console.print("3. Log out", style="cyan")
    console.print("4. Exit", style="cyan")

def print_spacing():
    """Add extra spacing when needed."""
    console.print("\n")

# ========= ASCII Art Styling =========

def print_rainbow_text(text, font='ANSI_Shadow'):
    """Main title - ASCII art with bright rainbow colors on black background"""
    figlet_text = pyfiglet.figlet_format(text, font=font)
    
    # Colours for rainbow effect
    rich_colors = ['bright_red', 'bright_yellow', 'bright_green', 'bright_cyan', 'bright_blue', 'bright_magenta']
    
    lines = figlet_text.splitlines()
    
    # Find the longest line to calculate proper padding
    max_line_length = max(len(line) for line in lines) if lines else 0
    total_width = max_line_length + 8  # 4 spaces on each side
    
    # Add empty lines above (top padding)
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

def show_app_title():
    """Display the app title with rainbow styling"""
    print("\n" + "="*50)
    print_rainbow_text("TO DO.", font='ANSI_Shadow')
    print("="*50 + "\n")
    print_info("Your personal task manager that cares about you!")