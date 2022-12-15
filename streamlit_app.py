# import os
# from selenium.webdriver.support.wait import WebDriverWait

import streamlit as st
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-features=NetworkService")
options.add_argument("--window-size=1920x1080")
options.add_argument("--disable-features=VizDisplayCompositor")

def run_selenium():
    name = str()
    with webdriver.Chrome(options=options, service_log_path='selenium.log') as navegador:
        # Passa o Link do Pronto para o navegador
        navegador.get("https://pronto.blumenau.sc.gov.br/pronto/home.aspx")

        # Clica no botão "Confirmar"
        navegador.find_element(By.XPATH, '//*[@id="BUTTON1"]').click()

        # Espera 0,5 segundos para limpar e preencher a textbox de login
        time.sleep(0.5)
        navegador.find_element(By.XPATH, '//*[@id="vLOGINCODIGO"]').clear()
        navegador.find_element(By.XPATH, '//*[@id="vLOGINCODIGO"]').send_keys("edu")

        # Espera 0,5 segundos para preencher a textbox de Senha
        time.sleep(0.5)
        navegador.find_element(By.XPATH, '//*[@id="vSENHA"]').send_keys("eduardo06")

        # Clica no botão "Entrar"
        navegador.find_element(By.XPATH, '//*[@id="IMAGE3"]').click()
        time.sleep(0.5)
        url = 'https://pronto.blumenau.sc.gov.br/pronto/wwcep.aspx'
        navegador.get(url)
        time.sleep(0.5)
        name = navegador.find_element(By.XPATH, '//*[@id="span_CEPCODIGO_0001"]')
        name = name.text

    return name


if __name__ == "__main__":
    st.set_page_config(page_title="Teste", page_icon='✅')
        # initial_sidebar_state='collapsed')
    st.title('Teste')
    # st.balloons()
    if st.button('Teste'):
        st.info('Rodando...')
        result = run_selenium()
        st.info(f'Resultado -> {result}')
