u"Bitonic Merge Sortモジュール"

# Pythonによるsort関数
def sort(x, up):
    u"""
    リストxの要素をupで指定された向きにソートする
    upがTrueなら昇順、Falseなら降順になる
    xの要素数は2のべき乗でなければならない(さもなければソート結果がおかしくなる)
    """

    if len(x) <= 1:
        # 要素数が1になったら終わり
        return x
    else:
        # ステップ1a
        # リストの前半(first)は昇順、後半(second)は降順でソートする(//は整数除算)
        mid_point = len(x) // 2
        first = sort(x[:mid_point], True)
        second = sort(x[mid_point:], False)

        # ステップ1b
        # 2分割したリストを1つに結合する
        x1 = first + second

        # ステップ2
        # サブソートに進む
        return _sub_sort(x1, up)

# Pythonによる_sub_sort関数
def _sub_sort(x, up):
    u"""
    バイトニックにソートされたリストxの前半と後半を
    upで指定された向きに比較、交換し、
    前半と後半それぞれについて再帰的にサブソートを適用する
    """
    if len(x) == 1:
        # 要素数が1になったら終わり
        return x
    else:
        # ステップ2a
        # 要素数nのバイトニック列の要素をn/2要素おきに比較して
        # upで指定された順序(昇順または降順)になるように交換する
        _compare_and_swap(x, up)

        # ステップ2b
        mid_point = len(x) // 2
        first = _sub_sort(x[:mid_point], up)
        second = _sub_sort(x[mid_point:], up)

        # ステップ2c
        # 2分割したデータ列を1つに結合する
        return first + second

# Pythonによる_compare_and_swap関数
def _compare_and_swap(x, up):
    u"""
    要素数nのバイトニック列の要素をn/2要素おきに比較して
    upで指定された順序(昇順または降順)になるように交換する(ステップ2a)
    """
    mid_point = len(x) // 2
    for i in range(mid_point):
        if (x[i] > x[mid_point + i]) == up:
            # 要素を交換する
            x[i], x[mid_point + i] = x[mid_point + i], x[i]

# Pythonによるmain関数
if __name__ == '__main__':
    # ソート対象の数列を作成する
    nums = [10, 30, 11, 20, 4, 330, 21, 110]
    
    # 昇順にソートする
    print(sort(nums, True))
    # 降順にソートする
    print(sort(nums, False))