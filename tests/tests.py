import unittest
import requests


class search_one_Tests(unittest.TestCase):
    valid_search_input_data = None
    invalid_search_input_data = None

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://127.0.0.1:8000/busqueda/"
        cls.valid_search_input_data = "2959c9d3-bb20-4799-9acc-508f4d05bbe4"
        cls.invalid_search_input_data = "2959c9d3-bb20-4799-9acc-508f4d05bbe4-"

    @classmethod
    def tearDownClass(cls):
        del cls.valid_search_input_data
        del cls.invalid_search_input_data

    def test_search_one(self):
        response = requests.get(self.base_url + self.valid_search_input_data)
        self.assertEqual("200", str(response.status_code))

    def test_search_one_invalid(self):
        response = requests.get(self.base_url + self.invalid_search_input_data)
        self.assertEqual("400", str(response.status_code))


class contacto_estado_Tests(unittest.TestCase):
    valid_tallerista_input_data = None
    invalid_tallerista_input_data = None

    @classmethod
    def setUpClass(cls):
        cls.base_url = "http://127.0.0.1:8000/tallerista/"

        cls.valid_tallerista_input_data = "4556cc01-2555-4664-be19-b899d9750be1/Contactado y validado"

        cls.invalid_tallerista_input_data = "4556cc01-2555-4664-be19-b899d975/Contactado y validado"

    @classmethod
    def tearDownClass(cls):
        del cls.valid_tallerista_input_data
        del cls.invalid_tallerista_input_data

    def test_put(self):
        response = requests.put(self.base_url + self.valid_tallerista_input_data)
        self.assertEqual("200", str(response.status_code))


    def test_put_invalid(self):
        response = requests.put(self.base_url + self.invalid_tallerista_input_data)
        self.assertEqual("400", str(response.status_code))


if __name__ == '__main__':
    unittest.main()