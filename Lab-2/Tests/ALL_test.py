import unittest
import toml
import yaml
import json
from objects import *
from lib.Serializers.Factory.SerializerFactory import factory
import lib.files_paths as path
from func import f
from myclass import mycls


class TestJsonCase(unittest.TestCase):
    def setUp(self) -> None:
        self.serializer = factory("JSON")

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
        self.serializer.dump(a, path.JSON_PATH)
        self.assertEqual(self.serializer.load(path.JSON_PATH), json.load(open(path.JSON_PATH)))

    def test_dict_from_file(self):
        self.serializer.dump(my_obj, path.JSON_PATH)
        self.assertEqual(self.serializer.load(path.JSON_PATH), json.load(open(path.JSON_PATH)))

class TOMLTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.serializer = factory("TOML")

    def test_dumps_dict(self):
        self.assertEqual(self.serializer.dumps(dct), toml.dumps(dct))

    def test_dumps_list(self):
        ser_my_lst = self.serializer.dumps(lst)
        self.assertEqual(self.serializer.loads(ser_my_lst), lst)

    def test_dump_list(self):
        self.serializer.dump(lst, path.TOML_PATH)
        self.assertEqual(self.serializer.load(path.TOML_PATH), lst)

    def test_dumps_func(self):
        self.assertEqual(self.serializer.loads(self.serializer.dumps(f))(), f())

    def test_dump_func(self):
        self.serializer.dump(f, path.TOML_PATH)
        self.assertEqual(self.serializer.load(path.TOML_PATH)(), f())

    def test_dumps_class(self):
        ser_class = self.serializer.dumps(mycls)
        self.assertEqual(self.serializer.loads(ser_class).pupa_lupa(), mycls.pupa_lupa())

    def test_loads_dict(self):
        self.assertEqual(self.serializer.loads(self.serializer.dumps(dct)), dct)

class YAMLTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.serializer = factory("YAML")

    def test_dump_dict(self):
        self.serializer.dump(my_obj, path.YAML_PATH)
        with open(path.YAML_PATH,'r') as file:
            string = file.read()
        self.assertEqual(string, yaml.safe_dump(my_obj))

    def test_dumps_list(self):
        self.assertEqual(self.serializer.dumps(a), yaml.safe_dump(a))

    def test_dump_func(self):
        self.serializer.dump(f, path.YAML_PATH)
        func = self.serializer.load(path.YAML_PATH)
        self.assertEqual(func(), f())

    def test_dump_class(self):
        self.serializer.dump(mycls, path.YAML_PATH)
        cls = self.serializer.load(path.YAML_PATH)
        self.assertEqual(cls.name, mycls.name)

    def test_loads_dict(self):
        dct = self.serializer.dumps(new_dict)
        self.assertEqual(self.serializer.loads(dct), new_dict)

