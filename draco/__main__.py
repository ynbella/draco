from pathlib import Path
from os import scandir, listdir
from os.path import join
from prompt import Prompt
from constellation import Constellation
from nightsky import NightSky
from tqdm import tqdm, trange

import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c_dir",
        type=Path,
        default=Path(__file__).absolute().parent.parent / "data/constellations",
        help="Path to directory of constellations reference images",
    )
    parser.add_argument(
        "-s_dir",
        type=Path,
        default=Path(__file__).absolute().parent.parent / "data/samples",
        help="Path to the directory of sample images",
    )
    parser.add_argument(
        "-tri_method",
        type=float,
        default=0,
        help="Method for triangularization"
    )
    parser.add_argument(
        "-tri_limit",
        type=float,
        default=1000,
        help="Limit for triangularization randomization"
    )
    parser.add_argument(
        "-tri_tol",
        type=float,
        default=250,
        help="Tolerance for triangularization clustering"
    )
    parser.add_argument(
        "-star_limit",
        type=int,
        default=20,
        help="Maximum number of stars to extract from image"
    )

    args = parser.parse_args()

    # region Constellations

    c = []
    c_dir = args.c_dir
    c_paths = [join(c_dir, c_file) for c_file in listdir(c_dir)]

    with tqdm(c_paths, desc='Scanning constellations') as t:
        for c_path in t:
            if (c_path.endswith(".jpg") or c_path.endswith(".png")):
                c.append(Constellation(c_path))
                t.set_postfix({'current_path': c_path})

    # endregion

    # region Samples

    s = []
    s_dir = args.s_dir
    s_paths = [join(s_dir, s_file) for s_file in listdir(s_dir)]
    with tqdm(s_paths, desc='Scanning samples') as t:
        for s_path in t:
            if (s_path.endswith(".jpg") or s_path.endswith(".png")):
                s.append(
                    NightSky(s_path, star_limit=args.star_limit, tri_method=args.tri_method, tri_limit=args.tri_limit,
                             tri_tol=args.tri_tol))
                t.set_postfix({'current_path': s_path})

    # endregion

    Prompt(c, s).cmdloop()


if __name__ == "__main__":  # pragma: no cover
    main()
