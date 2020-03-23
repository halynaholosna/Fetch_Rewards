Fetch_Rewards_Coding_challenge
Selenium Test Automation Framework
written in

Python / Selenium / Behave
How to install and run:
Download Python 3.7 (do NOT use python version below 3.5).
Install Python from downloaded package. (Alternatively, you can use desktop anaconda app for easier work with envs Python 3, Anaconda, work with environments)
Clone the project, navigate to project directory from your terminal, run: pip3 install -r requirements.txt
To run all the tests from terminal, inside the project, run behave features. To launch 1 feature, run behave features/tests/<feature_name>.featuregit
Behave
features package contains tests (feature file scenarios), steps, and environment.

feature files contain test scenarios written as text with behave keywords
test steps define scenario statements and translate English text to Python
environment.py file links test steps to app package and defines set of methods to execute before and after every test feature/scenario/step.
Official documentation about BDD, keywords, and running behave scenarios.
