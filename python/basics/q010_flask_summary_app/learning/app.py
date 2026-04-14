from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    # 最初の画面を表示する
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    try:
        # フォームから送られた値は文字列なので int に変換する
        quantity = int(request.form["quantity"])
        unit_price = int(request.form["unit_price"])

        # 合計金額を計算する
        total = quantity * unit_price

        # result.html に値を渡して表示する
        return render_template(
            "result.html",
            quantity=quantity,
            unit_price=unit_price,
            total=total
        )
    except ValueError:
        # 数字以外が入力されたときのメッセージ
        return "数量と単価は整数で入力してください。"

if __name__ == "__main__":
    app.run(debug=True)
