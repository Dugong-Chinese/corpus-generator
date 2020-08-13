import click
from .extractor import parse
from .converter import json2csv
import pathlib
import os
from importlib import util


@click.group()
def process():
    """ Corpus generation tool for DugongChinese's Mandarin resource application. Please run one of the subcommands below.
    """
    pass


@process.command('json2csv')
@click.option("--in", "-i", "in_json", required=True,
              help="Path to JSON in plaintext.",
              )
@click.option("--out", "-o", 'out_csv', default="output.csv",
              help="Path to output CSV")
def j2c(in_json, out_csv):
    """ Converts the JSON progress file saved to a CSV (without statistic summaries.)
    """
    ihandle = open(in_json, 'r', encoding='utf-8')
    ohandle = open(out_csv, 'r+' if os.path.isfile(out_csv)
                   else 'w+',  encoding='utf-8')
    json2csv(ihandle, ohandle)
    ihandle.close()
    ohandle.close()


@process.command()
@click.option("--in", "-i", "in_file", required=True,
              help="Path to file in plaintext.")
@click.option("--out", "-o", 'out_json', default="output.json",
              help="Path to output JSON file containing the relative and absolute frequencies and various other stats. Updates if exists. Default: output.json")
@click.option("--chunker", "-c", 'chunking_function', required=True,
              help="Path to a module that contains a function which chunks the input file up into syntactically correct sentences. Example: ./cloze_rc_splitter.py")
@click.option("--extractor-args", "extractor_args", default=None,
              help="JSON string to pass to the extractor if supported.")
def extract(in_file, out_json, chunking_function, extractor_args):
    """Extracts vocabulary frequencies from a plaintext file."""

    # https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path
    spec = util.spec_from_file_location("chunker", chunking_function)
    chunker = util.module_from_spec(spec)
    spec.loader.exec_module(chunker)

    ihandle = open(in_file, 'r', encoding='utf-8')
    ohandle = open(out_json, 'r+' if os.path.isfile(out_json)
                   else 'w+',  encoding='utf-8')
    if extractor_args:
        parse(ihandle, ohandle, chunker.to_generator, extractor_args)
    else:
        parse(ihandle, ohandle, chunker.to_generator)

    ihandle.close()
    ohandle.close()
