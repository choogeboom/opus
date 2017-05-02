import click
import subprocess


@click.command()
@click.option('--skip-init/--no-skip-init', default=True,
              help='Skip __init__.py files?')
@click.argument('path', default='opus')
def cli(skip_init, path):
    """
    Run flake8 to analyze the codebase
    
    :param skip_init: whether to skip package __init__.py files  
    :param path: root path
    :return: the result
    """
    flake8_flag_exclude = ' --exclude __init__.py' if skip_init else ''

    command = 'flake8 {0}{1}'.format(path, flake8_flag_exclude)
    return subprocess.run(command, shell=True)
