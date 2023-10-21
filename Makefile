# Display python command-line utility versions
python_install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

python_test:
	python -m pytest -vv --cov=main --cov=mylib test_*.py

python_format:
	black *.py 

python_lint:
	# Disable comment to test speed
	# pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py
	# ruff linting is 10-100X faster than pylint
	ruff check *.py mylib/*.py

python_deploy:
	# deploy goes here

python_all: python_install python_lint python_test python_format

python_extract:
	python main.py extract

python_transform_load:
	python main.py transform_load

python_create:
	python main.py general_query "INSERT INTO AirlineSafetyDB (airline, avail_seat_km_per_week, incidents_85_99, fatal_accidents_85_99, fatalities_85_99, incidents_00_14, fatal_accidents_00_14, fatalities_00_14) VALUES ('Happy Airlines', 965346770, 1, 1, 1, 1, 1, 1);"

python_read:
	python main.py general_query "SELECT * FROM AirlineSafetyDB WHERE airline = 'Happy Airlines';"

python_update:
	python main.py general_query "UPDATE AirlineSafetyDB SET airline='Happy Airlines', avail_seat_km_per_week=965346770, incidents_85_99=0, fatal_accidents_85_99=0, fatalities_85_99=0, incidents_00_14=0, fatal_accidents_00_14=0, fatalities_00_14=0 WHERE id=57;"

python_delete:
	python main.py general_query "DELETE FROM AirlineSafetyDB WHERE id=57;"

# Display Rust command-line utility versions
rust-version:
	@echo "Rust command-line utility versions:"
	rustc --version              # Rust compiler
	cargo --version              # Rust package manager
	rustfmt --version            # Rust code formatter
	rustup --version             # Rust toolchain manager
	clippy-driver --version      # Rust linter

format:
	cargo fmt --quiet

lint:
	cargo clippy --quiet

test:
	cargo test --quiet

run:
	cargo run

release:
	cargo build --release

install:
	# Install if needed
	# @echo "Updating rust toolchain"
	# rustup update stable
	# rustup default stable

all: format lint test run

extract:
	cargo run extract

transform_load:
	cargo run transform_load

create:
	cargo run query "INSERT INTO AirlineSafetyDB (airline, avail_seat_km_per_week, incidents_85_99, fatal_accidents_85_99, fatalities_85_99, incidents_00_14, fatal_accidents_00_14, fatalities_00_14) VALUES ('Happy Airlines', 965346770, 1, 1, 1, 1, 1, 1);"

read:
	cargo run query "SELECT * FROM AirlineSafetyDB WHERE airline = 'Happy Airlines';"

update:
	cargo run query "UPDATE AirlineSafetyDB SET airline='Happy Airlines', avail_seat_km_per_week=965346770, incidents_85_99=0, fatal_accidents_85_99=0, fatalities_85_99=0, incidents_00_14=0, fatal_accidents_00_14=0, fatalities_00_14=0 WHERE id=57;"

delete:
	cargo run query "DELETE FROM AirlineSafetyDB WHERE id=57;"

generate_and_push:
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "action@github.com"; \
		git config --local user.name "GitHub Action"; \
		git add .; \
		git commit -m "Add query log"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi
