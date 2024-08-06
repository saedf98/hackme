from django import forms


class LessonExerciseForm(forms.Form):
    exercise_id = forms.CharField(max_length=100)
    solution = forms.CharField(widget=forms.Textarea)
    solution_output = forms.CharField(widget=forms.Textarea)
