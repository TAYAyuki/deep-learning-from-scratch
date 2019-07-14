# coding: utf-8
"""サンプルクラス"""
class Man:
     """コンストラクタ"""
     # self は必ず引数に書く
    def __init__(self, name):
        self.name = name
        # self.変数名 : インスタンス変数
        print("Initilized!")

    def hello(self):
        print("Hello " + self.name + "!")

    def goodbye(self):
        print("Good-bye " + self.name + "!")

"""インスタンス生成"""
m = Man("David")

m.hello()
#呼び出すインスタンス.関数名()
m.goodbye()
