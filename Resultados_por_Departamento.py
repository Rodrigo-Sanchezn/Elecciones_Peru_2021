from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
import pandas as pd
import time

# El path para abrir el driver de Chrome
path = "/Users/rodrigosanchez/Selenium/chromedriver"
driver = webdriver.Chrome(path) # Asigna la ubicación del driver de chrome
driver.get("https://resultadoshistorico.onpe.gob.pe/SEP2021/EleccionesPresidenciales/RePres/P")# Abre la página de la ONPE con los resultados de Perú

WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "select_departamento"))) # Espera por un máximo de 10 segundos a que aparezca la lista de departamentos

search = driver.find_element(By.ID, "select_departamento") # Se busca la casilla de opciones donde se elige el departamento
options = search.find_elements(By.TAG_NAME, "option") # Se encuentra la lista de opciones de dicha casilla encontrada y cada opción se añade a la lista options
options.pop(0) # Elimina la opción 0, que hace referencia a "-elegir departamento-

deps = [] # Se crea una lista vacía llamada deps --> aquí se guardaran los nombres de los departamentos
for option in options:
    deps.append(option.text) # Se appendea en la lista deps el nombre hallado anteriormente --> se usa "option.text" porque los elementos extraídos no están en forma de texto y se tienen que pasar a texto

col_names = ["Departamento",
             "Votos Validos",
             "Total Fujimori",
             "Total Castillo",
             "% Fujimori",
             "% Castillo",
             "% Participacion",
             "% Validos"]

resultados = pd.DataFrame(columns=col_names) # Se crea un data frame en Pandas con los títulos de la futura tabla (títulos mencionados en col_names)
resultados.to_csv("resultados_por_departamento.csv", index=False) # Se pasa el data frame creado en la línea 33 a un archivo CSV

for dep in deps:
    data_raw = []
    search = Select(driver.find_element(By.ID, "select_departamento")) # Busca el pop-up para poner los departamentos
    search.select_by_visible_text(dep) # Manda los departamentos que están guardados en la lista
    data_raw.append(dep)
    time.sleep(2)
    total = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[3]") #Halla el total de los votos
    data_raw.append(total.text)
    kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[4]")
    data_raw.append(kf.text)
    pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[4]")
    data_raw.append(pc.text)
    p_kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[5]")
    data_raw.append(p_kf.text)
    p_pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[5]")
    data_raw.append(p_pc.text)
    part = driver.find_element(By.ID, "porPartCiudadanapor")
    data_raw.append(part.text)
    valid = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[5]")
    data_raw.append(valid.text)
    data = pd.DataFrame([data_raw])
    data.to_csv("resultados_por_departamento.csv", mode="a", index=False, header=False)

driver.quit()