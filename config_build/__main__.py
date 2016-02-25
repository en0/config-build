#!/usr/bin/env python
from argparse import ArgumentParser, FileType
from os.path import realpath, dirname, join
from sys import argv, stdout
from jinja2 import Environment
from pprint import pprint as pp

try:
    from ConfigParser import ConfigParser
except ImportError:
    from configparser import ConfigParser


def get_opts(args):
    ap = ArgumentParser()
    ap.add_argument(
        "-o", "--output",
        type=FileType('w'),
        default=stdout,
        help="Specify where to write the result. (Default: STDOUT)"
    )
    ap.add_argument(
        "-t", "--template",
        type=FileType('r'),
        default=open(join(dirname(realpath(__file__)), "template"), 'r'),
        help="Override the default generation template."
    )
    ap.add_argument(
        "INI",
        type=FileType('r'),
        help="The INI file to use as a model"
    )
    return ap.parse_args(args)


def ini2keys(fp):
    cp = ConfigParser()
    cp.optionxform = str
    cp.readfp(fp)

    default_keys = [x for x in cp.defaults()]
    keys = {'DEFAULT': default_keys}

    for section in cp.sections():
        keys[section] = [
            o for o in cp.options(section)
            if o not in default_keys
        ]
    del cp
    return keys


def main(args=None):
    _opts = get_opts(args or argv[1:])
    _template_str = _opts.template.read()
    keys = ini2keys(_opts.INI)
    output = Environment().from_string(_template_str).render(config=keys)
    _opts.output.write(output)

if __name__ == "__main__":
    main()
