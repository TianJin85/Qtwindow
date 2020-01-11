from functools import reduce
import multiprocessing as mp

def power(x):
    return pow(x, 2)

if __name__ == '__main__':
    with mp.Pool(processes=4) as mpp:
        print(reduce(lambda a,b:a+b, mpp.map(power, range(1000000)), 0))
