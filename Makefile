test_all:
	python -m unittest discover -s ./ -p "*_test.py"
lint:
	pylint ./slib ./test main.py