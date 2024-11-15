import click
import numpy as np
from numpy import pi
import pandas as pd


@click.group()
def cmd_group():
    """Initializes the cmd_group click group
    """
    pass

@cmd_group.command()
@click.option(
    "--number",
    "-n",
    default = 10,
    help = "Amount of numbers printed",
    show_default = True,
)
def sin(number):
    """Display numbers and their sinus values as if they were radians.

    NUMBER gives the amount of numbers.
    """    
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)

@cmd_group.command()
@click.option(
    "--number",
    "-n",
    default = 10,
    help = "Amount of numbers printed",
    show_default = True,
)
def tan(number):
    """Display numbers and their tangent values as if they were radians.

    NUMBER gives the amount of numbers shown.
    """
    x = np.linspace(0, 2 * pi, int(number))
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)


if __name__ == "__main__":
    cmd_group()