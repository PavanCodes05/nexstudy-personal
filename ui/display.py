import os
from config import DOCS_PATH
from utils.logger import logger
import questionary

def get_role():
    """Prompt user to select a role."""
    try:
        role = questionary.select(
            "Select Your Role:",
            choices=["Student", "Faculty"]
        ).ask()

        if not role:
            logger.warning("User cancelled role selection.")
            return None
        return role

    except KeyboardInterrupt:
        logger.info("User interrupted during role selection.")
        return None

    except Exception as e:
        logger.error(f"Unexpected error during role selection: {e}")
        return None


def get_material_info():
    """Prompt user for year, subject, and material information."""
    try:
        year = questionary.select(
            "Select The Year:",
            choices=["I", "II", "III"]
        ).ask()
        if not year:
            logger.warning("User cancelled year selection.")
            return None

        subject = questionary.select(
            "Select The Subject:",
            choices=["Physics", "PSPP", "Maths"]
        ).ask()
        if not subject:
            logger.warning("User cancelled subject selection.")
            return None

        material = questionary.select(
            "Select The Material:",
            choices=["python_notes.pdf", "Notes.pdf"]
        ).ask()
        if not material:
            logger.warning("User cancelled material selection.")
            return None

        return (year, subject, material)

    except KeyboardInterrupt:
        logger.info("User interrupted during material selection.")
        return None

    except Exception as e:
        logger.error(f"Unexpected error during material info retrieval: {e}")
        return None


def run_question_prompts():
    """Main function to handle user prompts and build material path."""
    try:
        role = get_role()
        if not role:
            logger.info("Role selection aborted.")
            return None

        material_info = get_material_info()
        if not material_info:
            logger.info("Material info selection aborted.")
            return None

        year, subject, material = material_info

        # Build material path
        material_path = os.path.join(DOCS_PATH, year, subject, material)

        # Validate file existence
        if not os.path.exists(material_path):
            logger.error(f"Material not found: {material_path}")
            return None

        logger.info(f"Material Path: {material_path}")
        return material_path

    except KeyboardInterrupt:
        logger.info("User interrupted the process.")
        return None

    except Exception as e:
        logger.error(f"Unexpected error in run_question_prompts: {e}")
        return None

