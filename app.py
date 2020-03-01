#!/usr/bin/env python
import click

@click.command()
@click.option('--name', prompt='Your name',
              help='The person to greet.')
              
@click.option('--place', prompt='Where are you from?')     

              
def hello(name, place):
    """Simple program that greets NAME for a total of COUNT times."""
    click.echo('Hello %s from %s! Welcome to DockerHub!' % (name, place))


if __name__ == '__main__':
    hello()
    
    
    
    

