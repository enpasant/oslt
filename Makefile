# Variables
PYTHON = python3
VENV = venv
SRC = src
BIN_DIR = $(PREFIX)/bin

# Default rule: Run the main Python script
run:
	$(PYTHON) $(SRC)/oslt.py
	@echo "oslt Done!"

# Create a virtual environment
venv:
	$(PYTHON) -m venv $(VENV)
	@echo "Virtual environment created in $(VENV)/"

# Install dependencies in the virtual environment
install: venv
	$(VENV)/bin/pip install -r $(SRC)/make/requirements.txt
	@echo "Dependencies installed."

# Clean up temporary files
clean:
	rm -rf $(VENV)
	find . -name "__pycache__" -exec rm -rf {} +

# Package the application
package: install
	@echo "Packaging oslt..."
	@mkdir -p package/DEBIAN
	@chmod 0755 package/DEBIAN
	@echo "Package: oslt" > package/DEBIAN/control
	@echo "Version: 1.0" >> package/DEBIAN/control
	@echo "Architecture: all" >> package/DEBIAN/control
	@echo "Maintainer: enpasant" >> package/DEBIAN/control
	@echo "Description: CLI (Command Line Interface) language translator utility" >> package/DEBIAN/control
	@mkdir -p package$(BIN_DIR)
	@cp $(SRC)/oslt.py package$(BIN_DIR)/oslt
	@chmod +x package$(BIN_DIR)/oslt  # Ensure it's executable
	@dpkg-deb --build package
	@mv package.deb oslt_1.0.deb
	@rm -rf package
	@echo "oslt packaged as oslt_1.0.deb"
	@rm -rf ./venv/
.PHONY: run venv install clean package
