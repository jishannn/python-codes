from flask import Flask, render_template, request, redirect

app = Flask(__name__)
NOTES_FILE = "notes.txt"

def load_notes():
    """Load notes from file."""
    try:
        with open(NOTES_FILE, "r", encoding="utf-8") as f:
            return f.readlines()
    except FileNotFoundError:
        return []

def save_notes(notes):
    """Save notes to file."""
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        f.writelines(notes)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        note = request.form.get("note").strip()
        if note:
            notes = load_notes()
            notes.append(note + "\n")
            save_notes(notes)
        return redirect("/")
    
    notes = load_notes()
    return render_template("index.html", notes=notes)

@app.route("/delete/<int:note_id>")
def delete(note_id):
    notes = load_notes()
    if 0 <= note_id < len(notes):
        notes.pop(note_id)
        save_notes(notes)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
