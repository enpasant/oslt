#!/usr/bin/env python3

import sys
import argparse
from googletrans import Translator
from rich.console import Console
from rich.text import Text

# Initialize rich Console
console = Console()

def print_usage():
    console.print("Usage: oslt [options] \"source language\" to \"target language\"", style="bold green")
    console.print("Options:", style="bold yellow")
    console.print("  -h, --help         Show this help message and exit.", style="cyan")
    console.print("  -i, --input <text> Specify the text to translate.", style="cyan")
    console.print("  -o, --output       Display output of translation.", style="cyan")
    console.print("\nExample:", style="bold yellow")
    console.print("  oslt -i \"Hello, world!\" English to Spanish", style="green")

def translate(text, source_lang, target_lang):
    """
    Perform translation using googletrans API.
    """
    translator = Translator()

    try:
        # Translate text using googletrans
        result = translator.translate(text, src=source_lang, dest=target_lang)
        # Print with rich text formatting
        source_text = Text(f"[{source_lang}] {text}", style="bold blue")
        target_text = Text(f"→ [{target_lang}] {result.text}", style="bold green")
        
        console.print(source_text)
        console.print(target_text)
    except Exception as e:
        console.print(f"[bold red]Error: Unable to translate.[/]\nDetails: {e}", style="bold red")

def main():
    parser = argparse.ArgumentParser(
        description="OSLT: Open Source Language Translate",
        usage="oslt [options] \"source language\" to \"target language\""
    )

    parser.add_argument(
        "-i", "--input",
        type=str,
        required=True,
        help="The text to translate."
    )
    parser.add_argument(
        "source_language",
        type=str,
        help="The source language for translation (e.g., English)."
    )
    parser.add_argument(
        "to",
        type=str,
        help="Keyword 'to' separating source and target languages.",
        choices=["to"]
    )
    parser.add_argument(
        "target_language",
        type=str,
        help="The target language for translation (e.g., Spanish)."
    )
    parser.add_argument(
        "-o", "--output",
        action="store_true",
        help="Display the output of the translation."
    )

    args = parser.parse_args()

    # Process arguments
    source_lang = args.source_language
    target_lang = args.target_language
    text = args.input

    # Perform translation
    translate(text, source_lang, target_lang)

    # Output option
    if args.output:
        console.print("\n[bold green]Translation completed successfully![/]")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print_usage()
        sys.exit(1)
    main()
