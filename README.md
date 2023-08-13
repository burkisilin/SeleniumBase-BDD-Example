# Wask-Case-Study
[![Python](https://img.shields.io/badge/Python-yellow?style=flat&logo=python)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-blue?style=flat&logo=selenium)](https://www.selenium.dev/)
[![Selenium Base](https://img.shields.io/badge/SeleniumBase-green?style=flat&logo=selenium)](https://seleniumbase.io/)
[![PyTest](https://img.shields.io/badge/PyTest-orange?style=flat&logo=pytest)](https://docs.pytest.org/en/6.2.x/)
[![Allure](https://img.shields.io/badge/Allure-blue?style=flat&logo=java)](https://docs.qameta.io/allure/)
[![Behave](https://img.shields.io/badge/Behave-red?style=flat&logo=behave)](https://behave.readthedocs.io/en/latest/)


This project aims to cover example test cases for arabam.com using Behave & Selenium Base


## Project Structure Summary
"config" folder contains test data configs such as selectors, environment url's etc. in order to provide the low-cost maintenance for the project.  
"features" folder contains "steps" folder, "todo features" folder, feature files and "environment.py" which is required for SeleniumBase.  
"steps" folder contains step functions to execute tests from gherkin formatted feature files.   
"todo features" folder contains example test scenarios which are not added due to lack of time.
feature files contain test scenarios and test steps written in gherkin format using cucumber.  
"utils" folder contain "Helpers.py" which contains functions such as "return_int_from_string"

## Dependencies

Here are all the dependencies needed for the project to run:


Tools                 |       Versions
-------------         |       -------------
Python                |         3.8 + 
Pytest                |         7.4.0
Pytest-bdd            |         6.1.1
Selenium              |         4.11.2
Selenium Base         |         4.17.2
Behave                |         1.2.6

Inorder to run the project, first, Python and the necessary packages needs to be installed. You can install the required packages automatically by running the code provided below.
```bash 
pip install -r /path/to/requirements.txt
```


run the tests by executing the command at your terminal (Uses --chrome by default)
```bash 
cd Wask-Case-Study/
behave ./features/ -D dashboard -D 
```
other browsers can be run in such example down below. See [Selenium Base Docs](https://seleniumbase.io/) for details

```bash 
cd Wask-Case-Study/
behave ./features/ -D dashboard -D --firefox
```

You can also use ``--junit`` to get ``.xml`` reports for each Behave feature. Jenkins can use these files to display better reporting for the tests.

### Note  
Some scenarios such as login failure scenarios may fail due to bot protection (captcha) on arabam.com  
Some scenarios fail due to bugs present on production env :)

Example:  
![bug example](https://i.ibb.co/dPfG2QR/arabam-bug.png)
