# Styling for the CLI app using Rich

from rich.console import Console
import pyfiglet

console = Console()

# ========= Basic Print Functions =========

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

# ========= ASCII Art Functions =========

def print_rainbow_text(text, font='big'):
    """Create rainbow ASCII art text using pyfiglet"""
    # Create ASCII art using pyfiglet
    figlet_text = pyfiglet.figlet_format(text, font=font)
    
    # Rich rainbow colors
    colors = ['bright_red', 'bright_yellow', 'bright_green', 'bright_cyan', 'bright_blue', 'bright_magenta']
    
    lines = figlet_text.splitlines()
    
    for i, line in enumerate(lines):
        colored_line = ""
        for j, char in enumerate(line):
            color_index = (j + i) % len(colors)
            color = colors[color_index]
            colored_line += f"[bold {color}]{char}[/bold {color}]"
        
        console.print(colored_line)

def show_app_title():
    """Display the app title with rainbow styling"""
    print("\n" + "="*60)
    print_rainbow_text("TO DO.", font='big')  # Your beautiful ASCII art!
    print("="*60 + "\n")
    print_info("Your personal task manager that cares about you!")