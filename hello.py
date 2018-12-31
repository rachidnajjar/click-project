# -*- coding: utf-8 -*-
import click


class Config(object):
    def __init__(self):
        self.verbose = False

pass_config = click.make_pass_decorator(Config,  ensure=True)

@click.group()
@click.option("--verbose", is_flag=True)
@click.option("--home-directory", type=click.Path())
@pass_config
def cli(config, verbose, home_directory):
    config.verbose = verbose
    if home_directory is None:
        home_directory = '.'
    config.home_directory = home_directory

@click.command()
@click.option("--name", default="tout le monde", help="Nom de l'utilisateur")
@click.option("--repeat", default=1, help="Nombre de message de bienvenue")
@click.argument("out", type=click.File('w'), default='-', required=False)
@pass_config
def welcome(config, name, repeat, out):
    '''Ce script souhaite la bienvenue.'''
    if config.verbose:
        click.echo("We are in verbose mode")
    
    click.echo("Home directory is %s" % config.home_directory)
    
    for i in range(repeat):
        click.echo("Bonjour %s !" % name, file=out)
        
@click.command()
@pass_config
def initdb(config):
    '''Ce script initialise la base de données.'''
    if config.verbose:
        click.echo("We are in verbose mode")

    click.echo('Initialized the database')

@click.command()
@pass_config
def dropdb(config):
    '''Ce script supprime la base de données.'''
    if config.verbose:
        click.echo("We are in verbose mode")

    click.echo('Dropped the database')


cli.add_command(welcome)
cli.add_command(initdb)
cli.add_command(dropdb)