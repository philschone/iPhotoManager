
from modules.job import ConvertJob
import config as cfg


def main():
    options = {'path': cfg.path,
               'backup': cfg.backup,
               'overwrite_backup': cfg.overwrite_backup,
               'convert_heic': cfg.convert_heic,
               'heic_output_format': cfg.heic_output_format,
               'delete_heic': cfg.delete_heic,
               'rename_e': cfg.rename_e,
               'delete_e': cfg.delete_e,
               'delete_aae': cfg.delete_aae}

    ConvertJob(options).run()


if __name__ == '__main__':
    main()
