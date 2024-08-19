from django import forms


class LessonExerciseForm(forms.Form):
    exercise_id = forms.CharField(max_length=100)
    solution = forms.CharField(widget=forms.Textarea)
    solution_output = forms.CharField(widget=forms.Textarea)


class UserProfileUpdateForm(forms.Form):
    first_name = forms.CharField(max_length=255, strip=True)
    last_name = forms.CharField(max_length=255, strip=True)
    username = forms.CharField(max_length=255, strip=True)
    email = forms.CharField(max_length=255, strip=True)
    title = forms.CharField(max_length=255, strip=True, required=False)
    profile_picture = forms.ImageField(
        widget=forms.FileInput, required=False)


class UserPasswordChangeForm(forms.Form):
    old_password = forms.CharField(
        widget=forms.PasswordInput, label='Current Password')
    new_password = forms.CharField(
        widget=forms.PasswordInput, label='New Password')
    new_password_confirmation = forms.CharField(
        widget=forms.PasswordInput, label='Confirm New Password')
