import unittest

import steam_groups


class TestSteamGroupsMethods(unittest.TestCase):
    def test_download_user_library(self):
        steam_id = 76561198028705366
        _, query_count = steam_groups.download_user_library(steam_id)

        assert query_count == 1


if __name__ == '__main__':
    unittest.main()
