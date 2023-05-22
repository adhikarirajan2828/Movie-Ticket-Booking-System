from django import forms
from .models import Movies, movieCertificate, movieType, movieLanguage,movieShowtime, movieStatus
# 

class AddMovieForm(forms.ModelForm):
    
    release_date=forms.DateTimeField(
        label= "Released Date",
        widget= forms.DateTimeInput(
            
            attrs={
                'type':'date'
            }),
        
    )
    
 
    class Meta:
        model = Movies
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(AddMovieForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    


class AddMovieCertificate(forms.ModelForm):
    class Meta:
        model = movieCertificate
        fields = "__all__"
    
    
    def __init__(self, *args, **kwargs):
        super(AddMovieCertificate, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class AddMovieType(forms.ModelForm):
    class Meta:
        model = movieType
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(AddMovieType, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
    
class AddMovieLanguage(forms.ModelForm):
    class Meta:
        model = movieLanguage
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(AddMovieLanguage, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'    


class AddMovieShowtime(forms.ModelForm):
    class Meta:
        model = movieShowtime
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(AddMovieShowtime, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'    
           

class movieForm(forms.ModelForm):
    class Meta:
        model = Movies
        fields = "__all__"
        
    def __init__(self, *args, **kwargs):
        super(movieForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class addMovieStatus(forms.ModelForm):
    class Meta:
        model = movieStatus
        fields = "__all__"
        
        

