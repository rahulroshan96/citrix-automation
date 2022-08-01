python -m venv venv
project_dir=$(pwd)
$project_dir/venv/bin/pip install -r req.txt
cd nitro-python/
$project_dir/venv/bin/python setup.py install