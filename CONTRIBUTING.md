# Contributing to Mario built with Pygame

Thank you for your interest in contributing to Mario built with Pygame! Here are
some guidelines to help you get started.

## How to Report Bugs

If you find a bug, please open an issue on GitHub and include:

- A clear and descriptive title.
- Steps to reproduce the bug.
- Expected and actual behavior.
- Any relevant screenshots or log files.

## Getting Started

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/)
- [node.js](https://nodejs.org/en/)
- [pnpm](https://pnpm.io/)

### Installation

1. Clone the repository to your local machine.

   ```bash
   git clone https://github.com/MorveN11/mario-pygame.git
   cd mario-pygame
   ```

2. Create a virtual environment named "venv" using the following command:

   ```bash
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS and Linux:

     ```bash
     source venv/bin/activate
     ```

4. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   pip install -r dev-requirements.txt
   ```

With these steps, you'll have a virtual environment set up and all project
dependencies installed, ready for isolated development.

### Setting Up Pyright for Static Type Checking

Pyright is a static type checker for Python that can help you catch errors to
improve code quality. To set it up, follow these steps:

- On Visual Studio Code:

  1. Install all the recommended extensions for the project
     `.vscode/extensions.json`.

- On PyCharm:

  1. Go to `File` > `Settings` > `Plugins` and search for "Pyright".
  2. Install the plugin and restart the IDE.

### Setting Up Black for Code Formatting

Black is a code formatter for Python that can help you maintain a consistent and
readable code style. To set it up, follow these steps:

- On Visual Studio Code:

  1. Install all the recommended extensions for the project
     `.vscode/extensions.json`.

- On PyCharm:

  1. Go to `File` > `Settings` > `Plugins` and search for "Black".
  2. Install the plugin and restart the IDE.

## Testing

- Run the test suite with the following command:

  ```bash
  pytest
  ```

- Add new tests to cover the changes you make.

## Running the Game

Run the game with the following command:

```bash
./run.sh
```

## Development Guidelines

- Follow the coding style and conventions outlined in the
  [documentation](docs/conventions.md).
- Write clear and concise commit messages following the
  [commit convention](docs/commit-convention.md).
- Make sure your code is well-documented.

## License

By contributing to Mario built with Pygame, you agree that your contributions
will be licensed under its [MIT License](LICENSE).

## Additional Resources

- [Project Documentation](https://tree.taiga.io/project/denis-gandel-puro-piton/wiki/home)
- [Pygame Documentation](https://www.pygame.org/docs/)

Thank you for your interest in contributing to Mario built with Pygame! We look
forward to your contributions.
