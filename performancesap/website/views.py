from django.http import HttpResponse 
from django.shortcuts import render, get_object_or_404 
from django.views import View 

# Create your views here.

class ContactView(View):
	def get(self, request, *args, **kargs):
		context_data = {
			"title": "INDEX WEBSITE HTML"
		}
		return render(request, "index.html", context_data)

def post_create(request):
	return HttpResponse("<h1>Create</h1>")

def post_detail(request, id):
	instance = get_object_or_404(Post, id=None)
	# # # if request.user.is_authenticated():
	# # 	context_data = {
	# # 		"title":"My Detail"
	# # 	}
	# else:
	context_data = {
		"title":instance.title,
		"instance":instance
	}
	return render(request, 'details.html', context_data)

def initial(request):
	# queryset = get_object_or_404(Post, id=1)
	# # # if request.user.is_authenticated():
	# # 	context_data = {
	# # 		"title":"My Detail"
	# # 	}
	# else:
	context_data = {
		"title":"INDEX WEBSITE HTML",
		# "object_list":queryset
	}
	return render(request, 'index.html', context_data)
