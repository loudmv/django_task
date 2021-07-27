from django.shortcuts import render
from .models import Candidate, Score


def candidate_list(request):
    candidates = Candidate.objects.all()
    scores = Score.objects.all()

    # scores_dict = {}
    #
    # for score in scores:
    #     if score.candidate_reference not in scores_dict:
    #         scores_dict[score.candidate_reference] = []
    #     scores_dict[score.candidate_reference].append(score.score)
    #
    # return_dict = []
    #
    # for candidate in candidates:
    #     for can_ref, can_scores in scores_dict.items():
    #         if candidate.candidate_reference == can_ref:
    #             can_scores_str = ", ".join([str(value) for value in can_scores])
    #             row = {
    #                 'name': candidate.name,
    #                 'candidate_reference': can_ref,
    #                 'candidate_scores_str': can_scores_str
    #              }
    #             return_dict.append(row)
    # return_dict = []
    # for candidate in candidates:
    #     for can_ref, can_scores in scores_dict.items():
    #         if candidate.candidate_reference == can_ref:
    #             can_scores_str = ", ".join([str(value) for value in can_scores])
    #             return_dict.append(
    #                 f"""
    #                 <td> {candidate.name} </td>
    #                 <td> {candidate.candidate_reference} </td>
    #                 <td> {can_scores_str} </td>
    #                 """
    #             )

    scores = "10, 20, 30, 40, 50"
    return render(request, 'candidates/candidate_list.html', {'candidate_scores': candidates, 'scores': scores})
