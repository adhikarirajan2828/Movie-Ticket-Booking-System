from django import forms
from .models import Movies, movieCertificate, movieType, movieLanguage, movieShowtime


class AddMovieForm(forms.ModelForm):
    
    release_date=forms.DateTimeField(
        label= "Released Date",
        widget= forms.DateTimeInput(
            # format = '%Y-%m-%d',
            attrs={
                'type':'datetime-local'
            }),
        # input_formats=('%Y-%m-%d')
    )
    
    # movie_showtime=forms.MultipleChoiceField(choices=[(item.pk, item) for item in movieShowtime.objects.all()], widget=forms.CheckboxSelectMultiple)
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
           