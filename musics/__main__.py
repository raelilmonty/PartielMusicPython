"""CLI public options."""

import argparse

from . import cli

parser = argparse.ArgumentParser(
    prog='muscis',
    description='Display various information about music',
)
parser.add_argument(
    'command',
    help='command to launch',
    choices=('artists', 'tracks', 'customers'),
)
parser.add_argument(
    '--top',
    help='number of top elements to display',
    type=float,
    default=10,
)

def main(argv=None):
    args = parser.parse_args(argv)
    if (top := args.top) <= 0:
        raise argparse.ArgumentTypeError(f'{top} is not a positive number')
    match args.command:
        case 'artists':
            cli.top_artists(top)
        case 'tracks':
            cli.top_tracks(top)
        case 'customers':
            cli.top_customers(top)


if __name__ == '__main__':  # pragma: no cover
    main()
