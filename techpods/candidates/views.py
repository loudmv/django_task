from django.shortcuts import render
from django.db import models
from .models import Candidate, Score
import pandas as pd


def candidate_list(request):
    candidates = Candidate.objects.all().order_by('name')
    scores = Score.objects.all()

    scores_dict = {}
    for score in scores:
        if score.candidate_reference not in scores_dict:
            scores_dict[score.candidate_reference] = []
        scores_dict[score.candidate_reference].append(score.score)

    if scores_dict:
        max_value = max(scores_dict.values())[0]

    highlight_rows = []
    if len(candidates) > 0:
        for candidate in candidates:
            for can_ref, can_scores in scores_dict.items():
                if candidate.candidate_reference == can_ref:
                    can_scores.sort()
                    can_scores_str = ", ".join([str(value) for value in can_scores])
                    #TODO pretty sure this is not the correct way to do this...
                    candidate.scores = models.CharField(default='N/A')
                    candidate.scores = can_scores_str

                    if max_value in can_scores:
                        highlight_rows.append(candidate.candidate_reference)

    return render(request, 'candidates/candidate_list.html', {'candidate_scores': candidates, 'highlight': highlight_rows})
