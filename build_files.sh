python3.9 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3.9 manage.py collectstatic
python3.9 manage.py migrate
python3.9 data_create.py