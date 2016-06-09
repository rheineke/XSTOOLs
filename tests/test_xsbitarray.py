import unittest

from xstools.xsbitarray import XsBitArray


class TestXSBitArray(unittest.TestCase):
    def test_head(self):
        arr = XsBitArray('0b01')
        self.assertEqual(arr.head(), XsBitArray('0b1'))
        self.assertNotEqual(arr.head(), XsBitArray('0b0'))

    def test_to_usb(self):
        a_arr = XsBitArray('0b00010')
        b_arr = XsBitArray('0b1111001')
        c_arr = a_arr + b_arr
        self.assertEqual(c_arr, XsBitArray('0xf22'))
        self.assertEqual(c_arr.to_usb(), b'"\x0f')