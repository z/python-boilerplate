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

    parser.add_argument('routes', choices=['rock', 'paper', 'scissors'], help="A route to rock, paper or scissors")
    parser.add_argument("parameter", nargs='?', help="A parameter", type=str)
    parser.add_argument('--foo', nargs='?', help='foo help')
    parser.add_argument('--bar', nargs='+', help='bar help')
    parser.add_argument('--subprocess', nargs='?', help="Run a subprocess", const=run_subprocess)

    return parser.parse_args()


if __name__ == "__main__":
    main()
