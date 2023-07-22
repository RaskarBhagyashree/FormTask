from django import forms


class Employeeform(forms.Form):
   # class Meta:
      #  model=EmpDetails
        #fields=['fname','lname','dob','email','phone']
         fname=forms.CharField(max_length=50)
         lname=forms.CharField(max_length=50)
         dob=forms.DateField()
         email=forms.EmailField()
         phone=forms.CharField(max_length=10)
    
    