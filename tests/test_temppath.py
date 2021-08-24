# vim: expandtab tabstop=4 shiftwidth=4

import unittest

import temppath

class TemporaryPathTests(unittest.TestCase):
    def test_manual(self):
        path = temppath.TemporaryPath()
        self.assertTrue(path.is_file())

        path.unlink()
        self.assertFalse(path.exists())

    def test_write_read(self):
        path = temppath.TemporaryPath()
        path.write_text('lorem ipsum doler sit amet')
        self.assertTrue(path.exists())
        self.assertEqual(path.read_text(), 'lorem ipsum doler sit amet')
        path.unlink()

    def test_context_manager(self):
        with temppath.TemporaryPath() as path:
            path.write_text('lorem ipsum doler sit amet')
            self.assertTrue(path.exists())
            self.assertEqual(path.read_text(), 'lorem ipsum doler sit amet')

        self.assertFalse(path.exists())
