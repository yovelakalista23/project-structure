# HOW TO RUN DASHBOARD

## SETUP ENVIRONMENT - ANACONDA
```bash
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```
## SETUP ENVIRONMENT -TERMINAL
```bash
mkdir project-structure
cd project-structure
pipenv install
pipenv shell
pip install -r requirements.txt
```
## RUN STREAMLIT
```bash
streamlit run dashboard.py
```
