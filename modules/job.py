import os
import shutil

from PIL import Image
from pillow_heif import register_heif_opener


class ConvertJob():
    def __init__(self, options: dict):
        self.version = '1.0'

        # job options
        self.path = options['path']
        self.backup = options['backup']
        self.overwrite_backup = options['overwrite_backup']
        self.convert_heic = options['convert_heic']
        self.heic_output_format = options['heic_output_format']
        self.delete_heic = options['delete_heic']
        self.rename_e = options['rename_e']
        self.delete_e = False if options['rename_e'] else options['delete_e']
        self.delete_aae = options['delete_aae']

        self.backup_dir = '_bkp'

        print('\t### Welcome to iPhonePhotoManager ###')
        print(f'\t ##     Version {self.version}    ##')
        print('\t  #        Created by Phil        #')

    def run(self):
        self.runBackup()
        if self.convert_heic:
            self.runHEICConvert()
        if self.rename_e:
            self.runRenameE()
        if self.delete_e:
            self.runDeleteE()
        if self.delete_aae:
            self.runDeleteAAE()


    def runBackup(self):
        if self.backup:
            bkp_path = os.path.join(self.path, self.backup_dir)
            while True:
                try:
                    shutil.copytree(self.path, bkp_path)
                    print(f'Backup saved:\t{bkp_path}')
                except FileExistsError:
                    if self.overwrite_backup.lower() not in ['s', 'o']:
                        self.overwrite_backup = 'o' if input('Backup already exists! Overwrite? y/n : ').lower() in ['j', 'y'] else 's'  # o overwrite, s skip
                    if self.overwrite_backup.lower() == 'o':
                        shutil.rmtree(bkp_path)
                        print(f'Backup   Deleted:\t{bkp_path}')
                        continue
                    print('Backup skipped')
                break
        else:
            print('Backup inactive!')

    def runHEICConvert(self):
        # register a Pillow plugin for HEIF format
        register_heif_opener()
        for root, dirs, files in os.walk(self.path): # pylint: disable=W0612
            for file in files:
                filepath = os.path.join(root, file)
                name, sep, ext = file.lower().rpartition('.')
                new_filename = name + sep + self.heic_output_format
                new_filepath = os.path.join(root, new_filename)

                if self.convert_heic and ext == 'heic' and not os.path.exists(new_filepath):
                    img = Image.open(filepath)
                    img.save(new_filepath)
                    print(f'Converted:\t{filepath}\n       to:\t{new_filepath}')
                    if self.delete_heic and self.backup_dir not in filepath:
                        os.remove(filepath)
                        print(f'  Deleted:\t{filepath}')

    def runRenameE(self):
        for root, dirs, files in os.walk(self.path): # pylint: disable=W0612
            for file in files:
                filepath = os.path.join(root, file)
                name, sep, ext = file.lower().rpartition('.')

                if self.rename_e and 'e' in name and self.backup_dir not in filepath:
                    new_filename = name.split('e')[0] + name.split('e')[1] + 'e' + sep + ext
                    new_filepath = os.path.join(root, new_filename)
                    os.rename(filepath, new_filepath)
                    print(f'Renamed:\t{filepath}\n\tto\t{new_filepath}')

    def runDeleteE(self):
        for root, dirs, files in os.walk(self.path): # pylint: disable=W0612
            for file in files:
                filepath = os.path.join(root, file)
                name = file.lower().rpartition('.')[0]

                if self.delete_e and 'e' in name and self.backup_dir not in filepath:
                    os.remove(filepath)
                    print(f'  Deleted:\t{filepath}')

    def runDeleteAAE(self):
        for root, dirs, files in os.walk(self.path): # pylint: disable=W0612
            for file in files:
                filepath = os.path.join(root, file)
                ext = file.lower().rpartition('.')[2]

                if self.delete_aae and ext == 'aae' and self.backup_dir not in filepath:
                    os.remove(filepath)
                    print(f'  Deleted:\t{filepath}')
