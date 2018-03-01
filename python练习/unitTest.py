#!/usr/bin/env python3
#_*_ encoding:utf-8 _*_
import unittest
from unitTest_DictClass import Dict
class TestDict(unittest.TestCase):
    def test_init(self):
        d = Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key,'value')
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertEqual(d['key'],'value')
        self.assertTrue('key' in d)

    def test_keterror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
    def setUp(self):
        print('wocao\n')
    def tearDown(self):
        print('shizhende')
if __name__ == '__main__':
    unittest.main()
