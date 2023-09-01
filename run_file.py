import subprocess
import os

path = os.getcwd()


def start():
    allure_report = input("Построить отчет в Allure? [Y(да)/N(нет)]\n")
    if allure_report.lower() == 'y':
        command = 'python -m pytest --alluredir=test_results/ tests/test_google_maps_api.py'
        create_allure_report = subprocess.call(command, shell=True)
        open_allure_report = subprocess.call('allure serve test_results', shell=True)
    else:
        command = 'python -m pytest -s -v'
        test_run = subprocess.call(command, shell=True)


start()
