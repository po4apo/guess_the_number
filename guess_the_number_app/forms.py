from django import forms


class InputTwoNumberForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    one_number = forms.IntegerField(label='Первое число',
                                    min_value=0,
                                    )
    two_number = forms.IntegerField(label='Второе число',
                                    min_value=0)
