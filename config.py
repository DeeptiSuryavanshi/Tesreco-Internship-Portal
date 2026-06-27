import logging

logging.basicConfig(
    filename="tesreco.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logging.info("User Manju logged in")

try:
    result = 10 / 0
except Exception as e:
    logging.error(f"Error: {e}")

logging.info("Performance report generated for Manju")