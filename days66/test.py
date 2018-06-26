# import re
#
# li =['day62/', 'day62.zip', 'day62/mysiteday62/', 'day62/mysiteday62/.idea/', 'day62/mysiteday62/.idea/dataSources/', 'day62/mysiteday62/.idea/dataSources.local.xml', 'day62/mysiteday62/.idea/dataSources.xml', 'day62/mysiteday62/.idea/dataSources/77017d31-fe8a-4e0e-80c7-1d64a47081bc.xml', 'day62/mysiteday62/.idea/dictionaries/', 'day62/mysiteday62/.idea/dictionaries/oldboy.xml', 'day62/mysiteday62/.idea/misc.xml', 'day62/mysiteday62/.idea/modules.xml', 'day62/mysiteday62/.idea/mysiteday62.iml', 'day62/mysiteday62/.idea/workspace.xml', 'day62/mysiteday62/app01/', 'day62/mysiteday62/app01/admin.py', 'day62/mysiteday62/app01/apps.py', 'day62/mysiteday62/app01/migrations/', 'day62/mysiteday62/app01/migrations/0001_initial.py', 'day62/mysiteday62/app01/migrations/0002_delete_user.py', 'day62/mysiteday62/app01/migrations/0003_user.py', 'day62/mysiteday62/app01/migrations/0004_auto_20180612_1042.py', 'day62/mysiteday62/app01/migrations/0005_publisher.py', 'day62/mysiteday62/app01/migrations/__init__.py', 'day62/mysiteday62/app01/migrations/__pycache__/', 'day62/mysiteday62/app01/migrations/__pycache__/0001_initial.cpython-36.pyc', 'day62/mysiteday62/app01/migrations/__pycache__/0002_delete_user.cpython-36.pyc', 'day62/mysiteday62/app01/migrations/__pycache__/0003_user.cpython-36.pyc', 'day62/mysiteday62/app01/migrations/__pycache__/0004_auto_20180612_1042.cpython-36.pyc', 'day62/mysiteday62/app01/migrations/__pycache__/0005_publisher.cpython-36.pyc', 'day62/mysiteday62/app01/migrations/__pycache__/__init__.cpython-36.pyc', 'day62/mysiteday62/app01/models.py', 'day62/mysiteday62/app01/tests.py', 'day62/mysiteday62/app01/views.py', 'day62/mysiteday62/app01/__init__.py', 'day62/mysiteday62/app01/__pycache__/', 'day62/mysiteday62/app01/__pycache__/admin.cpython-36.pyc', 'day62/mysiteday62/app01/__pycache__/models.cpython-36.pyc', 'day62/mysiteday62/app01/__pycache__/views.cpython-36.pyc', 'day62/mysiteday62/app01/__pycache__/__init__.cpython-36.pyc', 'day62/mysiteday62/db.sqlite3', 'day62/mysiteday62/manage.py', 'day62/mysiteday62/mysiteday62/', 'day62/mysiteday62/mysiteday62/settings.py', 'day62/mysiteday62/mysiteday62/urls.py', 'day62/mysiteday62/mysiteday62/wsgi.py', 'day62/mysiteday62/mysiteday62/__init__.py', 'day62/mysiteday62/mysiteday62/__pycache__/', 'day62/mysiteday62/mysiteday62/__pycache__/settings.cpython-36.pyc', 'day62/mysiteday62/mysiteday62/__pycache__/urls.cpython-36.pyc', 'day62/mysiteday62/mysiteday62/__pycache__/wsgi.cpython-36.pyc', 'day62/mysiteday62/mysiteday62/__pycache__/__init__.cpython-36.pyc', 'day62/mysiteday62/static/', 'day62/mysiteday62/static/bootstrap-3.3.7/', 'day62/mysiteday62/static/bootstrap-3.3.7/css/', 'day62/mysiteday62/static/bootstrap-3.3.7/css/bootstrap.min.css', 'day62/mysiteday62/static/bootstrap-3.3.7/fonts/', 'day62/mysiteday62/static/bootstrap-3.3.7/fonts/glyphicons-halflings-regular.eot', 'day62/mysiteday62/static/bootstrap-3.3.7/fonts/glyphicons-halflings-regular.svg', 'day62/mysiteday62/static/bootstrap-3.3.7/fonts/glyphicons-halflings-regular.ttf', 'day62/mysiteday62/static/bootstrap-3.3.7/fonts/glyphicons-halflings-regular.woff', 'day62/mysiteday62/static/bootstrap-3.3.7/fonts/glyphicons-halflings-regular.woff2', 'day62/mysiteday62/static/bootstrap-3.3.7/js/', 'day62/mysiteday62/static/bootstrap-3.3.7/js/bootstrap.min.js', 'day62/mysiteday62/static/dashboard.css', 'day62/mysiteday62/static/fontawesome/', 'day62/mysiteday62/static/fontawesome/css/', 'day62/mysiteday62/static/fontawesome/css/font-awesome.min.css', 'day62/mysiteday62/static/fontawesome/fonts/', 'day62/mysiteday62/static/fontawesome/fonts/fontawesome-webfont.eot', 'day62/mysiteday62/static/fontawesome/fonts/fontawesome-webfont.svg', 'day62/mysiteday62/static/fontawesome/fonts/fontawesome-webfont.ttf', 'day62/mysiteday62/static/fontawesome/fonts/fontawesome-webfont.woff', 'day62/mysiteday62/static/fontawesome/fonts/fontawesome-webfont.woff2', 'day62/mysiteday62/static/fontawesome/fonts/FontAwesome.otf', 'day62/mysiteday62/static/jquery-3.3.1.min.js', 'day62/mysiteday62/static/my-style.css', 'day62/mysiteday62/templates/', 'day62/mysiteday62/templates/add_publisher.html', 'day62/mysiteday62/templates/login.html', 'day62/mysiteday62/templates/publisher_list.html', 'day62/mysiteday62/templates/publisher_list2.html', 'day62课上笔记.txt']
# li = list(filter(lambda x: re.findall('\.[a-z]+$', x), li))
# # a = re.findall('\..*$', li)
# # b=li.endswith(r'\..*')
# print(li)
# # print(b)

# data=b'<!DOCTYPE html>\r\n<html lang="en">\r\n<head>\r\n    <meta charset="UTF-8">\r\n    <title>Title</title>\r\n  '
# data_list=data.decode('utf8').split('\r\n')
# print(data_list)