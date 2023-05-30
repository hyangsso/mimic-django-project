import pandas as pd

def cases_parsing():
    df_cases = pd.read_csv("https://api.vitaldb.net/cases")  # 임상 정보
    dict_cases = df_cases.to_dict("records")
    return dict_cases

def trks_parsing():
    df_trks = pd.read_csv('https://api.vitaldb.net/trks')  # 트랙 목록
    dict_trks = df_trks.to_dict("records")
    return dict_trks

def tid_extracting(tid):
    df_features = pd.read_csv(f'https://api.vitaldb.net/{tid}')
    dict_features = df_features.to_dict("records")
    return dict_features

def lab_parsing():
    df_labs = pd.read_csv('https://api.vitaldb.net/labs')  # 검사 결과
    dict_labs = df_labs.to_dict("records")
    return dict_labs