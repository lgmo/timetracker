import click
from click_default_group import DefaultGroup

# @click.group()
@click.group(cls=DefaultGroup, default='all', default_if_no_args=True)
def cli():
    pass

@cli.command()
def all():
    print('all tasks')

@cli.command()
@click.option('--name')
@click.option('--id')
@click.option('--date')
@click.pass_context
def task(ctx, name=None, id=None, date=None, begin=None, end=None, status=None):
    if name != None:
        print(f'tasks found by name {name}')
    elif id != None:
        print(f'task found by {id}')
    elif date != None:
        print(f'tasks found by {date}')
    else:
        click.echo(ctx.get_help())

@cli.command()
@click.argument('id')
def remove(id):
    print(f'remove task with id {id}')

@cli.command()
@click.argument('id')
@click.option('--name')
@click.option('--begin')
@click.option('--end')
@click.option('--status')
def update(id, name=None, begin=None, end=None, status=None):
    if name != None:
        print('update name')
    if begin !=  None:
        print('update begin')
    if end != None:
        print('update end')
    if status != None:
        print('udate status')
