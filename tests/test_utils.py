import io
import unittest

from penne_shell import utils


class ChecksumFileTests(unittest.TestCase):
    def setUp(self):
        self.octets = b'abcd'
        self.sample_file = io.BytesIO(self.octets)

    def test_default_sum_fmt_is_hex_md5(self):
        import hashlib
        algo = hashlib.md5()
        algo.update(self.octets)
        self.assertEqual(
            algo.hexdigest(),
            utils.checksum_file(self.sample_file)
        )

    def test_byte_offset_is_changed(self):
        former_offset = self.sample_file.tell()
        _ = utils.checksum_file(self.sample_file)
        self.assertNotEqual(former_offset, self.sample_file.tell())


class SafeChecksumFileTests(unittest.TestCase):
    def setUp(self):
        self.octets = b'abcd'
        self.sample_file = io.BytesIO(self.octets)

    def test_default_sum_fmt_is_hex_md5(self):
        import hashlib
        algo = hashlib.md5()
        algo.update(self.octets)
        self.assertEqual(
            algo.hexdigest(),
            utils.safe_checksum_file(self.sample_file)
        )

    def test_byte_offset_is_preserved(self):
        former_offset = self.sample_file.tell()
        _ = utils.safe_checksum_file(self.sample_file)
        self.assertEqual(former_offset, self.sample_file.tell())

