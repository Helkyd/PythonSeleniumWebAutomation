
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

import asyncio

'''
class ChromeSearch(unittest.TestCase):


    def setUp(self):
        #self.driver = webdriver.Chrome('./chromedriver')

        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', True)
        #opt.w3c = True        
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',options=opt)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://www.python.org")
        self.assertIn("Python", driver.title)

        elem = driver.find_element(By.NAME,"q")
        
        elem.send_keys("getting started with python")

        elem.send_keys(Keys.RETURN)
        
        assert "https://www.python.org/search/?q=getting+started+with+python&submit=" == driver.current_url

    def tearDown(self):
        self.driver.close()


    if __name__ == "__main__":
        unittest.main()
'''



class AgtNifCheck():

    def agtnif_setup(self):
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option('w3c', True)
        #opt.w3c = True        
        self.driver = webdriver.Chrome(executable_path='/usr/bin/chromedriver',options=opt)
        self.driver.delete_all_cookies()

    async def pagina_agtnif(self):
        nif = "9999999999"
        driver = self.driver
        driver.get("https://agt.minfin.gov.ao/PortalAGT/#!/servicos/consultar-nif/" + (self.nifverificar or nif))
        
        
        janela = driver.window_handles[0]
        driver.switch_to.window(janela)

        #elem = driver.find_element(By.NAME,"nif")
        fframe = driver.find_element(By.TAG_NAME,"iframe")
        driver.switch_to.frame(fframe)
        driver.implicitly_wait(30)

        driver.find_element(By.ID,"recaptcha-anchor").click()
        print ('Fez Clique no Iframe')
        driver.implicitly_wait(30)

        driver.switch_to.window(janela)
        #WebDriverWait(driver,50).until(EC.visibility_of_element_located((By.XPATH,"//*[contains(text(),'CONSULTAR')]")))
        #WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'CONSULTAR')]"))).click()
        elemento = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'CONSULTAR')]")))
        elemento.click()

        #driver.find_element(By.CLASS_NAME,'card-action text-right')
        #element = WebDriverWait(driver,50).until(EC.visibility_of_element_located((By.CLASS_NAME,'card-action text-right')))

        #elem = driver.find_element(By.XPATH,"//*[contains(text(),'CONSULTAR')]")
        #print (elem)
        #element = WebDriverWait(driver,50).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'CONSULTAR')]"))) # By.XPATH,"CONSULTAR")))
        #tt = driver.find_element(By.XPATH,"//*[contains(text(),'CONSULTAR')]")
        #tt = driver.find_element(By.XPATH,"//button[text()='CONSULTAR']")
        #tt.click()
        
        #if driver.find_element(By.CLASS_NAME,'imprimirDli'):
        #    print ('found Dli')
        
        #driver.find_element(By.CLASS_NAME,'imprimirDli')
        #element = driver.find_elements(By.CLASS_NAME,'collection-item')
        #WebDriverWait(driver,50).until(EC.visibility_of_all_elements_located((By.CLASS_NAME,"collection-item")))
        print ('FIM')
        janela1 = driver.window_handles[0]
        driver.switch_to.window(janela1)


        driver.find_elements(By.CLASS_NAME,'colletion-item__title ng-binding')
        #driver.find_elements(By.CLASS_NAME,'collection-item')
        #driver.implicitly_wait(30)

        
        for ee in driver.find_elements(By.CLASS_NAME,'collection-item'):
            print (ee.text)
            if 'NIF' in ee.text:
                print (ee.text)
            elif 'Nome' in ee.text:
                print (ee.text)
            elif 'Regime' in ee.text:
                print (ee.text)
        
        #driver.find_element(By.XPATH,"//input[@type='submit' and @value='CONSULTAR']")

        #print (tt)

        #element = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//*[contains(text(),'CONSULTAR')]"))) # By.XPATH,"CONSULTAR")))
        #element.click()

        #driver.implicitly_wait(30)

        #elem.send_keys("getting started with python")

        #elem.send_keys(Keys.RETURN)
        
        #assert "https://www.python.org/search/?q=getting+started+with+python&submit=" == driver.current_url        

    def fechar_agtnif(self):
        self.driver.close()

    
    def __init__(self,nifverificar):
        self.nifverificar = nifverificar

nifcliente = AgtNifCheck('5417283657')
nifcliente.agtnif_setup()
asyncio.run(nifcliente.pagina_agtnif())
nifcliente.fechar_agtnif()


'''

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        #self.driver = webdriver.Firefox()
        self.driver = webdriver.Chrome('/usr/bin/chromedriver')

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        #elem = driver.find_element_by_name("q")
        elem = driver.find_element("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()

'''