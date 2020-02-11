from argparse import ArgumentParser

import smu

def linspace(initial, final, n = 100):
    if n >= 2:
        increment = (float(final) - float(initial)) / (n - 1)
        return [float(initial) + i * increment for i in range(n)]
    else:
        return []


parser = ArgumentParser(description="Output file")
parser.add_argument("-i", dest="filename", required=True,
                    help="input file with two matrices", metavar="FILE",
                    type=str)                

# if __name__ == "__main__":
args = parser.parse_args()




s = smu.smu()
vin = linspace(-5, 5, 101)
f = open(args.filename, 'w')
f.write('"Vin","Vout"\n')

s.set_current(2, 0.)
for v in vin:
    s.set_voltage(1, v)
    s.autorange(1)
    s.autorange(2)
    f.write('{!s},{!s}\n'.format(v, s.get_voltage(2)))

s.set_voltage(1, 0.)
s.set_voltage(2, 0.)
f.close()
