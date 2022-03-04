import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

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
    deps.append(option.text) # Se appendea en la lista deps el nombre hallado anteriormente --> se usa "search.text" porque los elementos extraídos no están en forma de texto y se tienen que pasar a texto

totales, total_kf, total_pc, porcent_kf, porcent_pc, porcent_participacion, porcent_validos = [], [], [], [], [], [], []

for dep in deps:
    search = Select(driver.find_element(By.ID, "select_departamento")) # Busca el pop-up para poner los departamentos
    search.select_by_visible_text(dep) # Manda los departamentos que están guardados en la lista
    total = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[3]") #Halla el total de los votos
    totales.append(total.text)
    kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[4]")
    total_kf.append(kf.text)
    p_kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[5]")
    porcent_kf.append(p_kf.text)
    pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[4]")
    total_pc.append(pc.text)
    p_pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[5]")
    porcent_pc.append(p_pc.text)
    part = driver.find_element(By.ID, "porPartCiudadanapor")
    porcent_participacion.append(part.text)
    valid = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[5]")
    porcent_validos.append(valid.text)

with open("/Users/rodrigo/Desktop/elecciones_2021/General/resultados_generales.csv", "w", encoding="UTF8", newline="") as f:
    writer = csv.writer(f)

    writer.writerow(["DEPARTAMENTO", "ACTAS PROCESADAS", "ACTAS CONTABILIZADAS", "VOTOS VALIDOS", "TOTAL KF", "TOTAL PC", "% KF", "% PC", "ACTAS JNE", "% PARTICIPACION", "% VALIDOS"])
    data = []
    for i in range(len(deps)):
        data_raw = list()
        data_raw.append(deps[i])
        data_raw.append(totales[i])
        data_raw.append(total_kf[i])
        data_raw.append(total_pc[i])
        data_raw.append(porcent_kf[i])
        data_raw.append(porcent_pc[i])
        data_raw.append(porcent_participacion[i])
        data_raw.append(porcent_validos[i])
        data.append(data_raw)
    writer.writerows(data)

driver.get("https://resultadoshistorico.onpe.gob.pe/SEP2021/EleccionesPresidenciales/RePres/P")
WebDriverWait(driver, 10).until(EC.url_matches("https://resultadoshistorico.onpe.gob.pe/SEP2021/EleccionesPresidenciales/RePres/P"))
total = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[3]")
kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[4]")
p_kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[5]")
pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[4]")
p_pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[5]")
part = driver.find_element(By.ID, "porPartCiudadanapor")
valid = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[5]")

with open("/Users/rodrigo/Desktop/elecciones_2021/General/resultados_generales.csv", "a", encoding="UTF8") as f:
    writer = csv.writer(f)
    writer.writerows([["", "", "", "", "", "", "", ""], ["PERU", total.text, kf.text, pc.text, p_kf.text, p_pc.text, part.text, valid.text]])

driver.get("https://resultadoshistorico.onpe.gob.pe/SEP2021/EleccionesPresidenciales/RePres/E")
WebDriverWait(driver, 10).until(EC.url_matches("https://resultadoshistorico.onpe.gob.pe/SEP2021/EleccionesPresidenciales/RePres/E"))
total = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[3]")
kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[4]")
p_kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[5]")
pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[4]")
p_pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[5]")
part = driver.find_element(By.ID, "porPartCiudadanapor")
valid = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[5]")

with open("/Users/rodrigo/Desktop/elecciones_2021/General/resultados_generales.csv", "a", encoding="UTF8") as f:
    writer = csv.writer(f)
    writer.writerows([["", "", "", "", "", "", "", ""], ["EXTRANJERO", total.text, kf.text, pc.text, p_kf.text, p_pc.text, part.text, valid.text]])

driver.get("https://resultadoshistorico.onpe.gob.pe/SEP2021/EleccionesPresidenciales/RePres/T")
WebDriverWait(driver, 10).until(EC.url_matches("https://resultadoshistorico.onpe.gob.pe/SEP2021/EleccionesPresidenciales/RePres/T"))
total = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[3]")
kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[4]")
p_kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[5]")
pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[4]")
p_pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[5]")
part = driver.find_element(By.ID, "porPartCiudadanapor")
valid = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[5]")

with open("/Users/rodrigo/Desktop/elecciones_2021/General/resultados_generales.csv", "a", encoding="UTF8") as f:
    writer = csv.writer(f)
    writer.writerows([["", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", ""], ["TOTAL", total.text, kf.text, pc.text, p_kf.text, p_pc.text, part.text, valid.text]])