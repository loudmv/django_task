from candidates.models import Candidate, Score
from candidates.validators import validate_8char_length, validate_alnum, validate_float_0_100
from django.core.management.base import BaseCommand

import pandas as pd


class Command(BaseCommand):
    help = 'Load candidates from csv file.'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='File name and path to the csv file.')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']

        df = pd.read_csv(file_path)

        for index, row in df.iterrows():
            candidate = Candidate()
            score = Score()
            try:
                validate_8char_length(row['candidate_ref'])
                validate_alnum(row['candidate_ref'])
                candidate.name = row['name']
                candidate.candidate_reference = row['candidate_ref']
                candidate.save()
                validate_float_0_100(row['score'])
                score.candidate_reference = row['candidate_ref']
                score.score = row['score']
                score.save()
            except:
                pass
