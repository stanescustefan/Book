from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	DIVISION_CHOICES = (
		('Arad', 'Arad'),
		('Bacau', 'Bacau'),
		('Bucuresti', 'Bucuresti'),
		('Cluj', 'Cluj'),
		('Iasi', 'Iasi'),
	)

	DISCRICT_CHOICES = (
		('Arad', 'Arad'),
		('Bacau', 'Bacau'),
		('Bucuresti', 'Bucuresti'),
		('Cluj', 'Cluj'),
		('Iasi', 'Iasi'),
	)

	# PAYMENT_METHOD_CHOICES = (
	# 	('Card', 'Card'),
	# 	('PayPal', 'PayPal')
	# )

	country = forms.ChoiceField(choices=DIVISION_CHOICES)
	# payment_method = forms.ChoiceField(choices=PAYMENT_METHOD_CHOICES, widget=forms.RadioSelect())

	class Meta:
		model = Order
		fields = ['name', 'email', 'phone', 'address', 'country', 'zip_code','card_no']
