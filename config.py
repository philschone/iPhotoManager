### iPhonePhoto Manager ###

#
# this little skript converts, deletes, renames files and images
# that were copied from an iphone.
# it recursively loops through a given directory
# the user can configure:
# - perform a backup
# - convert images to png or jpg
# - delete or keep the original image.
# - rename or delete hdr images
# - delete aae image-info files
#
# Credits to Phil
# License MIT
#


### options ###

# root directory of the images
# all files in this dir and subdirs will be processed recursively
# double backslash. example: "C:\\temp\\abc"
path = "C:\\temp\\n"

# perform a backup of the files and dirs in the root path\_bkp?
backup = True
# overwrite the existing backup?
# options: ask (a), overwrite (o), skip (s)
overwrite_backup = 's'


# convert heic images?
convert_heic = True
# options: png, jpg, jpeg
heic_output_format = 'png'
# delete original heic?
delete_heic = True

# rename special iphone images (HDR??)?
# the e is positioned in a way, that the HDR images are all at the end.
# renaming them sorts them next to the normal image
rename_e = True
# delete original image?
delete_e = False

# delete aae files?
# these are info files that the iphone generates
delete_aae = True
