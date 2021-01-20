import random

# 従業員の名前と新人かどうかの判定だけ現在入れている
# 上長の方とセットにする為に入力している
# 上長の人は平日は基本いるということなので、シフト表には入れていない
def worker_input():
    # 名前の入力
    input_name = input('名前を入力してください。→')

    # 新人かどうかの設定
    input_type = input('新人または新人につく方の場合は１を入力してください。違う場合は１以外あるいは未入力でお願いします。→')

    # 名前が未入力だった場合再入力
    if not input_name:
        print('名前は必ず入力してください。')
        return worker_input()
    else:
        pass

    # 入力値のチェック
    try:
        input_type = int(input_type)
        if(input_type != 1):
            input_type = 0
        else:
            pass
    except:
        input_type = 0
    
    # 従業員のデータをリストに入れる
    worker_list = []
    
    # 従業員の名前
    worker_list.append(input_name)
    worker_list.append(input_type)
    return worker_list

# 従業員の人数の設定
def check_worker_num():
    # 従業員数の入力
    input_worker_num = input('従業員の人数を入力してください。→')

     # 入力値のチェック
    try:
        input_worker_num = int(input_worker_num)
    except:
        print('人数を入れてください')
        return check_worker_num()

    # 初期化
    worker_data = []
    
    # 人数分の従業員データの入力
    for x in range(input_worker_num):
        data = worker_input()
        worker_data.append(data)
    
    # 新人優先で並び替える
    worker_data = sorted(worker_data, key=lambda s: s[1],reverse=True)
    
    return worker_data
