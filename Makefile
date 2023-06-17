##
# Makefile
#

fix-style:
	isort --profile black treasury_prime_py
	black treasury_prime_py
	flakeheaven lint
