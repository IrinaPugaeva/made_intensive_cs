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

   def test_txt_reader(self):
        expected_data = \
            """Lover's Complaint by William Shakespeare
FROM off a hill whose concave womb reworded
"""

        self.assertEqual(expected_data, read_data(open('file.txt'), TXTReader))

    def test_json_writer(self):
        expected_data = {'1': 2, '3': 4, '5': 6}

        f = open('file.json', 'w')
        dump_data(expected_data, f, JSONWriter)
        f.close()

        self.assertEqual(expected_data, json.loads(open('file.json').read()))

    def test_json_reader(self):
        expected_data = {'1': 2, '3': 4, '5': 6}
        self.assertEqual(expected_data, read_data(open('file.json'), JSONReader))

    def test_csv_writer(self):
        expected_data = [['SN', 'Name', 'Contribution'],
                         ['Linus Torvalds', 'Linux Kernel'],
                         ['Tim Berners-Lee', 'World Wide Web'],
                         ['Guido van Rossum', 'Python Programming']]

        f = open('file.csv', 'w')
        dump_data(expected_data, f, CSVWriter)
        f.close()

        reader = csv.reader(open('file.csv'), delimiter=',')
        data = [row for row in reader]

        self.assertEqual(expected_data, data)

    def test_csv_reader(self):
        expected_data = [['SN', 'Name', 'Contribution'],
                         ['Linus Torvalds', 'Linux Kernel'],
                         ['Tim Berners-Lee', 'World Wide Web'],
                         ['Guido van Rossum', 'Python Programming']]
        self.assertEqual(expected_data, read_data(open('file.csv'), CSVReader))


 
