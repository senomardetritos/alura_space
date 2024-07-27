from django import forms


class LoginForms(forms.Form):
    nome = forms.CharField(
        label='Nome Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome'
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a senha'
            }
        )
    )


class CadastroForms(forms.Form):
    nome = forms.CharField(
        label='Nome Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome'
            }
        )
    )
    email = forms.CharField(
        label='Email',
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite o email'
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Digite a senha'
            }
        )
    )
    senha2 = forms.CharField(
        label='Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Repetir a senha'
            }
        )
    )

    def clean_nome(self):
        nome = self.cleaned_data.get('nome')
        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Não pode ter espaço em branco')
            else:
                return nome

    def clean_senha2(self):
        senha = self.cleaned_data.get('senha')
        senha2 = self.cleaned_data.get('senha2')
        if senha != senha2:
            raise forms.ValidationError('Senhas estão diferentes')
        else:
            return senha
