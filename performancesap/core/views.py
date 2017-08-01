from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

# Create your views here.
class CoreViews(View):
	def get(self, request, *args, **kargs):
		context_data = {

		}
		return render(request, "index.html", context_data)

	# def post(self, request, *args, **kargs):
	# 	context_data = {
			
	# 	}
	# 	return render(request, "index.html", context_data)

	# def put(self, request, *args, **kargs):
	# 	context_data = {
			
	# 	}
	# 	return render(request, "index.html", context_data)