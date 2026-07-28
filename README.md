# AlphaNumerical Password Generator

**Version:** 1.0.0

A lightweight Python command-line utility for generating secure random passwords.

## Features

- Generate passwords of a custom length
- Supports uppercase and lowercase letters
- Supports numbers
- Optional punctuation
- Colorized terminal output
- ASCII banner
- `--help` command
- `--version` command
- Saves the generated password to `Password.txt`

## Requirements

- Python 3.x

## Usage

Clone the repository or download the source.

```bash
py Password_Generator.py
```

### Examples

Generate a default password:

```bash
py Password_Generator.py
```

Generate a 20-character password:

```bash
py Password_Generator.py -length 20
```

Generate a 20-character password with punctuation:

```bash
py Password_Generator.py -anp -length 20
```

Show help:

```bash
py Password_Generator.py --help
```

Show version:

```bash
py Password_Generator.py --version
```

The generated password is displayed in the terminal and saved to `Password.txt`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.