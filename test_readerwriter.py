import unittest
import json
import csv
from readerwriter import TXTReader, TXTWriter, CSVReader, CSVWriter, \
    JSONReader, JSONWriter, read_data, dump_data


class Test(unittest.TestCase):

    def test_txt_writer(self):
        expected_data = \
            """Lover's Complaint by William Shakespeare
FROM off a hill whose concave womb reworded
"""

        f = open('file.txt', 'w')
        dump_data(expected_data, f, TXTWriter)
        f.close()

        self.assertEqual(expected_data, open('file.txt').read())

 
