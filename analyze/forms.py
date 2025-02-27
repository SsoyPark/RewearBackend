from django import forms
from .models import OrderInfo

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = OrderInfo
        fields = ['image']

class DesignForm(forms.Form):
    neck_line = forms.CharField(max_length=50, label="넥라인 (collar, round neck, v-neck, square neck, turtle neck, mock neck)")
    sleeve_length = forms.CharField(max_length=50, label="소매길이 (long-sleeved, short-sleeved, sleeveless)")
    pattern = forms.CharField(max_length=50, required=False, label="스웨터 패턴 (cable, waffle, plain)")
    pocket = forms.CharField(max_length=50, required=False, label="포켓 여부 (x, left, right)")
    zip = forms.CharField(max_length=50, required=False, label="지퍼 추가 여부 (x, half zip-up, full zip-up)")
    button = forms.CharField(max_length=50, required=False, label="버튼 추가 여부 (x, half, full)")
    addt_design = forms.CharField(max_length=100, required=False, label="추가 디자인 (crop, fit)")
