import unittest
from .objects import *
from lib.Serializers.JSONSerializer import JSONSerializer
from func import f
from myclass import mycls


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.serializer = JSONSerializer()

    def test_to_float(self):
        self.assertEqual(self.serializer.dumps(prim_6), json.dumps(prim_6), 'Wrong output on float')

    def test_to_int(self):
        self.assertEqual(self.serializer.dumps(prim_1), json.dumps(prim_1), 'Wrong output on int')

    def test_to_bool_true(self):
        self.assertEqual(self.serializer.dumps(prim_2), json.dumps(prim_2), 'Wrong output on bool_True')

    def test_to_bool_false(self):
        self.assertEqual(self.serializer.dumps(prim_3), json.dumps(prim_3), 'Wrong output on bool_False')

    def test_to_none(self):
        self.assertEqual(self.serializer.dumps(prim_4), json.dumps(prim_4), 'Wrong output on None')

    def test_to_str(self):
        self.assertEqual(self.serializer.dumps(prim_5), json.dumps(prim_5), 'Wrong output on str')

    def test_int_from_json(self):
        self.assertEqual(self.serializer.loads(json.dumps(prim_1)), json.loads(json.dumps(prim_1)))

    def test_float_from_json(self):
        self.assertEqual(self.serializer.loads(json.dumps(prim_6)), json.loads(json.dumps(prim_6)))

    def test_True_from_json(self):
        self.assertEqual(self.serializer.loads(json.dumps(prim_2)), json.loads(json.dumps(prim_2)))

    def test_False_from_json(self):
        self.assertEqual(self.serializer.loads(json.dumps(prim_3)), json.loads(json.dumps(prim_3)))

    def test_None_from_json(self):
        self.assertEqual(self.serializer.loads(json.dumps(prim_4)), json.loads(json.dumps(prim_4)))

    def test_str_from_json(self):
        self.assertEqual(self.serializer.loads(json.dumps(prim_5)), json.loads(json.dumps(prim_5)))

    def test_func_from_json(self):
        deser = self.serializer.loads(self.serializer.dumps(f))
        self.assertEqual(deser(55, 48), f(55, 48), "error in func")
        self.assertEqual(deser(228, 1337), f(228, 1337), "error in func")

    def test_class_from_json(self):
        deser = self.serializer.loads(self.serializer.dumps(mycls))
        self.assertEqual(deser.pupa_lupa(15, 23), mycls.pupa_lupa(15, 23))

    def test_hard_list(self):
        self.assertEqual(self.serializer.dumps(a), json.dumps(a))

    def test_hard_dict(self):
        self.assertEqual(self.serializer.dumps(my_obj), json.dumps(my_obj))

    def test_hard_from_file(self):
        self.serializer.dump(a, "../Files/JSONSerialize")
        self.assertEqual(self.serializer.load("../Files/JSONSerialize"), json.load(open("../Files/JSONSerialize")))

    def test_dict_from_file(self):
        self.serializer.dump(my_obj, "../Files/JSONSerialize")
        self.assertEqual(self.serializer.load("../Files/JSONSerialize"), json.load(open("../Files/JSONSerialize")))
