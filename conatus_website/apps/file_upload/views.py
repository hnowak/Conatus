from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.base import TemplateView

from .forms import UploadFileForm


# Create your views here.
class FileUpload(TemplateView):
    template_name = 'upload/file_upload.html'

    @staticmethod
    def file_upload(request: HttpRequest):
        if request.method == 'POST':
            form: UploadFileForm = UploadFileForm(request.POST, request.FILES)
            if form.is_valid():
                # todo: handle check file and go to next state
                return HttpResponseRedirect('')
        else:
            form: UploadFileForm = UploadFileForm()
            return render(request, template_name='upload.html', context={'form': form})

