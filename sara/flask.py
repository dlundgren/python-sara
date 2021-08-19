import click
from flask.cli import FlaskGroup

from sara.Kernel import Kernel

def create_app():
    """
    Create new Flask app instance
    """
    return Kernel().app


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    '''
    Main entry point.
    '''
