
import json


#params : (dup, src_path, tgt_path, s_file_names, s_file_exts, start_index, serial, numbering)
def copy_files():
  print('함수실행')
  
  
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
    


def file_read():
  file_path = "/data2/sykim/test_file_java/python_test_ksy/metadata.json"
  with open(file_path, 'r') as f:
    metadata = json.load(f)
  
  start_index = 0
  count = 10  # 발행 개수
  num = start_index
  nft_name = metadata['name']  # 기존 제목 저장
  set_nft_name = 'nft 이름변경테스트'
  
  for i in range(count):
    num = num + 1
    title_num = str(num)
    new_nft_name = set_nft_name + ' #' + title_num.zfill(5)
    print(new_nft_name)
    new_nft_name = nft_name
  
  # raw_val = ['화산','파이팅', '번개'] 조합인 경우 따로 만들기. raw data불러와서 작업
  attr = []
  a = ['배경', '캐릭터', '프레임']
  b = ['화산','파이팅', '번개']
  for i, k in zip(a, b):
    type_value = {'trait_type': 'test1', 'value': 'test2'}
    type_value["trait_type"] = i
    type_value["value"] = k
    
    attr.append(type_value)
  print("attr >>>", attr)
  
  
  prop = {'files' : [{'uri' : 'a', "type": "image/jpg"}],
          'category' : 'image',
          'creators' : [{'address' : 'address', 'share' : 0}]
          }

  col = {'name' : 'qqq', 'family' : 'ddd'}

    
  metadata['symbol'] = 'ABCDEF'
  metadata['description'] = 'DDDDDDD'
  metadata['seller_fee_basis_points'] = 3000
  metadata['image'] = 'SSSSS'
  metadata['external_url'] = 'SSSSS'
  metadata['attributes'] = attr
  metadata['properties'] = prop
  metadata['collection'] = col
  print(metadata)

  f.close()
  

  


if __name__ == '__main__':
    #copy_files()
    #file_save()
    file_read()
    