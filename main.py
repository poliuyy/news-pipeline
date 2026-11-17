import logging
import os

from extract import run_extract
from transform import run_transform
from load import run_load

os.makedirs("data", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler("data/pipeline.log", encoding="utf-8"),
        logging.StreamHandler(),
    ],
)

logger = logging.getLogger("main")

def main():
    logger.info("===Extract===")
    if not run_extract():
        logger.info("Пайплайн остановлен: нет данных")
        return

    logger.info("===Transform===")
    run_transform()

    logger.info("===Load===")
    run_load()

if __name__ == "__main__":
    main()