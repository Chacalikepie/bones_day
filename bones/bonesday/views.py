from django.shortcuts import render

# Create your views here.
def index(request):
	#Change depending on bones day
	isitbones = True

	return render(request, "bonesday/index.html", {
		"bonestoday": isitbones == True
	})
