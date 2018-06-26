from django.shortcuts import render, HttpResponse
import zipfile
import re


# Create your views here.


def op_zip(zip_file):
    zfile = zipfile.ZipFile(zip_file, 'r')

    zfile_name_list = zfile.namelist()
    # zfile_name_list = list(filter(lambda x: re.findall('\.[a-z]+$', x), zfile_name_list))
    # print(zfile_name_list)
    # html_files = filter(lambda x: x.endswith('.html'), zfile_name_list)
    # py_files = filter(lambda x: x.endswith('.py'), zfile_name_list)
    # css_files = filter(lambda x: x.endswith('.css'), zfile_name_list)
    # js_files = filter(lambda x: x.endswith('.js'), zfile_name_list)

    count_file = {'html': 0, 'py': 0, 'css': 0, 'js': 0}
    for file_name in zfile.namelist():
        # if file_name.endswith('.zip'):
        #     child_zip_file = zfile.getinfo(file_name)
        #     print(zipfile.is_zipfile(file_name))
        #
        #     data = zfile.read(file_name)
        #     print(data)
        #     res = op_zip(child_zip_file)
        #     for k in res:
        #         count_file[k] += res[k]

        if file_name.endswith('.html'):
            data = zfile.read(file_name)
            data_list = data.decode('utf8').split('\r\n')
            zhu = 0
            html_count = 0
            for line in data_list:
                if line.startswith('//'):
                    continue
                if line.startswith('<!--') or line.startswith('/*'):
                    zhu += 1
                if line.endswith('-->') or line.endswith('*/'):
                    zhu -= 1
                if zhu == 0:
                    html_count += 1
            count_file['html'] += html_count
        elif file_name.endswith('.py'):
            data = zfile.read(file_name)
            data_list = data.decode('utf8').split('\r\n')
            zhu = 0
            py_count = 0
            for line in data_list:
                if line.startswith('#'):
                    continue
                if line.startswith("\'\'\'") or line.startswith('\"\"\"'):
                    zhu += 1
                if line.endswith("\'\'\'") or line.endswith('\"\"\"'):
                    zhu -= 1
                if zhu == 0 and line:
                    py_count += 1
            count_file['py'] = py_count
        elif file_name.endswith('.css'):
            data = zfile.read(file_name)
            data_list = data.decode('utf8').split('\r\n')
            zhu = 0
            css_count = 0
            for line in data_list:
                if line.startswith('//'):
                    continue
                if line.startswith('/*'):
                    zhu += 1
                if line.endswith('*/'):
                    zhu -= 1
                if zhu == 0:
                    css_count += 1
            count_file['css'] += css_count

        elif file_name.endswith('.js'):
            data = zfile.read(file_name)
            data_list = data.decode('utf8').split('\r\n')
            zhu = 0
            js_count = 0
            for line in data_list:
                if line.startswith('//'):
                    continue
                if line.startswith('/*'):
                    zhu += 1
                if line.endswith('*/'):
                    zhu -= 1
                if zhu == 0:
                    js_count += 1
            count_file['js'] += js_count
    print(count_file)
    return count_file


def upload(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        upload_file = request.FILES.get('upload_file')
        count_file = op_zip(upload_file)
        print(count_file)
        return render(request, 'result.html', {'name': name, 'result': count_file})
    return render(request, 'upload.html')
