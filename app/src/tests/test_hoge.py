#!/usr/bin/python
# -*- coding: utf-8 -*-

# [Import start]
from server.hoge import hoge_api as hoge
import unittest

import pytest
# [Import end]

@pytest.mark.hoge
class TestTagAprioriMain(unittest.TestCase):

    def setUp(self):
        print('start')

    def tearDown(self):
        print('finished')

    def test_success(self):
        res = hoge.hoge()
        self.assertEqual(res, "hogehoge")

    def this_is_ignored(self):
        res = hoge.hoge()
        self.assertEqual(res, "hoge")

if __name__ == '__main__':
    unittest.main()
