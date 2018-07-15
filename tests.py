import unittest

import steam_groups


class TestSteamGroupsMethods(unittest.TestCase):

    def test_main(self):
        self.assertTrue(steam_groups.main())


if __name__ == '__main__':
    unittest.main()
