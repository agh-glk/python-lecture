import multiprocessing
import threading
import time


def f(max_count):
    a = 0
    b = 1
    count = 1
    if max_count == 0:
        return a
    while count < max_count:
        count += 1
        a, b = b, b + a
    return b


def timeit(method):
    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te - ts)
        return result

    return timed


@timeit
def thr():
    thread_pool = []
    for i in range(100000, 700000, 100000):
        thread_pool.append(threading.Thread(target=f, args=(i,)))
        thread_pool[-1].start()
    print "Ready?: ", [x.is_alive() for x in thread_pool]
    while not all([not x.is_alive() for x in thread_pool]):
        print [not x.is_alive() for x in thread_pool]
        time.sleep(1)
    print [not x.is_alive() for x in thread_pool]
    for x in thread_pool:
        x.join()


@timeit
def multi():
    pool = multiprocessing.Pool(6)
    results = []
    for i in range(100000, 700000, 100000):
        results.append(pool.apply_async(f, (i,)))
    print "Ready?: ", [x.ready() for x in results]
    while not all([x.ready() for x in results]):
        print [x.ready() for x in results]
        time.sleep(1)
    print [x.ready() for x in results]


if __name__ == '__main__':
    print "Threading:"
    thr()
    print "Multiprocessing"
    multi()
