import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class TestModak(unittest.TestCase):

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(
            executable_path=r'../chromeDriver/chromedriver.exe')
        cls.driver.implicitly_wait(10)
        cls.driver.get("http://www.aliexpress.com/")
        cls.driver.maximize_window()

    def test_find_item(self):
        assert self.driver.title == "AliExpress - Compra online de Electrónica, Moda, Casa y jardín, Deportes y ocio, Motor y seguridad, y más. - AliExpress - AliExpress", "NO SE INGRESÓ CORRECTAMENTE A LA WEB"
        self.driver.find_element(By.ID, "search-words").clear()
        self.driver.find_element(By.ID, "search-words").send_keys("instax mini")
        assert self.driver.find_element(By.ID, "search-words").get_attribute(
            "value") == "instax mini", "ERROR EN EL INPUT USUARIO"
        self.driver.find_element(By.ID, "search-words").send_keys(Keys.RETURN)

        botonPaginado = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[1]/div/div[2]/div[3]/ul/li[3]")
        self.assertTrue(botonPaginado.is_displayed() and botonPaginado.is_enabled())
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        botonPaginado.click()

        time.sleep(3)

        assert self.driver.title == "instax mini – Compra instax mini con envío gratis en AliExpress version"

        listado = self.driver.find_elements(By.XPATH,
                                            "//*[@id='card-list']/div")
        print("\nla cantidad de items dentro del listado es: ", len(listado))

        assert len(listado), "NO HAY ÍTEMS EN EL LISTADO"

        self.driver.find_element(By.XPATH,
                                  "//*[@id='card-list']/div[2]").click()

        self.driver.switch_to.window(self.driver.window_handles[1])

        #assert self.driver.title == "instax mini – Compra instax mini con envío gratis en AliExpress version"

        item = self.driver.find_element(By.CLASS_NAME, "comet-v2-input-number-input")
        self.assertTrue(item.is_displayed() and item.is_enabled())
        print("\nCantidad de items en stock:", item.get_attribute("value"))
        assert int(item.get_attribute("value")), "NO HAY STOCK"