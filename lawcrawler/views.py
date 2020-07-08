from django.shortcuts import render



def index(request):
    return render(request, template_name='index.html')


def pass_page(request, page_name):
    return render(request, template_name='{}.html'.format(page_name))
