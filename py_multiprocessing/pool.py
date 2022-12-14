from multiprocessing import Pool


def process(i):
    return i*i


if __name__ == '__main__':
    with Pool(4) as worker:
        result = worker.map(process, [1,2,3,4])
        print(result)
