.PHONY: test test-cov

TAG="\033[0;32m\#\#\# "
END=" \#\#\# \033[0m\n"

run:
	@echo $(TAG)Executing main.py:$(END)
	@PYTHONPATH=. python list_of_prime_numbers/main.py

test:
	@echo $(TAG)Running tests$(END)
	PYTHONPATH=. py.test tests

test-cov:
	@echo $(TAG)Running tests with coverage$(END)
	PYTHONPATH=. py.test --cov=list_of_prime_numbers tests

coverage:
	@echo $(TAG)Coverage report$(END)
	@PYTHONPATH=. coverage run --source=list_of_prime_numbers $(shell which py.test) ./tests -q --tb=no >/dev/null; true
	@coverage report
