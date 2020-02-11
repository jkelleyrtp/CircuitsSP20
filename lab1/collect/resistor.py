# import argparse
from argparse import ArgumentParser
import os.path
from lib import smu as smu



def linspace(initial, final, n = 100):
    if n >= 2:
        increment = (float(final) - float(initial)) / (n - 1)
        return [float(initial) + i * increment for i in range(n)]
    else:
        return []



# parser = argparse.ArgumentParser(description='write to specific file')
# parser.add_argument('filepath', metavar='N', type=str, nargs='+',
                #    help='an integer for the accumulator')
# def is_valid_file(parser, arg):
#     if not os.path.exists(arg):
#         parser.error("The file %s does not exist!" % arg)
#     else:
#         return open(arg, 'r')  # return an open file handle

parser = ArgumentParser(description="Output file")
parser.add_argument("-i", dest="filename", required=True,
                    help="input file with two matrices", metavar="FILE",
                    type=str)                

# if __name__ == "__main__":
args = parser.parse_args()

s = smu.smu()
v = linspace(-5, 5, 101)
f = open(args.filename, 'w')
f.write('"V","I"\n')

for val in v:
    s.set_voltage(1, val)
    s.autorange(1)
    f.write('{!s},{!s}\n'.format(val, s.get_current(1)))

s.set_voltage(1, 0.)
f.close()
