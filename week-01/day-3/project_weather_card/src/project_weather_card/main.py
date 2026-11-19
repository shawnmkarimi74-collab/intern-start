from rich import print
from rich.panel import Panel

weather = """
City: Kermanshah
Temperature: 18 C
Weather: Sunny
Humidity: 35%
"""

print(Panel(weather, title="Weather Card", style="cyan"))