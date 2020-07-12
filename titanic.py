#テストデータで集計方法の練習をする。出来るだけdefで行う。
# ライブラリのインポート
import pandas as pd
pd.get_option("display.max_columns")#pandasで表を省略しない出力
pd.get_option("display.max_rows")#pandasで表を省略しない出力

# データセット読み込み
#フォルダー位置指定
#folder = "C:/Users/ponta/OneDrive/デスクトップ/Python/tatsuzawa/Kaggle/"
#train = pd.read_csv(f"{folder}/train.csv", encoding="cp932", header=0).dropna(how="all", axis=0)
#test = pd.read_csv(f"{folder}/test.csv", encoding="cp932").dropna(how="all", axis=0)
#data = [train, test]
#列名のリスト取得
#train_list = pd.read_csv(f"{folder}/train.csv", encoding="cp932", header=0).dropna(how="all", axis=0).iloc[:, 0]
#train_list = train.columns.tolist()
test = pd.read_csv("test.csv")
print(test.head())

