from django.shortcuts import render
import random

# Create your views here.
def index(request):
	return render(request, "bonesday/index.html")

def bones(request):
	#Random bones day
	isitbones = bool(random.getrandbits(1))

	return render(request, "bonesday/bones.html", {
		"bonestoday": isitbones == True
	})
	