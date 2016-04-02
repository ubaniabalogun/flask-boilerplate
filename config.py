"""
Configuration Class
"""

class Config(object):
    """
    Base configuration class
    """
    pass

class DevConfig(Config):
    """
    Development Configurations
    """
    DEBUG = True

class ProdConfig(Config):
    """
    Production Configurations
    """
    DEBUG = False
