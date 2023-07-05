pip3 install -r deps.text

python manage.py collectstatic --no-input

python3 manage.py migrate