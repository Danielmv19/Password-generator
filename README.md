# Password Generator

## Description
This Python script generates secure random passwords based on user input. It allows users to specify the length of the password (between 6 and 22 characters) and choose between generating a single password or multiple (five) passwords. The passwords include a mix of digits, lowercase letters, uppercase letters, and special symbols for enhanced security.

The script uses the `questionary` library for an interactive command-line interface, `rich` for formatted console output, and Python's built-in `random`, `time`, and `string` modules for password generation.

![video](https://github.com/Danielmv19/Password-generator/blob/main/recording.gif)


## Features
- Generate a single password or five passwords at once.
- Customizable password length (6 to 22 characters).
- Includes digits, lowercase, uppercase, and special symbols (`#$%&?@^_!`).
- Interactive CLI with validation for user inputs.
- Option to continue generating passwords in a loop.
- Rich console output with Markdown formatting for a better user experience.

## Requirements
- Python 3.6+
- Required libraries:
  - `questionary`
  - `rich`

Install the dependencies using:
```bash
pip install questionary rich
```

## Usage
1. Clone the repository.
2. Install the required libraries (see above).
3. Run the script:
   ```bash
   python main.py
   ```
4. Follow the prompts:
   - Select whether to generate a single password or five passwords.
   - Enter the desired password length (6–22 characters).
   - View the generated password(s).
   - Choose to continue generating more passwords or exit.
`

## Code Structure
- `pass_generator(longitud)`: Generates a random password of specified length using digits, lowercase, uppercase, and special symbols.
- `long_validator(_)`: Validates that the password length is between 6 and 22.
- `long_q()`: Prompts the user for password length with validation.
- `run()`: Handles the main logic for generating one or five passwords based on user input.
- Main loop: Allows users to generate more passwords until they choose to exit.
