from django.conf import settings

def template_env(request):
	return {'ENV': settings.ENVIRONMENT}