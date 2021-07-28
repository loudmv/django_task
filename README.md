#Once you clone the repo, please execute the below commands in order to start the app locally:

# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# python manage.py createsuperuser - if you want to access the admin panel

# There are 2 custom commands:

# python manage.py load_csv --file_path
# This command loads a csv with candidates and their scores into the DB

# python manage.py json_to_csv --input_file_path --output_file_path
# This command converts a json file with candidates and scores to a csv