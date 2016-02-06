# import hashlib
# from multiprocessing import pool

# Inverse Bloom Filter is a concurrent "inverse" Bloom filter
# as outlined by Jeff Hodges (link). It may report a false negative
# but will never report a false positive.


class InverseBloomFilter(object):

    def __init__(self):
        self.array = bytearray()
        self.hash_pool = []
        self.capacity = 0
