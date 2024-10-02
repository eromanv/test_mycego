from django.shortcuts import render, HttpResponse
from .forms import PublicKeyForm
from .utils import get_files_from_yandex_disk, get_download_link

def file_list_view(request):
    form = PublicKeyForm()
    files = None
    if request.method == 'POST':
        form = PublicKeyForm(request.POST)
        if form.is_valid():
            public_key = form.cleaned_data['public_key']
            files = get_files_from_yandex_disk(public_key)
    
    return render(request, 'files/file_list.html', {'form': form, 'files': files})


def download_file(request, public_key, file_path):
    download_url = get_download_link(public_key, file_path)
    if download_url:
        response = requests.get(download_url, stream=True)
        filename = file_path.split('/')[-1]
        response = HttpResponse(response.content, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename={filename}'
        return response
    return HttpResponse('Ошибка загрузки файла.')
