from django.shortcuts import render
# from django.views.generic import TemplateView

# class test(TemplateView):
#     template_name = 'main/test.html'


def test(request):
    return render(request, 'main/test.html')

