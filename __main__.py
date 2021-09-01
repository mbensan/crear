import pdb
import sys
import os
import fileinput


def add_after(filename, old_line, new_line):
    with fileinput.FileInput(filename, inplace=True, backup = '.bak') as f:
        for line in f:
            if old_line in line:
                print(line +  new_line, end='\n')
            else:
                print(line, end='')


def create_app(project, app):
    os.chdir(project)
    os.system(f'python manage.py startapp {app}')
    add_after(f'{project}/settings.py', 'INSTALLED_APPS', f"    '{app}',")
    add_after(f'{project}/urls.py', 'from django.urls', 'from django.urls import include')
    add_after(
        f'{project}/urls.py',
        'urlpatterns = [',
        f"    path('', include('{app}.urls')),")
    
    os.system(f'cp -R ../crear/templates {app}/templates')
    os.system(f'cp -R ../crear/static {app}/static')
    os.system(f'cp ../crear/views.py {app}/views.py')
    os.system(f'cp ../crear/auth.py {app}/auth.py')
    os.system(f'cp ../crear/decorators.py {app}/decorators.py')
    os.system(f'cp ../crear/models.py {app}/models.py')
    os.system(f'cp ../crear/urls.py {app}/urls.py')
    os.system(f'cp ../crear/gitignore .gitignore')


def main():
    if len(sys.argv) < 3:
        print('Usage error')
        sys.exit()
    project = sys.argv[1]
    app = sys.argv[2]
    if not os.path.exists(project):
        os.system(f'django-admin startproject {project}')

    create_app(project, app)


if __name__ == '__main__':
    main()
