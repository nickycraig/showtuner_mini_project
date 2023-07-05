pip3 install -r deps.text

python3 manage.py collectstatic --no-input

python3 manage.py migrate