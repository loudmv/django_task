from django.core.management.base import BaseCommand

import pandas as pd


class Command(BaseCommand):
    help = 'Converts the json input file to a csv output.'

    def add_arguments(self, parser):
        parser.add_argument('input_file_path', type=str, help='File name and path to the json file.')
        parser.add_argument('output_file_path', type=str, help='File name and path where the output csv should be saved.')

    def handle(self, *args, **kwargs):
        input_file_path = kwargs['input_file_path']
        output_file_path = kwargs['output_file_path']

        df = pd.read_json(input_file_path)
        df.sort_values(by=['score'], inplace=True, ignore_index=True)

        df.to_csv(output_file_path, index=False)
