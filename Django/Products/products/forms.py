from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder": "Your title"}))
    description = forms.CharField(
        label='Description',
        required=True,
        widget=forms.Textarea(
            attrs={
                "rows": 20,
                "cols": 120,
            }
        )
    )
    price = forms.DecimalField(max_digits=5, decimal_places=2, label='Price', widget=forms.TextInput())
    summary = forms.CharField(
        required=True,
        widget=forms.Textarea(
            attrs={
                "rows": 20,
                "cols": 120,
            }
        )
    )
    featured = forms.BooleanField(required=False)
    digital = forms.BooleanField(required=False)
    image = forms.ImageField()

    class Meta:
        model = Product
        fields = [ 
            'title',
            'description',
            'price',
            'summary',
            'featured',
            'digital',
            'image',
        ]

    # def clean_title(self, *args, **kwargs):
    #     title = self.cleaned_data.get("title")
    #     if not "CFE" in title: 
    #         raise forms.ValidationError("This is not a valid title")
    #     return title
    def clean_email(self, *args, **kwargs):
        email = self.cleaned_data.get("email")
        if not email.contains("@"): 
            raise forms.ValidationError("This is not a valid email")
        return email