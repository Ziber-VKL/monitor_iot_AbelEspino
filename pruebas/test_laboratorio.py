import unittest
from unittest.mock import patch
import config
from eventos import conexion
from alertas import cola

class PruebasConexion(unittest.TestCase):
    def setUp(self):
        conexion.reiniciar()
        cola.limpiar()

    def test_desconexion_y_recuperacion(self):
        self.assertEqual(conexion.detectar(ahora=10.0, conectado=True), [])
        eventos = conexion.detectar(ahora=20.0, conectado=False)
        self.assertEqual(eventos[0][0], "red_desconectada")
        eventos = conexion.detectar(ahora=25.0, conectado=True)
        self.assertEqual(eventos[0][0], "red_conectada")
        self.assertEqual(eventos[0][1]["segundos"], 5.0)

    def test_recordatorio_desconexion(self):
        conexion.detectar(ahora=10.0, conectado=True)
        conexion.detectar(ahora=20.0, conectado=False)
        eventos = conexion.detectar(
            ahora=20.0 + config.RECORDATORIO_RED, conectado=False
        )
        self.assertEqual(eventos[0][0], "red_sigue_desconectada")

class PruebasCola(unittest.TestCase):
    def setUp(self):
        cola.limpiar()

    def test_solo_encola_eventos_con_sonido(self):
        self.assertTrue(cola.encolar("cpu_alta"))
        self.assertFalse(cola.encolar("reporte"))
        self.assertEqual(cola.pendientes(), 1)
        self.assertEqual(cola.siguiente(), "cpu_alta")

if __name__ == "__main__":
    unittest.main()
