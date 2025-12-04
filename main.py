#!/usr/bin/env python3
from jinja2 import Environment, FileSystemLoader
import pdfkit
import yaml
import os
import sys


def load_cv_data(filename="cv_data.yaml"):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        print(f"✅ Loaded data from {filename}")
        return data
    except FileNotFoundError:
        print(f"❌ Error: File '{filename}' not found")
        print("   Make sure cv_data.yaml exists in the current directory")
        sys.exit(1)
    except yaml.YAMLError as e:
        print(f"❌ Error parsing YAML file: {e}")
        sys.exit(1)


def generate_cv(data_file="cv_data.yaml", output_name="cv"):
    data = load_cv_data(data_file)
    env = Environment(loader=FileSystemLoader('.'))

    try:
        template = env.get_template('cv_template.html')
    except Exception as e:
        print(f"❌ Error loading template: {e}")
        sys.exit(1)

    print("📝 Rendering HTML template...")
    html_content = template.render(data)
    html_file = f"{output_name}.html"
    with open(html_file, "w", encoding='utf-8') as f:
        f.write(html_content)
    print(f"✅ HTML saved to {html_file}")

    output_dir = "output"
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, f"{output_name}.pdf")

    print("🎨 Converting to PDF...")
    try:
        pdfkit.from_string(html_content, output_path, css='style.css')
        print(f"✅ CV generated successfully at {output_path}")

        pdf_size = os.path.getsize(output_path)
        print(f"\n📊 Generated PDF: {pdf_size:,} bytes")

    except Exception as e:
        print(f"❌ Error generating PDF: {e}")
        print("\nMake sure wkhtmltopdf is installed:")
        print("  Ubuntu/Debian: sudo apt-get install wkhtmltopdf")
        print("  macOS: brew install wkhtmltopdf")
        print("  Windows: Download from https://wkhtmltopdf.org/downloads.html")
        sys.exit(1)


def main():
    import argparse

    parser = argparse.ArgumentParser(description='Generate CV from YAML data')
    parser.add_argument(
        '-i', '--input',
        default='cv_data.yaml',
        help='Input YAML file (default: cv_data.yaml)'
    )
    parser.add_argument(
        '-o', '--output',
        default='cv',
        help='Output filename without extension (default: cv)'
    )
    parser.add_argument(
        '--keep-html',
        action='store_true',
        help='Keep the intermediate HTML file'
    )

    args = parser.parse_args()

    generate_cv(args.input, args.output)

    if not args.keep_html:
        html_file = f"{args.output}.html"
        if os.path.exists(html_file):
            os.remove(html_file)
            print(f"🧹 Cleaned up {html_file}")


if __name__ == "__main__":
    main()
