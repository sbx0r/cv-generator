# CV Generator

Generates CV from YAML file to PDF.

## Setup

```bash
# Install wkhtmltopdf
sudo apt-get install wkhtmltopdf  # Linux
brew install wkhtmltopdf          # macOS

# Run with uv
uv run main.py
```

## CV Data

- Edit: `cv_data.yaml`
- Example: `cv_data_example.yaml`

## Usage

```bash
# Basic
uv run main.py

# With parameters
uv run main.py -i my_cv.yaml -o resume_2024 --keep-html
```

Options:
- `-i` / `--input` - YAML file (default: cv_data.yaml)
- `-o` / `--output` - output name (default: cv)
- `--keep-html` - keep HTML file

PDF will appear in `output/`
