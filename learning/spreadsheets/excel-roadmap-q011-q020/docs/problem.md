# q011〜q020 問題一覧

## q011
`product_master` を参照して、`orders_data!F2:F11` にカテゴリを入力する。

## q012
`product_master` を参照して、`orders_data!G2:G11` に単価を入力する。

## q013
`orders_data!H2:H11` に売上（数量×単価）を入力する。

## q014
`region_master` を参照して、`orders_data!I2:I11` に地域割引率を入力する。

## q015
`orders_data!J2:J11` に割引後売上（売上×(1-地域割引率)）を入力する。

## q016
`controls!B2` の消費税率を絶対参照して、`orders_data!K2:K11` に税込売上を入力する。

## q017
`orders_data!M2` に「東日本かつPC」の割引後売上合計を入力する。

## q018
`orders_data!M3` に「西日本かつ周辺機器」の件数を入力する。

## q019
`orders_data!M4` に「PC」の税込売上平均を入力する。

## q020
`orders_data` を元にピボットテーブルを作成する。
- 行：地域
- 列：カテゴリ
- 値：割引後売上（合計）

作成後、次の値を `pivot_task` に転記する。
- B9: 東日本 × PC
- B10: 西日本 × 周辺機器
- B11: 中部 × PC
- B12: 総計
