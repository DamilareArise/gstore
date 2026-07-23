from django import forms
from .models import Product, Brand, Category, ProductImages, ProductSpecification



# class ProductForm(forms.Form):
#     BRAND_CHOICES = [(brand.id, brand.name) for brand in Brand.objects.all()]
    
    
#     title = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Enter product title', 'class': 'form-control mb-2'}))
#     price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'placeholder': 'Enter product price', 'class': 'form-control mb-2'}))
#     description = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Enter product description', 'class': 'form-control mb-2'}))
#     category = forms.ChoiceField(choices=BRAND_CHOICES, widget=forms.Select(attrs={'class': 'form-control mb-2'}))
#     image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control mb-2'}))



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'price', 'quantity', 'description', 'brand']
        
        # widgets = {
        #     'title': forms.TextInput(attrs={'placeholder': 'Enter product title', 'class': 'form-control mb-2'}),
        #     'price': forms.NumberInput(attrs={'placeholder': 'Enter product price', 'class': 'form-control mb-2'}),
        #     'quantity': forms.NumberInput(attrs={'placeholder': 'Enter product quantity', 'class': 'form-control mb-2'}),
        #     'description': forms.Textarea(attrs={'placeholder': 'Enter product description', 'class': 'form-control mb-2'}),
        #     'brand': forms.Select(attrs={'class': 'form-control mb-2'}),
        # }
        
        
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ['name', 'category']
        

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
        
class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImages
        fields = ['image', 'is_cover']
        
        
class ProductSpecificationForm(forms.ModelForm):
    class Meta:
        model = ProductSpecification
        fields = ['key', 'value']