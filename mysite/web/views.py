from django.http import HttpResponse

from web.models import Number
Number.objects.all()
s = Number(Nm = 0)

def plus(request):
	numberU = s.Nm +1
	s.Nm = numberU
	s.save()
	return HttpResponse("add Number = %d" %numberU)

def minus(request):
	numberD = s.Nm -1
	s.Nm = numberD
	s.save()
	return HttpResponse('minus Number = %d' %numberD)

def pre(request):
	p = s.Nm
	return HttpResponse('Number = %d' %p)
