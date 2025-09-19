from flask import Flask, render_template

app = Flask(__name__)

# 固定値
KINDS = ["REG", "BIG"]
FIXED_MEDALS = {"REG": 90, "BIG": 210}
FIXED_YUURI  = {"REG": 25, "BIG": 60}

# デフォルト10件（初期はREG/ゲーム数0）
DEFAULT_ROWS = [
    {"label": f"{i+1}個目", "kind": "REG", "games": 0}
    for i in range(10)
]

@app.route("/")
def index():
    return render_template(
        "index.html",
        kinds=KINDS,
        fixed_medals=FIXED_MEDALS,
        fixed_yuuri=FIXED_YUURI,
        default_rows=DEFAULT_ROWS,
    )

if __name__ == "__main__":
    app.run(debug=True)
