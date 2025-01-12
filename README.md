# OSLT (Open Source Language Translate)

OSLT is a simple, open-source command-line tool that enables language translation between two specified languages. It is built using Python and the `googletrans` library, which interfaces with Google Translate to provide translations.

## Features

- Translate text from one language to another.
- Supports multiple languages using Google Translate.
- Command-line interface for easy use in any terminal.
- Written in Python with the `googletrans` and `rich` libraries for enhanced functionality and output formatting.

## Installation

### Option 1: Install via `.deb` Package (Recommended for Debian-based Systems)

1. Download the `.deb` package:

   - [Download oslt_1.0.deb](https://github.com/enpasant/oslt/releases/download/1.0/oslt_1.0.deb)

2. Install the `.deb` package using the `dpkg` command:

    ```bash
    sudo dpkg -i oslt_1.0.deb
    sudo apt-get install -f  # Fix any dependency issues
    ```

### Option 2: Manual Installation (Python-based)

If you prefer to install from the source, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/enpasant/oslt.git
    cd oslt
    ```

2. Install the required Python packages:

    ```bash
    pip install googletrans==4.0.0-rc1 rich
    ```

## Usage

OSLT operates via the command line, using the following syntax:

```bash
oslt -i "your text here" <source language> to <target language>
