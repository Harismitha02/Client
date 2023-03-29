from django import forms
from .models import user
class UserForm(forms.ModelForm):
    class Meta:
        model=user
        fields=('fullname','user_id','mobile','previl')
        labels={
            'fullname':'Name',
            'user_id' : 'User ID',
            'mobile' : 'Mobile',
            'previl' : 'Privilege',
        }

        
    
    def __init__(self,*args,**kwargs):
        super(UserForm,self).__init__(*args,**kwargs)
        self.fields['previl'].empty_label="Select"
        self.fields['user_id'].required=False

# class ActivityForm(forms.ModelForm):
#     class Meta:
#         model=clients
#         fields=('client',)
#         labels={
#             'client' : 'Client Name',
            
#         }
    
#     def __init__(self,*args,**kwargs):
#         super(ActivityForm,self).__init__(*args,**kwargs)
#         self.fields['client'].empty_label="Select"