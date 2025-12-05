import click
from ComputeSquare import square   # importa apenas o necessário

@click.command()
@click.option(
    "-n", "--num",
    type=int,
    required=True,
    help="Specify a number to square."
)

def main(num):
    """Compute the square of a number provided via the --num option."""
    result = square(num)
    print(f"The square of {num} is {result}")