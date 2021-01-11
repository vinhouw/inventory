from django.forms import ModelForm
from .models import *
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Field,ButtonHolder


class ItemForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'form-horizontal'
        self.helper.layout = Layout(
                Field('name', css_class='input-xlarge'),
                Field('partNumber', rows="3", css_class='input-xlarge'),
                # NEW:
                ButtonHolder(
                    Submit('submit', 'Submit', css_class='btn btn-primary')
                )
            )


    class Meta:
        model = Item
        fields = ['name', 
                    'partNumber',
                    'manufacturer',
                    'category',
                    'quantity', 
                    'size',
                    'unit_price',
                    'description',
                    'location',
                    'url'

        ]



class AddItemForm(ModelForm):  #add button
    class Meta:
        model = Item
        fields = ['received_quantity']


class CategoryForm(ModelForm):
    
    class Meta:
        model = Category
        fields = ['category_name']



# class ItemDetailsForm(ModelForm): # Modify
#     class Meta:
#         model = Item_details
#         fields = ['unit_price',
#                 'total_quantity',
#                 'size',
#                 'location'
#                 ]

