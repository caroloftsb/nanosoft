import os
import shutil
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(filename='nanosoft.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Configuration
SOURCE_DIRECTORIES = [
    # Add directories you want to back up
    'C:\\Users\\YourUsername\\Documents',
    'C:\\Users\\YourUsername\\Pictures'
]

BACKUP_DIRECTORY = 'D:\\Backup'
BACKUP_INTERVAL = 60 * 60 * 24  # 24 hours in seconds

def create_backup(source, destination):
    try:
        if not os.path.exists(destination):
            os.makedirs(destination)
        backup_name = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_path = os.path.join(destination, backup_name)
        shutil.copytree(source, backup_path)
        logging.info(f"Backup created for {source} at {backup_path}")
    except Exception as e:
        logging.error(f"Error creating backup for {source}: {e}")

def main():
    logging.info("NanoSoft Backup Service Started.")
    while True:
        for source_directory in SOURCE_DIRECTORIES:
            if os.path.exists(source_directory):
                create_backup(source_directory, BACKUP_DIRECTORY)
            else:
                logging.warning(f"Source directory does not exist: {source_directory}")
        time.sleep(BACKUP_INTERVAL)

if __name__ == '__main__':
    main()