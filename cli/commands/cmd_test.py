import os

import click
import pytest


@click.command()
@click.argument('path', default=os.path.join('opus', 'tests'))
def cli(path):
    """
    Run py.test
    
    :return: 
    """
    return pytest.main([path])
