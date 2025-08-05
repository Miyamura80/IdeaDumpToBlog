from global_config import global_config
from src.utils.logging_config import setup_logging
from loguru import logger
import json

setup_logging()


def main():
    logger.info("Global config: {}", json.dumps(global_config.to_dict(), indent=2, default=lambda o: o.__dict__))
    logger.info("Model name: {}", global_config.model_name)
    logger.info("Default LLM config: {}", json.dumps(global_config.default_llm, indent=2, default=lambda o: o.__dict__))


if __name__ == "__main__":
    main()
