__author__ = 'lei'


# #############################
#root for opds server website
#SITE_URL = "http://192.168.1.104:5000"
SITE_URL = "http://opds.cockybook.com"
SITE_TITLE = "Opds CockyBook"
SITE_EMAIL = "yinlei212@gmail.com"
SITE_BOOK_LIST = SITE_URL + "/list"

#download URL is SITE_BOOK_DONWLOAD/$path/$filename.$postfix
SITE_BOOK_DONWLOAD = 'http://7sbqcs.com1.z0.glb.clouddn.com'

#for local filesyste
base = "f:\\opds"

# Used In opdscore.py
#filesyste_type='LocalFileSystem'
#filesyste_type = 'QiniuFileSystem'
filesyste_type = 'LocalMetadataFileSystem'
