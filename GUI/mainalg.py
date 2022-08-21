#import numpy as np
#import pandas as pd
from itertools import product

#site = input("사이트명을 영문으로 입력하세요 : ")
#pw = input("자주 쓰는 비밀번호를 입력하세요 : ")
#name = input("본인의 이름을 한글로 입력하세요 : ")
#birth = input("본인의 생년월일을 6자리 숫자로 입력하세요 : ")

# 한글 인물명 로마자 영어 변환 : 네이버 API 이용
# input : name / output : names(리스트 형태로 가능한 영문표기명 반환)
import json
import urllib.request


def kor_roman(korean_word):
    client_id = "9XMwvp_ssvqOrkZS4pfZ"
    client_secret = "o_xTKNP7uj"

    encText = urllib.parse.quote(korean_word)
    url = "https://openapi.naver.com/v1/krdict/romanization?query=" + encText

    request = urllib.request.Request(url)
    request.add_header("X-Naver-Client-Id", client_id)
    request.add_header("X-Naver-Client-Secret", client_secret)
    response = urllib.request.urlopen(request)
    rescode = response.getcode()

    if (rescode == 200):
        response_body = response.read()
        json_dict = json.loads(response_body.decode('utf-8'))
        result = json_dict['aResult'][0]
        name_items = result['aItems']
        names = [name_item['name'] for name_item in name_items]
    else:
        print("Error Code:" + rescode)

    return names


#names = kor_roman(name)
#print(names)

#한글 인물명 키보드대로 영문 입력 결과
#input : name / output : text

# 초성 리스트. 00 ~ 18
CHOSUNG_LIST = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
# 중성 리스트. 00 ~ 20
JUNGSUNG_LIST = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
# 종성 리스트. 00 ~ 27 + 1(1개 없음)
JONGSUNG_LIST = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

def kor_strip(korean_word):
    r_lst = []
    for w in list(korean_word.strip()):
        ## 영어인 경우 구분해서 작성함.
        if '가'<=w<='힣':
            ## 588개 마다 초성이 바뀜.
            ch1 = (ord(w) - ord('가'))//588
            ## 중성은 총 28가지 종류
            ch2 = ((ord(w) - ord('가')) - (588*ch1)) // 28
            ch3 = (ord(w) - ord('가')) - (588*ch1) - 28*ch2
            r_lst.append([CHOSUNG_LIST[ch1], JUNGSUNG_LIST[ch2], JONGSUNG_LIST[ch3]])
        else:
            r_lst.append([w])
    return r_lst

def kor_key(korean_word):
    # 자음-초성/종성
    cons = {'r':'ㄱ', 'R':'ㄲ', 's':'ㄴ', 'e':'ㄷ', 'E':'ㄸ', 'f':'ㄹ', 'a':'ㅁ', 'q':'ㅂ', 'Q':'ㅃ', 't':'ㅅ', 'T':'ㅆ','d':'ㅇ', 'w':'ㅈ', 'W':'ㅉ', 'c':'ㅊ', 'z':'ㅋ', 'x':'ㅌ', 'v':'ㅍ', 'g':'ㅎ', '' : ' '}
    # 모음-중성
    vowels = {'k':'ㅏ', 'o':'ㅐ', 'i':'ㅑ', 'O':'ㅒ', 'j':'ㅓ', 'p':'ㅔ', 'u':'ㅕ', 'P':'ㅖ', 'h':'ㅗ', 'hk':'ㅘ', 'ho':'ㅙ', 'hl':'ㅚ','y':'ㅛ', 'n':'ㅜ', 'nj':'ㅝ', 'np':'ㅞ', 'nl':'ㅟ', 'b':'ㅠ',  'm':'ㅡ', 'ml':'ㅢ', 'l':'ㅣ'}
    cons = {v:k for k,v in cons.items()}
    vowels = {v:k for k, v in vowels.items()}
    text = ""
    init = ""
    nn = kor_strip(korean_word)
    for i in nn: #자음모음 분리된 리스트의 한 음절씩
        init += cons[i[0]] #각 음절의 첫 번째 자음 영문변환
        for j in i: #한 음절 내에서 각 자음 모음
            if j in cons:
                text += cons[j]
            elif j in vowels:
                text += vowels[j]
    return text

#text = kor_key(name)
#print(text)

#한글 인물명 영어 이니셜 변환
#input : name / output = init
#아까 변환한 로마자 영문명 베이스 이용

def kor_init(name):
    n_list = []
    name_list = kor_roman(name)
    for nn in name_list:
        n = nn.split(" ") #성과 이름 분리
        n_list.append(n[0][0] + n[1][0]) #성의 초성, 이름 첫 글자 초성 이니셜
    n_list = list(set(n_list))
    for i in range(len(name) - 2):
        matching = [s for s in name_list if kor_roman(name[: 2 + i])[0] in s]
        new = [word.strip(kor_roman(name[: 2 + i])[0])[0] for word in matching]
        new = list(set(new))
        n_list = [s[0] + s[1] for s in list(product(*[n_list, new]))]
    n_list = [s.lower() for s in n_list]
    return n_list

#init = kor_init(name)
#print(init)

#이름으로 가능한 패턴 생성
#names(리스트) : 성과 이름 분리 후

# fname = list(set([s.split(" ")[0].lower() for s in names]))
# lname = list(set([s.split(" ")[1].lower() for s in names]))
# text = [text]
# birth_yd = [birth[:2], birth[2:]]
# pattern =  fname + lname + text + init + birth_yd
# length = [len(fname), len(lname), len(text), len(init), len(birth_yd)]
# pattern

# pw = pw.lower()
# remain = pw
# idxx = []
# sort = ["fname", "lname", "text", "init", "birth_yd"]
# lenn = np.cumsum(length) - 1
# for p in pattern:
    # idx = pw.find(p)
    # if idx != -1:
        # sorte = sort[np.where(pattern.index(p) <= lenn)[0][0]]
        # idxx.append((idx, sorte, p))
        # remain = remain.replace(p, "")

# print(pw, remain, idxx)

import re
import string
import random


def pwgen(min_len, max_len, lett, remain, fname, lname, init, birth, site):
    min_len = int(min_len)
    max_len = int(max_len)
    lett = int(lett)
    cur_eng = len(re.findall("[a-zA-Z]+", remain))
    cur_dig = len(re.findall("[0-9]+", remain))
    cur_let = len(re.findall("[!@#$%^&*]+", remain))
    eng = "".join(s for s in fname + lname + init)
    if len(remain) >= min_len and len(remain) <= max_len: #남은 비밀번호가 비밀번호 요구 길이 충족시
        if cur_eng != 0 and cur_dig != 0: #개중 숫자와 영어가 적어도 1자리 이상 각각 포함되는 경우
            if cur_let != 0 or lett == 0: #특수문자 추가하지 않아도 되는 경우 : 남은 비번에 특수문자가 있거나 특수문자 조건이 없는 경우
                output = remain
                output = site[0].upper() + output.replace(random.choice(re.findall("[a-zA-Z]+", output)[0]), "", 1)
            else:
                if max(cur_eng, cur_dig) == cur_eng:
                    output = site[0].upper() + re.findall("[a-zA-Z]+", remain)[0][:cur_eng - 2] + re.findall("[0-9]+", remain)[0] + random.choice("!@#$%^&*")
                else:
                    output = site[0].upper() + re.findall("[a-zA-Z]+", remain)[0] + re.findall("[0-9]+", remain)[0][:cur_dig - 2] + random.choice("!@#$%^&*")
        else:
            if cur_let != 0 or lett == 0:
                if max(cur_eng, cur_dig) == cur_eng:
                    output = remain.replace(random.choice(re.findall("[a-zA-Z]+", remain)[0])[0], "", 1) + random.choice(birth)
                    output = output.replace(random.choice(re.findall("[a-zA-Z]+", output)[0]), random.choice(re.findall("[a-zA-Z]+", output)[0]).upper(), 1)
                else:
                    output = site[0].upper() + remain.replace(random.choice(re.findall("[0-9]+", remain)[0])[0], "", 1)
            else:
                if max(cur_eng, cur_dig) == cur_eng:
                    output = remain.replace(random.choice(re.findall("[a-zA-Z]+", remain)[0])[0], "", 1).replace(random.choice(re.findall("[a-zA-Z]+", remain)[0])[0], "", 1)
                    output = output + random.choice(birth) + random.choice("!@#$%^&*")
                    output = output.replace(random.choice(re.findall("[a-zA-Z]+", output)[0]), random.choice(re.findall("[a-zA-Z]+", output)[0]).upper(), 1)
                else:
                    output = remain.replace(random.choice(re.findall("[0-9]+", remain)[0])[0], "", 1).replace(random.choice(re.findall("[0-9]+", remain)[0])[0], "", 1)
                    output = output + site[0].upper() + random.choice("!@#$%^&*")
    elif len(remain) < min_len:
        if cur_eng != 0 and cur_dig != 0:
            output = remain + ''.join(random.sample(birth + birth, round((min_len - len(remain))/2)))
            output = output + ''.join(random.sample(eng, min_len - len(remain) - round((min_len - len(remain))/2)))
        elif cur_eng != 0 and cur_dig == 0:
            output = remain + ''.join(random.sample(birth + birth, min_len - len(remain)))
        elif cur_eng == 0 and cur_dig != 0:
            output = remain + ''.join(random.sample(eng, min_len - len(remain)))
        else:
            output = remain + ''.join(random.sample(birth + birth, round(min_len/2)))
            output = output + ''.join(random.sample(eng, min_len - round(min_len/2)))
        if cur_let == 0 and lett == 1:
            output = output.replace(random.choice(re.findall("[a-zA-Z]+", output)[0]), random.choice(re.findall("[a-zA-Z]+", output)[0]).upper(), 1) + random.choice("!@#$%^&*")
        else:
            output = output.replace(random.choice(re.findall("[a-zA-Z]+", output)[0]), random.choice(re.findall("[a-zA-Z]+", output)[0]).upper(), 1)
    else:
        output = "".join(random.sample(eng, round(min_len / 2)))
        output = output.replace(random.choice(output), random.choice(output).upper()) + "".join(random.sample(birth + birth, min_len - round(min_len / 2)))
        if cur_let == 0 and lett == 1:
            output = output + random.choice("!@#$%^&*")
    output = "".join(random.sample(output, len(output)))
    return output

# spwgen(remain, idxx, fname, lname, init, birth, site)
