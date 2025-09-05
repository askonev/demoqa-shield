# demoqa_shield

<https://demoqa.com/>

A test automation project using py playwright.

## Installation (linux)

```bash
# For pyproject.toml via uv
uv venv
uv pip compile pyproject.toml -o requirements.txt
uv pip install -r requirements.txt
```

```bash
# For requirements.txt
uv venv .venv
uv pip install -r requirements.txt
```

```bash
source .venv/bin/activate
# invoke lib
inv --list
```

### playwright

```bash
playwright install
```

## Author

Maksim.Sorokin
<askonev007@gmail.com>
