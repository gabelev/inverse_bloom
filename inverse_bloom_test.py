# import hashlib
import unittest
from inverse_bloom import InverseBloomFilter


class TestInverseBloom(unittest.TestCase):

    def test_this(self):
        filter = InverseBloomFilter()
        self.assertTrue(filter)
