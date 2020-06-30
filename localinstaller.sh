pip uninstall openprov -y
rm build/ dist/ openprov.egg-info -rf
python setup.py sdist bdist_wheel
cd dist/
pip install *.whl
cd ../