import click

from linum import Loader, Context, TxtRendererContext
from linum.txt_renderer import CharPainter


@click.command()
@click.argument('tasks_filename', type=click.Path(exists=True))
@click.option('-o', '--out', type=click.Path(writable=True),
              help='Output filepath')
@click.option('-r', '--renderer', default='CP', type=click.Choice(['CP'],),
              help="Renderer to use. 'CP' - for char painter. "
                   "Default is 'CP'.")
@click.option('-c', '--context', type=click.Path(exists=True),
              help="Context for renderer. It is yaml file with render settings.")
def cli(tasks_filename, out, renderer, context):
    """ Command line interface for linum. """
    # Load tasks
    tasks = Loader().load_tasks(tasks_filename)

    # txt_renderer out
    if renderer == 'CP':
        context = Loader().load_txt_renderer_context(context) if context else TxtRendererContext()
        cp = CharPainter(tasks, context)
        if out:
            file = open(out, mode='wt', encoding='utf-8')
            file.write(cp.render())
        else:
            click.echo(cp.render())


if __name__ == '__main__':
    cli()
