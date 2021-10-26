import csv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

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

for dep in deps:
    search = driver.find_element(By.ID, "select_departamento")
    search.send_keys(dep)
    provs, totales, contabilizadas, total_kf, total_pc, porcent_kf, porcent_pc, impugnados = [], [], [], [], [], [], [], []

    search = driver.find_element(By.ID, "cod_prov")
    options = [x for x in search.find_elements(By.TAG_NAME, "option")]

    for i in range(len(options)):
        if i != 0:
            search = driver.find_element(By.XPATH, f"//select[@id='cod_prov']/option[{i + 1}]")
            provs.append(search.text)

    for i in range(len(provs)):
        if "NH" in provs[i]:
            provs[i] = provs[i].replace("NH", "Ñ")

    search = driver.find_element(By.ID, "select_departamento")
    time.sleep(2)
    for prov in provs:
        search = driver.find_element(By.ID, "cod_prov")
        search.send_keys(prov)
        time.sleep(2)

        total = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[3]")
        totales.append(total.text)
        contab = driver.find_element(By.XPATH, "//ul[@class='datos_leyend align-middle']/li[2]")
        contabilizadas.append(contab.text.lstrip("ACTAS CONTABILIZADAS: "))
        kf = driver.find_element(By.XPATH,
            "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[4]")
        total_kf.append(kf.text)
        p_kf = driver.find_element(By.XPATH,
            "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[5]")
        porcent_kf.append(p_kf.text)
        pc = driver.find_element(By.XPATH,
            "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[4]")
        total_pc.append(pc.text)
        p_pc = driver.find_element(By.XPATH,
            "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[5]")
        porcent_pc.append(p_pc.text)
        impug = driver.find_element(By.XPATH, "//table[@class='table table-striped tablas']/tr[5]/td[2]")
        impugnados.append(impug.text)

    with open(f"/Users/rodrigo/Desktop/elecciones_2021/Departamentos/{dep}/resultados.csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)

        writer.writerow(["PROVINCIA", "ACTAS CONTABILIZADAS", "VOTOS VALIDOS", "TOTAL KF", "TOTAL PC", "% KF", "% PC", "ACTAS IMPUGNADAS"])
        data = []
        for i in range(len(provs)):
            data_raw = list()
            data_raw.append(provs[i])
            data_raw.append(contabilizadas[i])
            data_raw.append(totales[i])
            data_raw.append(total_kf[i])
            data_raw.append(total_pc[i])
            data_raw.append(porcent_kf[i])
            data_raw.append(porcent_pc[i])
            data_raw.append(impugnados[i])
            data.append(data_raw)
        writer.writerows(data)


    search = driver.find_element(By.ID, "cod_prov")
    search.send_keys("--")
    time.sleep(2)
    total = driver.find_element(By.XPATH, "//tr[@class='datos_voto']/td[3]")
    contab = driver.find_element(By.XPATH, "//ul[@class='datos_leyend align-middle']/li[2]")
    kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[4]")
    p_kf = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[4]/td[5]")
    pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[4]")
    p_pc = driver.find_element(By.XPATH, "//table[@class='main-table table table-striped tabla_resultado']/tr[3]/td[5]")
    impug = driver.find_element(By.XPATH, "//table[@class='table table-striped tablas']/tr[5]/td[2]")

    with open(f"/Users/rodrigo/Desktop/elecciones_2021/Departamentos/{dep}/resultados.csv", "a", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        writer.writerows([["", "", "", "", "", "", ""], [dep, contab.text.lstrip("ACTAS CONTABILIZADAS: "), total.text, kf.text, pc.text, p_kf.text, p_pc.text, impug.text]])