# Styling for the CLI app using import rich

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

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