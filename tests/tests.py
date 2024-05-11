import unittest
import requests
import json

#ENDPOINT ASOCIADO A LA FUNCIÓN LEER_BUSQUEDA
class leer_busqueda_tests(unittest.TestCase):
    valid_busqueda_input_data = None
    invalid_busqueda_input_data = None

    @classmethod
    def setUpClass(cls):
        #URL BASE
        cls.base_url = "http://127.0.0.1:8000/busqueda/"
        #ENTRADA VÁLIDA: id de un objeto de la clase Busqueda existente en la base de datos
        cls.valid_busqueda_input_data = "05f8d7fc-bfd3-4216-929f-954147154ab0"
        #ENTRADA INVÁLIDA: id de un objeto de la clase Busqueda no existente en la base de datos
        cls.invalid_busqueda_input_data = "."

    @classmethod
    def tearDownClass(cls):
        del cls.valid_busqueda_input_data
        del cls.invalid_busqueda_input_data

    #CASO DE PRUEBA 1: ENTRADA VÁLIDA
    #Al realizar la petición con un id de un objeto de la clase Busqueda existente en la base de datos, se debería retornar el objeto de la clase Busqueda asociado a dicho id
    #En el caso de prueba, se busca afirmar que el resultado de la petición mencionada sea igual al objeto de la clase Busqueda asociado al id ingresado como entrada válida
    def test_leer_busqueda_valido(self):
        response = requests.get(self.base_url + self.valid_busqueda_input_data).json()
        response_valid_input_data = {"prompt": "Quiero hacer una clase de surf",
                                     "id": "05f8d7fc-bfd3-4216-929f-954147154ab0",
                                     "resultados_talleristas": [{"nombre": "Jaime",
                                                                 "precio": 12000,
                                                                 "valoracion": 5,
                                                                 "valoracion_cantidad": 4,
                                                                 "contacto_estado": "Sin contactar",
                                                                 "contacto": "https://www.superprof.cl/profesor-educacion-fisica-salud-entrenamiento-deportivo-realiza-clases-preparacion-fisica-para-tus-deportes.html",
                                                                 "fuente": "SuperProf.cl",
                                                                 "id": "f1e16e87-3ff3-4c6a-abc1-cf045bffc4a3",
                                                                 "id_busqueda": "05f8d7fc-bfd3-4216-929f-954147154ab0"}]}
        self.assertEqual(response_valid_input_data, response)

    #CASO DE PRUEBA 2: ENTRADA INVÁLIDA
    #Al realizar la petición con un id de un objeto de la clase Busqueda no existente en la base de datos, se debería retornar el código de estado 400
    #En el caso de prueba, se busca afirmar que el resultado de la petición mencionada tenga código de estado 400
    def test_leer_busqueda_invalido(self):
        response = requests.get(self.base_url + self.invalid_busqueda_input_data)
        self.assertEqual(400, response.status_code)

#ENDPOINT ASOCIADO A LA FUNCIÓN CREAR_PROPUESTA
class crear_propuesta_tests(unittest.TestCase):
    valid_propuesta_input_data = None
    invalid_propuesta_input_data = None

    @classmethod
    def setUpClass(cls):
        #URL BASE
        cls.base_url = "http://127.0.0.1:8000/propuesta"
        #ENTRADA VÁLIDA: objeto de la clase Propuesta, donde el atríbuto id_tallerista es el id de un objeto de la clase Tallerista existente en la base de datos
        cls.valid_propuesta_input_data = {"descripcion": "",
                                          "modalidad": "Presencial",
                                          "numero_vacantes": 1,
                                          "numero_sesiones": 1,
                                          "id_tallerista": "f1e16e87-3ff3-4c6a-abc1-cf045bffc4a3"}
        #ENTRADA VÁLIDA: objeto de la clase Propuesta, donde el atríbuto id_tallerista es el id de un objeto de la clase Tallerista no existente en la base de datos
        cls.invalid_propuesta_input_data = {"descripcion": "",
                                            "modalidad": "Presencial",
                                            "numero_vacantes": 1,
                                            "numero_sesiones": 1,
                                            "id_tallerista": "."}
    @classmethod
    def tearDownClass(cls):
        del cls.valid_propuesta_input_data
        del cls.invalid_propuesta_input_data

    #CASO DE PRUEBA 3: ENTRADA VÁLIDA
    #Al realizar la petición con un objeto de la clase Propuesta cuyo id_tallerista tenga como valor el id de un objeto de la clase Tallerista existente en la base de datos, se debería retornar el objeto de la clase Propuesta creado en la base de datos (y código de estado 200)
    #En el caso de prueba, se busca afirmar que el resultado de la petición mencionada tenga código de estado 200
    #Nótese que al crear una propuesta esta se crea con id aleatorio, por lo que no se puede saber previamente su valor para buscar afirmar que sea igual al resultado de la petición (como en el caso de prueba 1)
    def test_crear_propuesta_valido(self):
        response = requests.post(self.base_url, data = json.dumps(self.valid_propuesta_input_data))
        self.assertEqual(200, response.status_code)

    #CASO DE PRUEBA 4: ENTRADA INVÁLIDA
    #Al realizar la petición con un objeto de la clase Propuesta cuyo id_tallerista tenga como valor el id de un objeto de la clase Tallerista no existente en la base de datos, se debería retornar el código de estado 400
    #En el caso de prueba, se busca afirmar que el resultado de la petición mencionada tenga código de estado 200
    def test_crear_propuesta_invalido(self):
        response = requests.post(self.base_url, data = json.dumps(self.invalid_propuesta_input_data))
        self.assertEqual(400, response.status_code)

if __name__ == '__main__':
    unittest.main()