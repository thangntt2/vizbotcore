init:
    pip install -r requirements.txt

test:
    py.test test
.PHONY: init test