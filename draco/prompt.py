from cmd import Cmd
from sys import stderr
from matplotlib import pyplot as plt
from sys import exit


class Prompt(Cmd):
    def __init__(self, constellations=None, samples=None, debug=False):
        self.constellations = constellations
        self.samples = samples
        super().__init__()

    def list_samples(self):
        samples = []
        for s in self.samples:
            samples.append([s.name, s])
        return samples

    def list_constellations(self):
        constellations = []
        for c in self.constellations:
            constellations.append([c.name, c])
        return constellations

    def do_list_constellations(self, inp):
        for c in self.list_constellations():
            print(c[0])

    def help_list_constellations(self):
        print("Outputs a list of constellations that were read in at initial execution")

    def do_list_samples(self, inp):
        for s in self.list_samples():
            print(s[0])

    def help_list_samples(self):
        print("Outputs a list of samples that were read in at initial execution")

    def do_match(self, inp):
        labels = inp.split()
        if len(labels) < 2:
            print("You need to specify at least two arguments: <sample_name> <constellation_name>", file=stderr)
            return
        samples, sample = self.list_samples(), None
        for s in samples:
            if s[0] == labels[0]:
                sample = s[1]
        if sample is None:
            print("Invalid sample name", file=stderr)
            return
        constellations, constellation = self.list_constellations(), None
        for c in constellations:
            if c[0] == labels[1]:
                constellation = c[1]
        if constellation is None:
            print("Invalid constellation name", file=stderr)
            return
        method, side_tol, ang_tol = 0, 0.1, 5.0
        if len(labels) > 2:
            method = int(labels[2])
            if len(labels) > 4:
                side_tol = float(labels[3])
                ang_tol = float(labels[4])
            elif len(labels) > 3:
                ang_tol = side_tol = float(labels[3])

        matches, misses = sample.match(constellation, method, side_tol, ang_tol)
        percentage = "{:.0%}".format(matches / (matches + misses))
        print(matches, misses, percentage)

    def help_match(self):
        print("Attempts to match a specified constellation against a sample image")
        print("Invocation: match <sample_name> <constellation_name> {<method> {<tol> | {<side_tol> {ang_tol}}")
        print(" -sample_name: name of sample image from sample list")
        print(" -constellation_name: name of constellation image from constellation list")
        print(" -method (optional): triangle matching method to utilize (0: AAA, 1: , 2: SAS, 3: SSS), default: 0")
        print(" -side_tol (optional): tolerance to allow when matching sides of triangles, default: 0.1")
        print(" -ang_tol (optional): tolerance to allow when matching angles of triangles, default: 5.0")

    def do_match_aaa(self, inp):
        labels = inp.split()
        if len(labels) < 2:
            print("You need to specify at least two arguments: <sample_name> <constellation_name>", file=stderr)
            return
        samples, sample = self.list_samples(), None
        for s in samples:
            if s[0] == labels[0]:
                sample = s[1]
        if sample is None:
            print("Invalid sample name", file=stderr)
            return
        constellations, constellation = self.list_constellations(), None
        for c in constellations:
            if c[0] == labels[1]:
                constellation = c[1]
        if constellation is None:
            print("Invalid constellation name", file=stderr)
            return
        method, side_tol, ang_tol = 0, 0.1, 5.0
        if len(labels) > 2:
            ang_tol = float(labels[2])

        matches, misses = sample.match(constellation, method, side_tol, ang_tol)
        percentage = "{:.0%}".format(matches / (matches + misses))
        print(matches, misses, percentage)

    def help_match_aaa(self):
        print("Attempts to match a specified constellation against a sample image using AAA triangle similarity")
        print("Invocation: match <sample_name> <constellation_name> {<ang_tol>}")
        print(" -sample_name: name of sample image from sample list")
        print(" -constellation_name: name of constellation image from constellation list")
        print(" -ang_tol (optional): tolerance to allow when matching angles of triangles, default: 5.0")

    def do_match_sas(self, inp):
        labels = inp.split()
        if len(labels) < 2:
            print("You need to specify at least two arguments: <sample_name> <constellation_name>", file=stderr)
            return
        samples, sample = self.list_samples(), None
        for s in samples:
            if s[0] == labels[0]:
                sample = s[1]
        if sample is None:
            print("Invalid sample name", file=stderr)
            return
        constellations, constellation = self.list_constellations(), None
        for c in constellations:
            if c[0] == labels[1]:
                constellation = c[1]
        if constellation is None:
            print("Invalid constellation name", file=stderr)
            return
        method, side_tol, ang_tol = 1, 0.1, 5.0
        if len(labels) > 3:
            side_tol = float(labels[2])
            ang_tol = float(labels[3])
        elif len(labels) > 2:
            ang_tol = side_tol = float(labels[2])

        matches, misses = sample.match(constellation, method, side_tol, ang_tol)
        percentage = "{:.0%}".format(matches / (matches + misses))
        print(matches, misses, percentage)

    def help_match_sas(self):
        print("Attempts to match a specified constellation against a sample image using SAS triangle similarity")
        print("Invocation: match <sample_name> <constellation_name> {<side_tol> <ang_tol> | <tol>}")
        print(" -sample_name: name of sample image from sample list")
        print(" -constellation_name: name of constellation image from constellation list")
        print(" -side_tol (optional): tolerance to allow when matching sides of triangles, default: 0.1")
        print(" -ang_tol (optional): tolerance to allow when matching angles of triangles, default: 5.0")

    def do_match_sss(self, inp):
        labels = inp.split()
        if len(labels) < 2:
            print("You need to specify at least two arguments: <sample_name> <constellation_name>", file=stderr)
            return
        samples, sample = self.list_samples(), None
        for s in samples:
            if s[0] == labels[0]:
                sample = s[1]
        if sample is None:
            print("Invalid sample name", file=stderr)
            return
        constellations, constellation = self.list_constellations(), None
        for c in constellations:
            if c[0] == labels[1]:
                constellation = c[1]
        if constellation is None:
            print("Invalid constellation name", file=stderr)
            return
        method, side_tol, ang_tol = 2, 0.1, 5.0
        if len(labels) > 2:
            side_tol = float(labels[2])

        matches, misses = sample.match(constellation, method, side_tol, ang_tol)
        percentage = "{:.0%}".format(matches / (matches + misses))
        print(matches, misses, percentage)

    def help_match_sss(self):
        print("Attempts to match a specified constellation against a sample image using SSS triangle similarity")
        print("Invocation: match <sample_name> <constellation_name> {<ang_tol>}")
        print(" -sample_name: name of sample image from sample list")
        print(" -constellation_name: name of constellation image from constellation list")
        print(" -side_tol (optional): tolerance to allow when matching sides of triangles, default: 0.1")

    def do_plot_sample(self, inp):
        samples, sample = self.list_samples(), None
        for s in samples:
            if s[0] == inp:
                sample = s[1]
        if sample is None:
            print("Invalid sample name", file=stderr)
            return
        sample.plot()
        plt.show()

    def help_plot_sample(self):
        print("Plots related info regarding the specified sample")

    def do_plot_constellation(self, inp):
        constellations, constellation = self.list_constellations(), None
        for c in constellations:
            if c[0] == inp:
                constellation = c[1]
        if constellation is None:
            print("Invalid constellation name", file=stderr)
            return
        constellation.plot()

    def help_plot_constellation(self):
        print("Plots related info regarding the specified constellation")

    def do_quit(self, inp):
        exit(0)

    def help_quit(self):
        print("Exits the application")

    def do_exit(self, inp):
        exit(0)

    def help_exit(self):
        print("Exits the application")
