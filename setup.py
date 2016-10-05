from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='flask-swagger-ui',
    version='0.0.1',
    description='SwaggerUI blueprint for Flask',
    long_description=long_description,

    url='https://github.com/sveint/flask-swagger-ui',

    author='Svein Tore Koksrud Seljebotn',
    author_email='sveint@gmail.com',
    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',

        'Intended Audience :: Developers',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='flask swagger',
    packages=['flask_swagger_ui'],

    package_data={
        'flask_swagger_ui': [
            'README.md',
            'templates/*.html',
            'dist/VERSION',
            'dist/LICENSE',
            'dist/README.md',
            'dist/*.html',
            'dist/*.js',
            'dist/*/*.js',
            'dist/*/*.css',
            'dist/*/*.gif',
            'dist/*/*.png',
            'dist/*/*.ico',
            'dist/*/*.ttf',
        ],
    }
)
