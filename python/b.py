
import json
from re import S
  
  
def file_save():
  data = {
    "name": "박성연_러브스토리",
    "symbol": "PLO",
    "description": "테스트 소개글입니다.테스트 소개글입니다.테스트 소개글입니다.테스트 소개글입니다.테스트 소개글입니다.테스트 소개글입니다.테스트 소개글입니다.테스트 소개글입니다.테스트 소개글입니다.테스트 소개글입니다.테스트 소개글입니다.",
    "seller_fee_basis_points": 1000,
    "image": "https://www.arweave.net/abcd5678?ext=png",
    "external_url": "https://givecherry.org/",
    "attributes": [
      {"trait_type": "이름", "value": "강석희"},
      {"trait_type": "이름2", "value": "강석희2"},
      {"trait_type": "이름3", "value": "강석희3"}
    ],
    "properties": {
      "files": [{"uri": "501.png", "type": "image/jpg"}],
      "category": "image",
      "creators": [
        {"address": "9nnGAh8QnYLNmCgf8JP6J7VH7mxg3zgh8BoZei1MxEWX", "share": 100},
        {"address": "C98EGsTDSPZCaWQRKtsrpRD5WsyWmnu7LbRiWYTDaKiC", "share": 0}
      ]
    },
    "collection": {"name": "위마켓웰페어 사회적협동조합", "family": "위마켓웰페어"}
  }

  file_path = "./test.json"

  with open(file_path, 'w', encoding='utf-8') as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
    
    

'''
  list split 함수
'''
def list_chunk(lst, n):
    return [lst[i:i+n] for i in range(0, len(lst), n)]
    
    
'''
  기본 attributes 세팅
'''
def set_attr(trait_type, value):
  attr = []
  for i, k in zip(trait_type, value):
    type_value = {'trait_type': 'test1', 'value': 'test2'}
    type_value["trait_type"] = i
    type_value["value"] = k
    
    attr.append(type_value)
  return attr


'''
  attributes 조합 : raw data 정제 및 세팅 
'''
def set_attr_mix(trait_type, trait_type_num):
  attr = []
  #trait_type_num = 4 # attr 쌍의 개수, 몇 개씩 자를 건지 
  #trait_type = ['배경', '캐릭터', '프레임', '추가'] # trait_type 값 세팅
  # Read raw data 가져오기
  with open('/data2/sykim/test_file_java/python/IconList.txt', 'r') as f:
    while True:
      value = []
      line = f.readline()
      if not line: break
      
      i = 3
      splited = line.split('\t') # 탭으로 split
      
      for split in splited:
        value.append(splited[i].split('\n')[0])
        if i == len(splited) - 1:
          break 
        i = i + 1
      
      for i, k in zip(trait_type, value):
        type_value = {'trait_type': 'test1', 'value': 'test2'}
        type_value["trait_type"] = i
        type_value["value"] = k
        attr.append(type_value)
    list_chunked = list_chunk(attr, trait_type_num)

  f.close()
  return list_chunked


'''
  properties 세팅
'''
def set_prop():
  prop = {}
  # files 세팅
  f_dic = {'uri' : 'a', "type": "image/jpg"}
  f_arr = [f_dic]
  # creators 세팅
  address = ['GzZ47NaZbLTy3XxuLsyQfqkPXA4gq7osL5ixgEkTZ8JQ', '2jjh7Fm6zmbmCD9mvAtj2sb4gmTK5a2ynnbrA7pfHUZR'] # 볼트 / 단체 지갑
  share = [0, 100]
  c_arr = []
  for i, k in zip(address, share):
    creators = {'address': 'set', 'share': 0}
    creators["address"] = i
    creators["share"] = k
    c_arr.append(creators)
  # props 세팅
  prop['files'] = f_arr
  prop['category'] = 'image'
  prop['creators'] = c_arr
  return prop


'''
  collection 세팅
'''
def set_col():
  col = {}
  col['name'] = 'name'
  col['family'] = 'name22'
  return col


'''
  전체 metadata 세팅
'''
def set_matadata(start_index, count, default_file_path, save_file_path, trait_type_num, trait_type, set_nft_name, value):
  with open(default_file_path, 'r') as f:
    metadata = json.load(f)

  # NFT 조합(mix)인 경우 세팅 및 json 저장
  list_chunked = set_attr_mix(trait_type, trait_type_num)
  for k in list_chunked:
    start_index = start_index + 1 
    set_num = {'trait_type' : '시리얼넘버', 'value' : start_index}
    
    if k[0]['trait_type'] == '시리얼넘버': # 시리얼넘버가 이미 존재하는 경우, value값만 변경되도록.
      k[0]['value'] = start_index
    else: # 없는 경우, 생성
      k.insert(0, set_num)
  
  for j in range(count):
    if j >= len(list_chunked[0]):
      metadata['attributes'] = list_chunked[abs(j - len(list_chunked[0]))]
      
      title_num = str(j + start_index + 1)
      nft_name = set_nft_name + ' #' + title_num.zfill(5)
      metadata['name'] = nft_name
    else:
      metadata['attributes'] = list_chunked[j]
      title_num = str(j + start_index + 1)
      nft_name = set_nft_name + ' #' + title_num.zfill(5)
      metadata['name'] = nft_name
    
    prop = set_prop()
    col = set_col()
    metadata['symbol'] = 'ABCDEF'
    metadata['description'] = 'DDDDDDD'
    metadata['seller_fee_basis_points'] = 3000
    metadata['image'] = 'SSSSS'
    metadata['external_url'] = 'SSSSS'
    metadata['properties'] = prop
    metadata['collection'] = col
    #title_num = str(list_chunked[j][0]['value'])
    #nft_name = set_nft_name + ' #' + title_num.zfill(5)
    #metadata['name'] = nft_name
    
    # 파일 저장
    #with open(save_file_path + title_num.zfill(5) + '.json', 'w', encoding='UTF-8') as file:
      #json.dump(metadata, file, indent=2, ensure_ascii=False)
  

  '''
  # 기본 attr인 경우 세팅 및 json 저장
  #while True: # 발행 개수에 따른 반복
  for i in range(count):
    attr = set_attr(trait_type, value)
    prop = set_prop()
    col = set_col()
    metadata['symbol'] = 'ABCDEF'
    metadata['description'] = 'DDDDDDD'
    metadata['seller_fee_basis_points'] = 3000
    metadata['image'] = 'SSSSS'
    metadata['external_url'] = 'SSSSS'
    metadata['attributes'] = attr
    metadata['properties'] = prop
    metadata['collection'] = col
    
    start_index = start_index + 1 
    set_num = {'trait_type' : '시리얼넘버', 'value' : start_index}
    attr[0] = set_num
    title_num = str(start_index)
    nft_name = set_nft_name + ' #' + title_num.zfill(5)
    metadata['name'] = nft_name # name 세팅
    print(metadata)
    
    # JSON 재저장
    with open(save_file_path + title_num.zfill(5) + '.json', 'w', encoding='UTF-8') as file:
      json.dump(metadata, file, indent=2, ensure_ascii=False)
    #if start_index == count: break 
  '''
  
  f.close()

  
# ex) 이름 a, 1~10 / 이름 b, 11~20 / 이름 c, 21~30

if __name__ == '__main__':
  start_index = 20 # 표시번호 -1
  count = 10  # 발행 개수
  set_nft_name = 'c테스트'
  trait_type_num = 3 # attr 쌍의 개수, 몇 개씩 자를 건지 
  trait_type = ['배경', '캐릭터', '프레임', '추가', '추가2'] # trait_type 값 세팅
  default_file_path = "/data2/sykim/test_file_java/python/metadata.json" # 기본 메타데이터 가져오기
  save_file_path = '/data2/sykim/test_file_java/python/'
  
  # attr 직접 부여시 / 동일 attr일 때
  value = ['화산1','파이팅11', '번개111']
  
  set_matadata(
    start_index,
    count,
    default_file_path,
    save_file_path,
    trait_type_num,
    trait_type,
    set_nft_name,
    value
  )
    
    