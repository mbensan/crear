import pdb
import sys
import os
import fileinput
import json


def add_after(filename, old_line, new_line):
    with fileinput.FileInput(filename, inplace=True, backup = '.bak') as f:
        for line in f:
            if old_line in line:
                print(line +  new_line, end='\n')
            else:
                print(line, end='')

databases_str = '''DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'PROJECT',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}'''

def change_settings(project, app):
    f = open(f'{project}/settings.py', 'a')
    f.write('\n')
    f.write(databases_str.replace('PROJECT', project))
    f.write('\n')
    f.write("LOGIN_REDIRECT_URL = '/'")
    f.write('\n')
    f.write("LOGOUT_REDIRECT_URL = '/accounts/login'")
    f.write('\n')
    f.close()



def create_app(project, app):
    os.chdir(project)
    
    os.system(f'python manage.py startapp {app}')
    add_after(f'{project}/settings.py', 'INSTALLED_APPS', f"    '{app}',")

    change_settings(project, app)

    os.system(f'cp -R ../crear/templates {app}/templates')
    os.system(f'cp -R ../crear/static {app}/static')
    os.system(f'cp ../crear/views.py {app}/views.py')
    os.system(f'cp ../crear/admin.py {app}/admin.py')
    os.system(f'cp ../crear/models.py {app}/models.py')
    os.system(f'cp ../crear/forms.py {app}/forms.py')
    os.system(f'cp ../crear/urls.py {project}/urls.py')
    os.system(f'cp ../crear/gitignore .gitignore')

    os.system(f'rm -rf {project}/*.bak')


def main():
    if len(sys.argv) < 2:
        print('Usage error')
        sys.exit()
    project = sys.argv[1]
    # app = sys.argv[2]
    if not os.path.exists(project):
        os.system(f'django-admin startproject {project}')

    # create_app(project, app)
    create_app(project, 'main')

if __name__ == '__main__':
    main()
