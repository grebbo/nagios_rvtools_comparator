import argparse


# parse command line args
def parse_args():
    # pick arguments from command line
    argument_parser = argparse.ArgumentParser(
        description='Find differences between VMs in Nagios monitoring and RVTools.')
    argument_parser.add_argument(
        "-m", "--monitoring",
        type=str, default=None,
        help="Path to Nagios monitoring file.")
    argument_parser.add_argument(
        "-rv", "--rvtools",
        type=str, default=None,
        help="Path to RVTools file.")
    argument_parser.add_argument(
        "-n", "--name",
        type=str, default="Nagios-RVTools",
        help="Path to RVTools file.")

    return vars(argument_parser.parse_args())
