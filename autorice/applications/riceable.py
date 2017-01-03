import os
import shutil


class Riceable:
    """
    Generic riceable application.
    """

    def __init__(self):
        self.app_name = ''
        self.home_directory = os.path.expanduser('~')
        # Should be a dict with paths as keys and lists of filenames in them as values
        self.files = {}

    # ToDo add logging
    def backup(self, backup_directory):
        """
        Copy and save user config to backup directory.
        :param backup_directory: Full path to the backup directory
        :type backup_directory: str
        :return: list of files that couldn't be backed up
        """
        failed = []
        for directory in self.files:
            path_to_backup_dir = os.path.join(backup_directory, directory)
            # Create the directory if it doesn't exist, don't raise if it does
            os.makedirs(path_to_backup_dir, exist_ok=True)
            for file in self.files[directory]:
                path_to_file = os.path.join(self.home_directory, directory, file)
                try:
                    shutil.copy(path_to_file, path_to_backup_dir)
                except IOError:
                    failed.append(path_to_file)
        return failed

    # ToDo add logging
    def restore(self, backup_directory):
        """
        Restore user config from backup directory.
        :param backup_directory: Path to the backup directory
        :type backup_directory: str
        :return: list of files that couldn't be restored
        """
        failed = []
        for directory in self.files:
            path_to_dir = os.path.join(self.home_directory, directory)
            # Create the directory if it doesn't exist, don't raise if it does
            os.makedirs(path_to_dir, exist_ok=True)
            for file in self.files[directory]:
                path_to_backed_up_file = os.path.join(backup_directory, file)
                try:
                    shutil.copy(path_to_backed_up_file, path_to_dir)
                except IOError:
                    failed.append(path_to_backed_up_file)
        return failed

    # TODO figure out the exact api of this
    def rice(self, rice_config):
        """
        Install a rice config. Should probably get some kinda 'Rice' class instance
        as param
        :param rice_config: Rice object defining the rice configuration
        :return:
        """
        raise NotImplementedError
