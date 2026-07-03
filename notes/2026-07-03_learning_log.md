# 2026年7月3日 学習ログ

## 今日取り組んだこと

今日は、今週取り組んだ学習内容の中から、Python基礎の「商品ごとの売上合計を辞書にまとめる」課題について整理しました。

今週は以下の内容に取り組みました。

* SQL：4問
* Python基礎：2問
* Excel：q001〜q020

## 今日整理した課題

* 分野：Python基礎
* 課題：商品ごとの売上合計を辞書にまとめる
* 関連README：`python/basics/q002_sales_by_product/README.md`

## 目的

CSVファイルに記録されている商品名、数量、価格を読み込み、商品ごとの売上合計を辞書にまとめることを目的としました。

## 処理の流れ

1. CSVファイルを読み込む
2. 商品名、数量、価格を1行ずつ取り出す
3. 商品ごとに「数量 × 価格」を計算する
4. 計算した売上を商品ごとの辞書に加算する
5. 商品ごとの売上合計を、売上が大きい順に並び替えて表示する

## 学んだこと

`product_sales.items()` を使うことで、辞書のキーと値をセットで取り出せることを学びました。

また、`sorted(product_sales.items(), key=lambda x: x[1], reverse=True)` と書くことで、辞書の値である売上合計を基準にして、売上が大きい順に並び替えられることを学びました。

特に、`lambda x: x[1]` は「商品名と売上合計のセットのうち、売上合計の部分を並び替えの基準にする」という意味だと理解しました。

## SQL q026：ウィンドウ関数（科目内順位）の再実行

### 今日再実行した問題

SQL q026「ウィンドウ関数（科目内順位）」を再実行しました。

この問題では、各科目ごとに点数の高い順で順位を付け、`subject_id`、`subject_name`、`student_id`、`point`、`rnk` を表示します。

### 実行したSQL

```sql
SELECT
  p.subject_id,
  sub.name AS subject_name,
  p.student_id,
  p.point,
  RANK() OVER (
    PARTITION BY p.subject_id
    ORDER BY p.point DESC
  ) AS rnk
FROM point AS p
JOIN subject AS sub
  ON sub.id = p.subject_id
ORDER BY p.subject_id, rnk, p.student_id;
```

### なぜこの処理を書くのか

科目ごとに順位を付けたいので、`PARTITION BY p.subject_id` を使って、順位付けの範囲を科目ごとに分けます。

点数が高い学生を上位にしたいので、`ORDER BY p.point DESC` を使って、点数の高い順に並べます。

科目IDだけでは科目名が分からないため、`subject` テーブルを結合して、`subject_name` も一緒に表示します。

### 学んだこと

`RANK() OVER` を使うと、元の行を残したまま順位を追加できることを確認しました。


また、`PARTITION BY` を使うことで、全体順位ではなく「科目ごとの順位」を付けられることを復習しました。

## 次にやること

次回は、同じようにPython基礎の別課題やpandasのCSV読み込み課題について、目的・処理の流れ・学んだことを自分の言葉で整理します。
