from multiprocessing import Pool

def worker(args):
    start, end = args

    return sum(range(start, end + 1))


def calculator_usepool():
    ranges = [(i * 100 + 1, (i+1) * 100) for i in range(10)]
    with Pool(10) as pool:
        results = pool.map(worker, ranges)

    return sum(results)


if __name__== "__main__":
    calculator_usepool()