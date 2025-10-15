from ui.display import run_question_prompts
from utils.logger import logger

doc = run_question_prompts()
if doc:
    logger.info("Path received succesfully!")
