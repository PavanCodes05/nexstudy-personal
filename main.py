from ui.display import run_question_prompts
from utils.logger import logger
from core.pdf_handler import read_entire_pdf
from core.llm_handler import llm_call
from core.md_handler import save_to_markdown

role, doc_path, question = run_question_prompts()
if doc_path:
    logger.info("Path received succesfully!")

pdf = read_entire_pdf(doc_path)
llm_response = llm_call(role, pdf, question)

save_to_markdown(llm_response.choices[0].message.content, "PSPP", "notes")
