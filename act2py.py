import kagglehub
from kagglehub import KaggleDatasetAdapter
from rich.console import Console
from rich.table import Table
from rich.align import Align
from rich.panel import Panel
from rich.console import Group

console = Console()

file_path = "student_lifestyle_performance_dataset.csv"

df = kagglehub.dataset_load(
    KaggleDatasetAdapter.PANDAS,
    "sehaj1104/student-lifestyle-and-academic-performance-dataset",
    file_path,
    pandas_kwargs={"nrows": 1000}
)

numeric_df = df.select_dtypes(include="number")
data = numeric_df["Study_Hours_per_Day"]

mean = data.mean()
median = data.median()
mode = data.mode()[0] if not data.mode().empty else "No mode"
data_range = data.max() - data.min()
variance = data.var()
std_dev = data.std()

table = Table(show_header=True, header_style="bold cyan")
table.add_column("Metric", justify="center")
table.add_column("Value", justify="center")

table.add_row("Mean", f"{mean:.2f}")
table.add_row("Median", f"{median:.2f}")
table.add_row("Mode", str(mode))
table.add_row("Range", f"{data_range:.2f}")
table.add_row("Variance", f"{variance:.2f}")
table.add_row("Standard Deviation", f"{std_dev:.2f}")

title = Panel(
    Align.center("[bold magenta]Central Tendency and Variability of Study Hours Per Day of Students[/bold magenta]"),
    expand=False
)

footer = Panel (
    Group(
        Align.center("[bold magenta]Activity 2[/bold magenta]"),
        Align.center("[bold green]Name: Noel Jhumel G. Blanco[/bold green]"),
        Align.center("[bold green]Date: February 15, 2026[/bold green]"),
        Align.center("[bold green]Subject: Quantitative Methods[/bold green]"),   
        Align.center("[bold green]Instructor: Cheryll S. Pagal MSAMS[/bold green]"),
    ),
    expand=False
)


console.print(Align.center(title))
console.print(Align.center(table))
console.print(Align.center(footer))



