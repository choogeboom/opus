
import click
import pytest


@click.command()
@click.argument('path', default='opus')
def cli(path):
    """
    Run a test coverage report
    
    :param path: Test coverage path 
    :return: subprocess call result
    """
    return pytest.main(['--cov-report', 'term-missing', '--cov', path])
