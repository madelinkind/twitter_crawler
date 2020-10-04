import argparse

# https://docs.python.org/3/howto/argparse.html

DATABASE_STORAGE = 'DATABASE'
FILESYSTEM_STORAGE = 'FILESYSTEM'

STORAGE_TYPES = [
    DATABASE_STORAGE,
    FILESYSTEM_STORAGE,
]

# ------------------------------------------------------


def create_twitter_crawler_parser(desc='Twitter Crawler'):
    return argparse.ArgumentParser(description=desc)


def configure_twitter_crawler_parser(parser):
    # verbose optiobal parameter
    parser.add_argument(
        "-v", "--verbose",
        required=False,
        default=True,
        help="Indicates if output is verbose or not"
    )

    # verbose optiobal parameter
    parser.add_argument(
        "-s", "--storage",
        required=False,
        default=FILESYSTEM_STORAGE,
        choices=STORAGE_TYPES,
        help="Indicates if output is verbose or not"
    )

    return parser


if __name__ == '__main__':
    # create parser
    parser = create_twitter_crawler_parser()

    # configure parser
    parser = configure_twitter_crawler_parser(parser)

    # parse arguments
    args = parser.parse_args()

    if (args.verbose):
        print('Verbosity turned ON')

    print(f"storage={args.storage}")

    # TODO invoke desired functionality
