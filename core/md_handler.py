import os
from datetime import datetime

def save_to_markdown(content: str, subject: str, material: str) -> str:
    """
    Saves the AI-generated reply into a Markdown (.md) file.
    """
    # Ensure output directory exists
    output_dir = "outputs"
    os.makedirs(output_dir, exist_ok=True)

    # Generate timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    safe_subject = subject.replace(" ", "_").lower()
    safe_material = material.replace(" ", "_").lower()

    filename = f"{safe_subject}_{safe_material}_{timestamp}.md"
    filepath = os.path.join(output_dir, filename)

    # Create the markdown content
    header = f"# 📘 {subject} — {material}\n\n"
    header += f"🕒 *Generated on {datetime.now().strftime('%B %d, %Y at %H:%M:%S')}*\n\n"
    header += "---\n\n"

    # Write to file
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(header)
        f.write(content)

    print(f"\n✅ Output saved successfully at: {filepath}\n")
    return filepath

