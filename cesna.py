import snap
import logging
import argparse
import pathlib
import time

def setup_argparse():
    parser = argparse.ArgumentParser()

    io_options = parser.add_argument_group("I/O options")
    io_options.add_argument("-i", "--input",
            default="data/1912.edges",
            type=str,
            help="File for edgelist",
            required=False)
    io_options.add_argument("-o", "--output",
            default="",
            type=str,
            help="Output file prefix",
            required=False)
    io_options.add_argument("-l", "--labels",
            default=None,
            type=str,
            help="File name for node names (ID, label)",
            required=False)
    io_options.add_argument("-a", "--attributes",
            default="data/1912.nodefeat",
            type=str,
            help="File with node attributes",
            required=False)
    io_options.add_argument("-n", "--names-attrs",
            default="data/1912.nodefeatnames",
            type=str,
            help="File with node attribute names",
            required=False)

    comm_options = parser.add_argument_group("Communities options")
    comm_options.add_argument("-c", "--comm-opt",
            default=10,
            type=int,
            help="Number of communities to detect (-1 for auto)",
            required=False)
    comm_options.add_argument("-cm", "--comm-min",
            default=3,
            type=int,
            help="Minimal number of communities to try",
            required=False)
    comm_options.add_argument("-cx", "--comm-max",
            default=20,
            type=int,
            help="Maximum number of communities to try",
            required=False)
    comm_options.add_argument("-ct", "--comm-trials",
            default=5,
            type=int,
            help="How many trials for the number of communities",
            required=False)

    parser.add_argument("-nt", "--n-threads",
            default=1,
            type=int,
            help="Number of threads for parallelization",
            required=False)

    reg_options = parser.add_argument_group("Regularization options")
    reg_options.add_argument("-aw", "--attrs-w",
            default=0.5,
            type=float,
            help="Regularization coeff in (1 - c) * P(Network) + c * P(Attributes)",
            required=False)
    reg_options.add_argument("-lw", "--lasso-reg",
            default=1.0,
            type=float,
            help="Weight for L1 regularization",
            required=False)
    reg_options.add_argument("-sa", "--step-alpha",
            default=0.05,
            type=float,
            help="Alpha for backtracking line search",
            required=False)
    reg_options.add_argument("-sb", "--step-beta",
            default=0.3,
            type=float,
            help="Beta for backtracking line search",
            required=False)
    reg_options.add_argument("-mf", "--min-feat-fraction",
            default=0.0,
            type=float,
            help="If the fraction of nodes with possible values for an attribute is " +
                 "smaller than this, we ignore that attribute",
            required=False)

    return parser


def setup_logging():
    logger = logging.getLogger('cesna')

    logger.setLevel(logging.DEBUG)
    fh = logging.FileHandler('cesna-debug.log')
    fh.setLevel(logging.DEBUG)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger

if __name__ == "__main__":
    start_time = time.time()
    logger = setup_logging()
    logger.info("Starting Cesna.py")

    parser = setup_argparse()
    args = parser.parse_args()
    logger.debug(f"Got argument: {args}")

    G = snap.LoadConnList_PUNGraph(args.input)
    logger.debug(f"Read edges to graph: {G}")

    if args.labels is not None:
        # todo: parse labels
        pass

    logger.info(f"Graph: nodes: {G.GetNodes()}, edges: {G.GetEdges()}")

    if args.attributes is not None:
        # todo: load attributes
        pass

    # todo: get cesna sources from cpp part

    end_time = time.time()
    logger.info(f"Done in {end_time - start_time} sec")


