# test-framework-python-selenium-pytest
Test Automation framework using Python, Selenium and Pytest

#Installations
pip install selenium

pip install pytest

pip install webdriver-manager

pip install pytest-html

pip install pytest-xdist

pip install Openpyxl


#Command to run the tests from project root folder
pytest -v -s -n=3 --html=reports/report.html src/testCases/* --browser chrome

pytest -v -s -n=3 -m "sanity or regression" --html=reports/report.html src/testCases/* --browser chrome
