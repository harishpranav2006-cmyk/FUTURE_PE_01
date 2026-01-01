import os
import tkinter as tk
from tkinter import scrolledtext

TOPIC = "5 AI Tools That Can Replace a Full-Time Job (in 2025)"
OUTPUT_DIR = "outputs"

def ensure_dir():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

def save(name, content):
    with open(os.path.join(OUTPUT_DIR, name), "w", encoding="utf-8") as f:
        f.write(content)

def generate_titles():
    return [
        "5 AI Tools That Can Replace a Full-Time Job (in 2025)",
        "AI Tools That Can Replace Human Jobs",
        "Top AI Tools for Beginners in 2025",
        "How AI Is Replacing Jobs Faster Than Ever",
        "Best AI Tools to Learn in 2025"
    ]

def generate_script():
    script = f"""
INTRO:
Today we explore {TOPIC}.

AI tools are transforming how work is done.
They can write, design, code, and automate tasks.

SECTION:
These tools increase productivity and reduce manual effort.
Beginners can start with free versions and learn step by step.

CONCLUSION:
AI will not replace humans, but humans using AI will replace others.
Start learning today.
"""
    while len(script.split()) < 250:
        script += "\nAI tools help save time and increase efficiency."
    return script

def generate_thumbnail():
    return "AI TOOLS = JOBS? 😱", "Bold YouTube thumbnail, laptop, AI icons, dramatic lighting"

def prompt_chain():
    return """
Prompt Chain:
1. Generate video titles
2. Generate script
3. Generate thumbnail idea
4. Save outputs
"""

def show_popup(titles, script, thumb):
    win = tk.Tk()
    win.title("Task-1 Output")
    win.geometry("800x500")

    box = scrolledtext.ScrolledText(win, wrap=tk.WORD)
    box.pack(expand=True, fill="both")

    box.insert(tk.END, "TOP TITLES:\n")
    for t in titles:
        box.insert(tk.END, "- " + t + "\n")

    box.insert(tk.END, "\nTHUMBNAIL TEXT:\n" + thumb + "\n")
    box.insert(tk.END, "\nSCRIPT PREVIEW:\n" + script[:600])

    box.config(state=tk.DISABLED)
    win.mainloop()

def main():
    ensure_dir()

    titles = generate_titles()
    script = generate_script()
    thumb_text, thumb_prompt = generate_thumbnail()
    chain = prompt_chain()

    save("titles.txt", "\n".join(titles))
    save("script.txt", script)
    save("thumbnail.txt", thumb_text + "\n" + thumb_prompt)
    save("prompt_chain.txt", chain)

    show_popup(titles, script, thumb_text)

if __name__ == "__main__":
    main()
