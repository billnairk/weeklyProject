# 여러 학생의 이름과 점수를 등록한다.
# 특정 학생의 시험 점수를 확인하거나 변경 할 수 있어야 한다.
# 꼴등과 1등을 구할 수 있어야 한다.
# 1등부터 차례로 나열

stu_list = {
  "민석" : 100,
  "온달": 20,
  "나라": 90,
  "베인" : 75,
  "니꼬" : 99,
  "선혜" : 80
  }

def show_board():
  print(
  '''
  1. 학생 이름, 점수 등록

  2. 학생 점수 조회

  3. 1등과 꼴등 조회

  4. 점수 변경

  5. 석차 조회

  6. 학생 명단 조회
  ''')
  select_number()

def ask_for_again():
  conti = input("\n  더 보시겠습니까?(Y/N) : ")
  if conti == "y" or conti == "Y":
    show_board()
  elif conti == "n" or conti =="N":
    print("\n  프로그램을 종료 합니다.")
  else:
    ask_for_again()

# 1
def register_stu_score():
  name = input("  이름 : ")
  score = int(input("  점수 : "))
  stu_list[name] = score
  print("\n  등록 완료 !!")
  print('\n  명단 : ', stu_list)
  print()
  ask_for_again()

# 2
def enquiry_score():
  stu_name = input("  조회할 학생의 이름 : ")
  if stu_name in stu_list:
    print('\n  ' + '-' * 20)
    print(f"  [{stu_name}] 학생의 점수 : {stu_list[stu_name]}")
    print('  ' + '-' * 20)
  else:
    print(f"  ❌  {stu_name}은(는) 없는 학생입니다.\n")
    enquiry_score()
  ask_for_again()

# 3
def enquiry_first_last():
  print("3 입니다.")
  ask_for_again()

# 4
def socre_change():
  change_stu = input("  점수를 수정할 학생의 이름 : ")
  before_score = stu_list[change_stu]
  change_score = int(input("  수정 할 점수 : "))
  print()
  print('  ' + '-' * 20)
  stu_list[change_stu] = change_score
  print(f"  [{change_stu}] 학생의 점수가 변경되었습니다.")
  print(f"  {before_score}점 -> {change_score}점")
  print('  ' + '-' * 20)
  ask_for_again()

# 5
def ranking():
  # 순위 번호
  num = 0
  # 점수 비교 변수
  # j = 0
  # 점수 높은 순서대로 저장할 배열 = 랭킹
  ranking = {}

  # 순위 정하는 알고리즘
  for i in list(stu_list.items()):
    for j in i:
      print(i[1])
      print(i[0])

  # 저장된 순위 출력하는 알고리즘
    # print(f"  {num}등 {i[0]}({i[1]})")
  ask_for_again()

# 6
def show_stu():
  print('  ' + '-' * 20)
  num = 0
  for i in list(stu_list.keys()):
    num += 1
    print(f"  {num}. {i}", end=' ')
    if num % 2 == 0:
      print()
  if num % 2 != 0:
    print()
  print('  ' + '-' * 20)
  ask_for_again()

def select_number():
  try:
    number = int(input("  번호를 입력하세요. : "))
    print()
    if number == 1:
      print("  ### 학생 이름, 점수 등록 ###\n")
      register_stu_score()
    elif number == 2:
      print("  ### 학생 점수 조회 ###")
      enquiry_score()
    elif number == 3:
      print("  ### 1등과 꼴등 조회 ###\n")
      enquiry_first_last()
    elif number == 4:
      print("  ### 점수 변경 ###")
      socre_change()
    elif number == 5:
      print("  ### 석차 조회 ###")
      ranking()
    elif number == 6:
      print("  ### 학생 명단 조회 ###")
      show_stu()
    else:
      print("  ⛔️ 1 ~ 6 사이의 숫자를 입력하십시오.\n")
      select_number()      
  except ValueError:
    print("\n  ⛔️ 숫자를 입력하십시오.\n")
    select_number()
  except UnboundLocalError:
    print("\n  ⛔️ 숫자를 입력하십시오.\n")
    select_number()

def init():
  show_board()

init()