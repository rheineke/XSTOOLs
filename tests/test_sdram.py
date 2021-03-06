import unittest
from intelhex import IntelHex

from xstools.xsboard import XsBoard
from xstools.xsusb import XsUsb


class Sdramtest(unittest.TestCase):
    def setUp(self):
        self.board = XsBoard.get_xsboard()

    @unittest.skipUnless(XsUsb.get_xsusb_ports(), 'No Xula board found')
    def test_readwrite(self):
        """
        test read and write sdram

        writes 14 values to sdram, hereafter reads 14 values
        from sdram and checks equality
        """
        for v in [0, 255]:
            keys = range(0, 14)
            values = 14 * [v]
            data = IntelHex()
            data.fromdict(dict(zip(keys, values)))
            self.board.write_sdram(data, 0, len(keys)-1)
            result = self.board.read_sdram(0, len(keys)-1)
            self.assertEqual(data.todict(), result.todict())
