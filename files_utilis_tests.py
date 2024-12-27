import os
import unittest
from files_utils import read_json, write_json, append_json, read_csv, write_csv, append_csv, read_txt, write_txt, append_txt, read_yaml
import yaml 


class TestFileUtils(unittest.TestCase):

    def setUp(self):
        # Создадим тестовые файлы перед каждым тестом
        self.test_json = 'test.json'
        self.test_csv = 'test.csv'
        self.test_txt = 'test.txt'
        self.test_yaml = 'test.yaml'

    def tearDown(self):
        # Удалим тестовые файлы после каждого теста
        for file in [self.test_json, self.test_csv, self.test_txt, self.test_yaml]:
            if os.path.exists(file):
                os.remove(file)

    def test_write_read_json(self):
        data = {"name": "Alice", "age": 30}
        write_json(data, self.test_json)
        result = read_json(self.test_json)
        self.assertEqual(data, result)

    def test_append_json(self):
        data = [{"name": "Bob", "age": 25}]
        write_json([{"name": "Alice", "age": 30}], self.test_json)
        append_json(data, self.test_json)
        result = read_json(self.test_json)
        self.assertEqual(len(result), 2)

    def test_write_read_csv(self):
        data = [["Name", "Age"], ["Alice", 30], ["Bob", 25]]
        write_csv(data, self.test_csv)
        result = read_csv(self.test_csv)
        self.assertEqual(data, result)

    def test_append_csv(self):
        data = [["Charlie", 35]]
        write_csv([["Name", "Age"], ["Alice", 30]], self.test_csv)
        append_csv(data, self.test_csv)
        result = read_csv(self.test_csv)
        self.assertEqual(len(result), 3)

    def test_write_read_txt(self):
        data = "Hello, World!"
        write_txt(data, self.test_txt)
        result = read_txt(self.test_txt)
        self.assertEqual(data, result)

    def test_append_txt(self):
        data = "New Line\n"
        write_txt("Hello, World!\n", self.test_txt)
        append_txt(data, self.test_txt)
        result = read_txt(self.test_txt)
        self.assertEqual("Hello, World!\nNew Line\n", result)

    def test_write_read_yaml(self):
        data = {"name": "Alice", "age": 30}
        with open(self.test_yaml, 'w') as file:
            yaml.dump(data, file)
        result = read_yaml(self.test_yaml)
        self.assertEqual(data, result)


if __name__ == '__main__':
    unittest.main()