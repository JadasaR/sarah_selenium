from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time


class TestEntrarCorreo(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.gmail.com/')

#    def  test_prueba_titulo_gmail(self):
#        self.assertEqual('Gmail', self.driver.title)

#   def test_prueba_entrar_a_mi_gmail(self):
#        buscar = self.driver.find_element_by_id('gmail-sign-in')
#        buscar.click()

    def test_prueba_encontrar_correo(self):
        time.sleep(10)
        correo = self.driver.find_element_by_id('Email')
        correo.send_keys("jadasar4@gmail.com")
        btnNext = self.driver.find_element_by_id('next')
        btnNext.click()
        time.sleep(5)
        passw = self.driver.find_element_by_id('Passwd')
        passw.send_keys("hola")
        btnContra = self.driver.find_element_by_id('signIn')
        btnContra.click()
        time.sleep(20)
        btnMsg = self.driver.find_element_by_id(':3d')
        btnMsg.click()

#    def test_prueba_ingresar_contrasenha(self):
#        passw = self.driver.find_element_by_id('Psswd')
#        passw.send_keys("teamocristo")
#        btnContra = self.driver.find_element_by_id('signIn')
#        btnContra.click()

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()