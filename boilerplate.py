#!/usr/bin/env python3
# z@xnz.me
import configparser
import argparse
import os
import subprocess

config_file = 'config.ini'
config = {}


def main():
    global config

    config = read_config()
    args = parse_args()

    print(args)
    print(config['enable_logging'])

    if args.subprocess:
        run_subprocess()


def run_subprocess():
    subprocess.call(['ls', '-l'])


def read_config():
    global config_file

    if not os.path.isfile(config_file):
        print(config_file + ' not found, please create one.')
        raise SystemExit

    conf = configparser.ConfigParser()

    conf.read(config_file)

    return conf['default']


def parse_args():
    parser = argparse.ArgumentParser(description='A foo that bars',
                                     epilog="And that's how you'd foo a bar")

    parser.add_argument('--foo', nargs='?', help='foo help')
    parser.add_argument('--bar', nargs='+', help='bar help')
    parser.add_argument('--subprocess', nargs='?', help="Run a subprocess", const=run_subprocess)

    subparsers = parser.add_subparsers(help='sub-command help',
                                       dest='route'
                                       )
    subparsers.required = True

    parser_a = subparsers.add_parser('route1', help='route1 help')
    parser_a.add_argument('bar', nargs='?', type=int, help='bar help')
    parser_a.add_argument('--baz', nargs='?', type=str, help='bar help')

    parser_b = subparsers.add_parser('route2', help='route2 help')
    parser_b.add_argument('--baz', choices=['rock', 'paper', 'scissors'], help='baz help')

    parser.add_argument("parameter", nargs='?', help="A parameter", type=str)

    return parser.parse_args()


if __name__ == "__main__":
    main()
