class Config:
    SECRET_KEY = 'RzNS7DoWxtNWb7saVM8aiUjrtqduaYfVkXL'#SECRET_KEY = (os.environ['SECRET_KEY'])
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USERNAME = 'factorstockpicking@gmail.com'
    MAIL_PASSWORD = 'mqnjlytmeasatghy'#MAIL_PASSWORD = (os.environ['MAIL_PASSWORD'])
    MAIL_USE_SSL = True
   

    UPLOAD_FOLDER = "flaskblog/upload_folder"
    ALLOWED_EXTENSIONS = {'txt', 'pkl'}



    
#AAAAAAAAAAAAAAAAAAAAAAXvawEAAAAADXG8hdvFabfj6NqMB5VoOYsnv%2B4%3D6V0ntRJVLDSJUsIXqKwSHvXtjPP1Y18bLAIJ4DKeYKqc5PWvPk