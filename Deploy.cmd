REM Criar pasta do pacote PyPI 
REM Configurar setup.py
REM Criar README.rst e licence.txt
REM Criar Setup.cfg
REM Instalar twine: pip3 install twine

python setup.py --help-commands
python setup.py sdist
REM python setup.py bdist
python setup.py bdist_wheel
REM python setup.py register
twine upload dist/*