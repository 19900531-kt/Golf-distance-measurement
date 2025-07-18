import tkinter as tk
from tkinter import ttk, messagebox

# サンプルのクラブ飛距離データ（ヤード）
CLUB_DISTANCES = [
    ("ドライバー", 300),
    ("3W", 280),
    ("5W", 260),
    ("4I", 240),
    ("5I", 225),
    ("6I", 200),
    ("7I", 185),
    ("8I", 170),
    ("9I", 155),
    ("PW", 140),
    ("AW", 120),
    ("SW", 100),
]

WIND_EFFECT = {
    "無風": 0,
    "向かい風": -10,  # 向かい風は10ヤード減算
    "追い風": 10,    # 追い風は10ヤード加算
}

class GolfClubSelector(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("ゴルフクラブ選択サポート")
        self.geometry("350x250")
        self.create_widgets()

    def create_widgets(self):
        # 距離入力
        tk.Label(self, text="残り距離（ヤード）").pack(pady=(20, 5))
        self.distance_var = tk.StringVar()
        tk.Entry(self, textvariable=self.distance_var).pack()

         # 風向き選択
        tk.Label(self, text="風向き").pack(pady=(15, 5))
        self.wind_var = tk.StringVar(value="無風")
        wind_options = list(WIND_EFFECT.keys())
        ttk.Combobox(self, textvariable=self.wind_var, values=wind_options, state="readonly").pack()

        # 計算ボタン
        tk.Button(self, text="おすすめクラブを表示", command=self.suggest_club).pack(pady=15)

        # 結果表示
        self.result_label = tk.Label(self, text="")
        self.result_label.pack(pady=10)

    def suggest_club(self):
        try:
            distance = int(self.distance_var.get())
        except ValueError:
            messagebox.showerror("入力エラー", "距離は数字で入力してください。")
            return
        wind = self.wind_var.get()
        wind_adjust = WIND_EFFECT.get(wind, 0)
        adjusted_distance = distance - wind_adjust

        # 最適なクラブを選択
        for club, club_dist in CLUB_DISTANCES:
            if adjusted_distance >= club_dist:
                self.result_label.config(text=f"おすすめクラブ: {club}")
                return
        self.result_label.config(text="該当するクラブがありません")

if __name__ == "__main__":
    app = GolfClubSelector()
    app.mainloop()




