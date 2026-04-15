# q011〜q020 解答

## q011
`orders_data!F2`
```excel
=VLOOKUP(C2,product_master!$A$2:$C$5,2,FALSE)
```
下までコピー

## q012
`orders_data!G2`
```excel
=VLOOKUP(C2,product_master!$A$2:$C$5,3,FALSE)
```
下までコピー

## q013
`orders_data!H2`
```excel
=E2*G2
```
下までコピー

## q014
`orders_data!I2`
```excel
=VLOOKUP(D2,region_master!$A$2:$B$4,2,FALSE)
```
下までコピー

## q015
`orders_data!J2`
```excel
=H2*(1-I2)
```
下までコピー

## q016
`orders_data!K2`
```excel
=J2*(1+controls!$B$2)
```
下までコピー

## q017
`orders_data!M2`
```excel
=SUMIFS(J2:J11,D2:D11,"東日本",F2:F11,"PC")
```

## q018
`orders_data!M3`
```excel
=COUNTIFS(D2:D11,"西日本",F2:F11,"周辺機器")
```

## q019
`orders_data!M4`
```excel
=AVERAGEIF(F2:F11,"PC",K2:K11)
```

## q020
ピボットテーブル作成後、転記する値は以下。
- 東日本 × PC: `152000`
- 西日本 × 周辺機器: `18400`
- 中部 × PC: `77600`
- 総計: `435370`
