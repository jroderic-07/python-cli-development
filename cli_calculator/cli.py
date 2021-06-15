import click
import operations

@click.group()
def cli():
    pass

@click.command()
@click.argument('nums', type=float, nargs=-1)
def addition(nums):
    click.echo(operations.addition(nums))

@click.command()
@click.argument('nums', type=float, nargs=-1)
def subtraction(nums):
    click.echo(operations.operation(nums, '-'))

@click.command()
@click.argument('nums', type=float, nargs=-1)
def multiplication(nums):
    click.echo(operations.operation(nums, '*'))

@click.command()
@click.argument('nums', type=float, nargs=-1)
def division(nums):
    click.echo(operations.operation(nums, '/'))

cli.add_command(addition)
cli.add_command(subtraction)
cli.add_command(multiplication)
cli.add_command(division)

if __name__ == '__main__':
    cli()
