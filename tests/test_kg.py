#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Path hack
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

try:
    import unittest2 as unittest
except ImportError:
    import unittest

from kgtool.core import *  # noqa
from kgtool.kg import *  # noqa


class CoreTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def test_statJsonld(self):
        tin = "test_kg_stat.jsonld"
        tout = file2abspath(tin, __file__)
        with open(tout) as f:
            data = json.load(f)
            ret = stat_jsonld(data)
            print json.dumps(ret)
            assert ret["triple"] == 29
            assert ret[u"tag_抒情"] == 1

    def test_stat_jsonld(self):
        tin = "test_kg_stat.jsonld"
        tout = file2abspath(tin, __file__)
        with open(tout) as f:
            data = json.load(f)
            ret = stat_jsonld(data)
            print json.dumps(ret)
            assert ret["triple"] == 29
            assert ret[u"tag_抒情"] == 1

    def test_stat_items(self):
        tin = "test_kg_stat.jsonld"
        tout = file2abspath(tin, __file__)
        with open(tout) as f:
            data = json.load(f)
            data = [data]
            ret = stat_items(data)
            print json4debug(ret)
            #raise("aa")

    def test_stat_kg_pattern(self):
        tin = "test_kg_stat.jsonld"
        tout = file2abspath(tin, __file__)
        with open(tout) as f:
            data = json.load(f)
            ret = stat_kg_pattern(data)
            print json4debug(ret)
            #raise("aa")


if __name__ == '__main__':
    unittest.main()
