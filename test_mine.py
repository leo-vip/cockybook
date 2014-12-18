from filesystem import QiniuFileSystem
import unittest
__author__ = 'lei'

fs=QiniuFileSystem()
class MineTest(unittest.TestCase):

    def test_list(self):
        info = fs.listdir(u'Noval')
        for inf in info:

            print(inf)

    def test_stat(self):
        fs.exists(u'Noval')

if __name__ == "__main__":
    unittest.main()
