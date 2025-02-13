# NanoSoft

NanoSoft is a simple Python-based program designed to automatically create backup copies of important files and folders on Windows. It ensures your data is safely stored by periodically copying specified directories to a backup location.

## Features

- Automatically creates backups of specified directories.
- Configurable backup intervals.
- Logs backup activities and errors.

## Requirements

- Python 3.x
- Windows OS

## Installation

1. Clone this repository or download the `nanosoft.py` file.
2. Ensure you have Python 3.x installed on your system.

## Usage

1. Edit the `nanosoft.py` file to specify the directories you want to back up in the `SOURCE_DIRECTORIES` list. For example:
   ```python
   SOURCE_DIRECTORIES = [
       'C:\\Users\\YourUsername\\Documents',
       'C:\\Users\\YourUsername\\Pictures'
   ]
   ```

2. Set the `BACKUP_DIRECTORY` to your desired backup location:
   ```python
   BACKUP_DIRECTORY = 'D:\\Backup'
   ```

3. Adjust the `BACKUP_INTERVAL` if needed. The default is set to 24 hours:
   ```python
   BACKUP_INTERVAL = 60 * 60 * 24  # 24 hours in seconds
   ```

4. Open a terminal and run the program:
   ```bash
   python nanosoft.py
   ```

5. The program will log its activities in `nanosoft.log`.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Disclaimer

This software is provided "as is", without warranty of any kind. Please ensure you have additional backup solutions in place for critical data.