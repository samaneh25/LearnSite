from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


# class SingleBlogForms(forms.Form):
#     title = forms.CharField(max_length=100)
#     primary_image = forms.ImageField()
#     body = forms.CharField(widget=SummernoteWidget)
#
# class FormFromSingleBlogForms(forms.ModelForm):
#     class Meta:
#         model = SingleBlogForms
#         fields = ['title', 'body']
#         widgets = {
#             'foo': SummernoteWidget(),
#             'bar': SummernoteInplaceWidget(),
#         }
#
