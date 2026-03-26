from setuptools import setup
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="flask-swagger-ui",
    version="5.21.0",
    description="Swagger UI blueprint for Flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    zip_safe=False,
    url="https://github.com/sveint/flask-swagger-ui",
    author="Svein Tore Koksrud Seljebotn",
    author_email="sveint@gmail.com",
    license="MIT",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
    keywords="flask swagger",
    packages=["flask_swagger_ui"],
    install_requires=["flask"],
    package_data={
        "flask_swagger_ui": [
            "LICENSE",
            "README.md",
            "templates/*.html",
            "dist/VERSION",
            "dist/LICENSE",
            "dist/README.md",
            "dist/*.html",
            "dist/*.js",
            "dist/*.css",
            "dist/*.png",
        ]
    },
)
