class Config(object):
    """
    Konfigurasi Umum
    """

    DEBUG = True
    # Taruh konfigurasi umum untuk semua envs di sini

class DevelopmentConfig(Config):
    """
    Konfigurasi Development
    """

    # DEBUG = True
    SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
    """
    Konfigurasi Produksi
    """

    DEBUG = False

class TestingConfig(Config):
    """
    Konfigurasi Testing
    """
    TESTING = True

app_config = {
    'development' : DevelopmentConfig,
    'production' : ProductionConfig,
    'testing': TestingConfig
}
