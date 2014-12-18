__author__ = 'lei'


##############################
#root for opds server website
SITE_URL = "http://192.168.1.104:5000"
#SITE_URL = "http://10.10.113.237:5000"
SITE_TITLE = "CockyBook"
SITE_EMAIL = "yinlei212@gmail.com"
SITE_BOOK_LIST = SITE_URL + "/list"

SITE_BOOK_DONWLOAD = 'http://7sbqcs.com1.z0.glb.clouddn.com'

base = "f:\\opds"

#
#filesyste_type='LocalFileSystem'
filesyste_type='QiniuFileSystem'

#################


bucket_name='cockybook'

QiNiu_Book_types=['Noval', '\xb7\xf0\xd1\xa7', '\xd0\xc4\xc0\xed\xd1\xa7', '\xca\xfd\xd1\xa7', '\xbf\xc6\xbc\xbc', '\xc8\xed\xbf\xbc']


access_key='lMdYca_7_oS99RWHTKD2D0pCU7IJECckrMnFnKOH'
secret_key='jFUoC_h2Rv94Em6qiLnIuwXFOvGhvvRd-OVga-3D'