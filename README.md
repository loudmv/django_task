### Once you clone the repo, please execute the below commands in order to start the app locally:

1 - python manage.py makemigrations
2 - python manage.py migrate
3 - python manage.py runserver
4 - python manage.py createsuperuser - if you want to access the admin panel

### There are 2 custom commands:

python manage.py load_csv --file_path
This command loads a csv with candidates and their scores into the DB

python manage.py json_to_csv --input_file_path --output_file_path
This command converts a json file with candidates and scores to a csv
