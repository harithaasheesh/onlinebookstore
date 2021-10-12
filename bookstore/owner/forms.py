from django import forms

class BookForm(forms.Form):
    book_name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    author=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    price=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    copies=forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))
    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data["price"]
        copies=cleaned_data["copies"]
        if price<0:
            msg="invalid price"
            self.add_error("price",msg)
        if copies<0:
            msg="invalid copies"
            self.add_error("copies",msg)
