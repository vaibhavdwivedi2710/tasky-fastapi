from mongoengine import connect
import logging

from app_secrets import TASKY_MONGODB_URI

def connect_to_mongo():
    """
    Connect to MongoDB using the URI from app_secrets.
    """
    try:
        connect(
            host=TASKY_MONGODB_URI,
            authentication_source='admin',
            authentication_mechanism='SCRAM-SHA-1'
        )
        logging.info("------- MongoDB connection successful -------")
    except Exception as e:
        logging.error(f"Failed to connect to MongoDB: {str(e)}")
        raise