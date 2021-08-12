# 1 задание
# Имя;
# ■ Фамилия;
# ■ E-mail;
# ■ Контактный телефон;
# ■ Адрес;
# ■ Количество месяцев доставки воды (возможные варианты: один месяц, три месяца, шесть месяцев, двенадцать месяцев);
# ■ Объём баллона воды (возможные варианты: 5 литров,
# 10 литров, 15 литров).

from django import forms


class UserForm(forms.Form):
    firstname = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите имя',
        }),
        label='Имя'
    )
    lastname = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите фамилию',
        }),
        label='Фамилия'
    )
    email = forms.EmailField(
        required=True,
        widget = forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите почтовый адрес',
            'label': 'Email'
        }),
        label='Email'
    )


class WaterDeliveryForm(UserForm):
    phone = forms.CharField(
        required=True,
        widget = forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+380-xx-xxx-xx-xx',
        }),
        min_length=10,
        max_length=10,
        label = 'Номер телефона'
    )
    address = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите адрес доставки',
        }),
        label = 'Адрес доставки'
    )
    delivery_months = forms.ChoiceField(
        choices=(
            (1, '1 месяц'),
            (6, '6 месяцев'),
            (12, '12 месяцев')
        ),
        widget=forms.Select(attrs={
            'class': 'form-select',
            'placeholder': 'Выберите срок доставки',
        }),
        label='Срок доставки',
        initial=1
    )
    water_volume = forms.ChoiceField(
        choices=(
            (5, '5 литров'),
            (10, '10 литров'),
            (15, '15 литров')
        ),
        widget=forms.Select(attrs={
            'class': 'form-select',
            'placeholder': 'Выберите объем воды',
        }),
        label='Объем воды',
        initial=5
    )
