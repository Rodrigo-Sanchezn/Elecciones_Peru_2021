import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

#Es una pruebaaa
hola = []
hola.append("me llamo rodrigo")


# El path para abrir el driver de Chrome (ya arreglado con el método SERVICE)
s = Service("/Users/rodrigo/Downloads/chromedriver")
driver = webdriver.Chrome(service=s)
driver.get("https://resultadoshistorico.onpe.gob.pe/SEP2021/EleccionesPresidenciales/RePres/P")

time.sleep(3)
search = driver.find_element(By.ID, "select_departamento")
options = [x for x in search.find_elements(By.TAG_NAME, "option")]

deps = []
for i in range(len(options)):
    if i != 0:
        search = driver.find_element(By.XPATH, f"//select[@id='select_departamento']/option[{i+1}]")
        deps.append(search.text)

totales, procesadas, contabilizadas, total_kf, total_pc, porcent_kf, porcent_pc, enviadas_JNE, porcent_participacion, porcent_validos = [], [], [], [], [], [], [], [], [], []

for dep in deps:
    search = driver.find_element(By.ID, "select_departamento") # Busca el pop-up para poner los departamentos
    search.send_keys(dep) # Manda los departamentos que están guardados en la lista
    time.sleep(2)
    total = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[3]")
    totales.append(total.text)
    proce = driver.find_element(By.ID, "porActasProcesadas")
    procesadas.append(proce.text)
    contab = driver.find_element(By.XPATH, "//ul[@class='datos_leyend align-middle']/li[2]")
    contabilizadas.append(contab.text.lstrip("ACTAS CONTABILIZADAS: "))
    kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[4]")
    total_kf.append(kf.text)
    p_kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[5]")
    porcent_kf.append(p_kf.text)
    pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[4]")
    total_pc.append(pc.text)
    p_pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[5]")
    porcent_pc.append(p_pc.text)
    observ = driver.find_element(By.XPATH, "//table[@id='table2']/tr[3]/td[2]")
    observ = int(observ.text)
    impug = driver.find_element(By.XPATH, "//table[@class='table table-striped tablas']/tr[5]/td[2]")
    impug = int(impug.text)
    jne = observ - impug
    enviadas_JNE.append(jne)
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
        data_raw.append(procesadas[i])
        data_raw.append(contabilizadas[i])
        data_raw.append(totales[i])
        data_raw.append(total_kf[i])
        data_raw.append(total_pc[i])
        data_raw.append(porcent_kf[i])
        data_raw.append(porcent_pc[i])
        data_raw.append(enviadas_JNE[i])
        data_raw.append(porcent_participacion[i])
        data_raw.append(porcent_validos[i])
        data.append(data_raw)
    writer.writerows(data)

driver.get("https://resultadoshistorico.onpe.gob.pe/SEP2021/EleccionesPresidenciales/RePres/P")
time.sleep(4)
total = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[3]")
proce = driver.find_element(By.ID, "porActasProcesadas")
contab = driver.find_element(By.XPATH, "//ul[@class='datos_leyend align-middle']/li[2]")
kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[4]")
p_kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[5]")
pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[4]")
p_pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[5]")
observ = driver.find_element(By.XPATH, "//table[@id='table2']/tr[3]/td[2]")
observ = int(observ.text)
impug = driver.find_element(By.XPATH, "//table[@class='table table-striped tablas']/tr[5]/td[2]")
impug = int(impug.text)
jne = observ - impug
part = driver.find_element(By.ID, "porPartCiudadanapor")
valid = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[5]")

with open("/Users/rodrigo/Desktop/elecciones_2021/General/resultados_generales.csv", "a", encoding="UTF8") as f:
    writer = csv.writer(f)
    writer.writerows([["","", "", "", "", "", "", "", "", "", ""], ["PERU", proce.text, contab.text.lstrip("ACTAS CONTABILIZADAS: "), total.text, kf.text, pc.text, p_kf.text, p_pc.text, jne, part.text, valid.text]])

driver.get("https://resultadoshistorico.onpe.gob.pe/SEP2021/EleccionesPresidenciales/RePres/E")
time.sleep(4)
total = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[3]")
proce = driver.find_element(By.ID, "porActasProcesadas")
contab = driver.find_element(By.XPATH, "//ul[@class='datos_leyend align-middle']/li[2]")
kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[4]")
p_kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[5]")
pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[4]")
p_pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[5]")
observ = driver.find_element(By.XPATH, "//table[@id='table2']/tr[3]/td[2]")
observ = int(observ.text)
impug = driver.find_element(By.XPATH, "//table[@class='table table-striped tablas']/tr[5]/td[2]")
impug = int(impug.text)
jne = observ - impug
part = driver.find_element(By.ID, "porPartCiudadanapor")
valid = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[5]")

with open("/Users/rodrigo/Desktop/elecciones_2021/General/resultados_generales.csv", "a", encoding="UTF8") as f:
    writer = csv.writer(f)
    writer.writerows([["","", "", "", "", "", "", "", "", ""], ["EXTRANJERO", proce.text, contab.text.lstrip("ACTAS CONTABILIZADAS: "), total.text, kf.text, pc.text, p_kf.text, p_pc.text, jne, part.text, valid.text]])

driver.get("https://resultadoshistorico.onpe.gob.pe/SEP2021/EleccionesPresidenciales/RePres/T")
time.sleep(4)
total = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[3]")
proce = driver.find_element(By.ID, "porActasProcesadas")
contab = driver.find_element(By.XPATH, "//ul[@class='datos_leyend align-middle']/li[2]")
kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[4]")
p_kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[5]")
pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[4]")
p_pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[5]")
observ = driver.find_element(By.XPATH, "//table[@id='table2']/tr[3]/td[2]")
observ = observ.text

if "," in observ:
    observ = observ.replace(",", "")

observ = int(observ)
impug = driver.find_element(By.XPATH, "//table[@class='table table-striped tablas']/tr[5]/td[2]")
impug = int(impug.text)
jne = observ - impug
part = driver.find_element(By.ID, "porPartCiudadanapor")
valid = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[5]")

with open("/Users/rodrigo/Desktop/elecciones_2021/General/resultados_generales.csv", "a", encoding="UTF8") as f:
    writer = csv.writer(f)
    writer.writerows([["", "", "", "", "", "", "", "", "", "", ""], ["", "", "", "", "", "", "", "", "", "", ""], ["TOTAL", proce.text, contab.text.lstrip("ACTAS CONTABILIZADAS: "), total.text, kf.text, pc.text, p_kf.text, p_pc.text, jne, part.text, valid.text]])