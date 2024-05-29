# HexaHack CLI Tool

HexaHack CLI is a command line interface tool designed to interact with the HexaCore API. This tool allows users to perform various operations such as creating an account, checking available taps, mining taps, and retrieving the balance. The interface is user-friendly and provides colored outputs for better readability.

## Features

- **Create Account**: Create a new user account with a specified referer ID.
- **Available Taps**: Check the number of available taps for a user.
- **Mine All**: Execute mining for all available taps for a user.
- **Get Balance**: Retrieve the balance of a user.
- **User-Friendly Interface**: Interactive and color-coded command line interface.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/hexahack-cli.git
   cd hexahack-cli
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage

Run the HexaHack CLI tool:
```sh
python hexahack.py
```

### Commands

- **create_account fullname referer_id**
  - Create a new user account with the specified referer ID.
  
- **available_taps**
  - Check the number of available taps for the user.
  
- **mine_all**
  - Execute mining for all available taps for the user.
  
- **get_balance**
  - Retrieve the balance of the user.
  
- **exit**
  - Exit the command line interface.

### Example

```sh
Welcome to the HexaHack command line interface. Type help or ? to list commands.

(hexahack) create_account "John Doe" 123
Account creation successful

(hexahack) available_taps
Available taps: 5

(hexahack) mine_all
Mining successful

(hexahack) get_balance
Balance: 50.0

(hexahack) exit
Exiting HexaHack CLI
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.
