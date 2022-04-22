###mysql
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'learn_platform'
USERNAME = 'root'
PASSWORD = '7ujm8ik,'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME,PASSWORD,HOSTNAME,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI  #使用链接地址，可用于创建数据库引擎
SQLALCHEMY_TRACK_MODIFICATIONS = True    #
SECRET_KEY = ''

###email
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT =465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = 'duanyunpeng.nm@foxmail.com'
MAIL_PASSWORD = ''
MAIL_DEFAULT_SENDER = 'duanyunpeng.nm@foxmail.com'
