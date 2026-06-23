import logging

logging.basicConfig(
    filename='tesreco.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Login Successful")
logging.error("Database Error")