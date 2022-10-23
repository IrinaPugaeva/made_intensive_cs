import unittest
from read_large_file import read_large_file

class Test(unittest.TestCase):

    def test_read_large_file(self):
        expected_data = [
            'My spirits to attend this double voice accorded,\n',
            'And down I laid to list the sad-tuned tale;\n',
            "Storming her world with sorrow's wind and rain.\n",
            'Which fortified her visage from the sun,\n',
            'Whereon the thought might think sometime it saw\n',
            'The carcass of beauty spent and done:\n',
            'Oft did she heave her napkin to her eyne,\n',
            'Laundering the silken figures in the brine\n',
            'And often reading what contents it bears;\n',
            'In clamours of all size, both high and low.\n',
            'As they did battery to the spheres intend;\n',
            'To the orbed earth; sometimes they do extend\n',
            "To every place at once, and, nowhere fix'd,\n",
            "The mind and sight distractedly commix'd.\n",
            'Hanging her pale and pined cheek beside;\n',
            'And true to bondage would not break from thence,\n',
            ]

        gen_file = read_large_file(open('Shakespeare_min.txt'), ['and',
                                   'the', 'to'])

        self.assertEqual(expected_data, list(iter(gen_file)))
