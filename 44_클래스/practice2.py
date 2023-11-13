# 실습2 : Supermarket 클래스
class Supermarket:
  count = 0 # 슈퍼마켓 클래스 인스턴스 카운트 정의
  #조건. 클래스 선언시, 인자로 location,name,product,customer 받기
  def __init__(self,location,name,product,customer): # 생성자
    self.location=location
    self.name=name
    self.product=product
    self.customer=customer
    Supermarket.count +=1 # 슈퍼마켓 클래스 인스턴스 카운트 ++
    
  def print_location(self): # 위치를 출력하는 함수
    print(f"{self.name}의 위치는 {self.location}  입니다") 
  def change_category(self, change_product): # 받은 인자로 파는 물건 바꾸는 함수
    self.product=change_product
  def show_list(self): # 현재 파는 물건 출력 함수
    print(f"{self.name}의 현재 판매물품은 {self.product} 입니다")
  def enter_customer(self): # 손님의 수를 1씩 늘리는 함수
    self.customer+=1
  def show_info(self): # 가게이름, 위치, 파는 물건, 손님 수 모두 출력 함수
    print(f"가게이름 : {self.name} / 위치 : {self.location} / 판매물품 : {self.product} / 손님 수 : {self.customer}")
  def show_supermarket_count(self): # 슈퍼마켓 클래스 인스턴스 개수 출력 함수
    print(f"슈퍼마켓 클래스 인스턴스 개수 : {Supermarket.count}")

new=Supermarket("마포구 대흥동", "코딩온", "얼음없는아이스아메리카노", 0)
new.print_location()
new.change_category("차가운아이스아메리카노")
new.show_list()
new.enter_customer()
new.show_info()
new.show_supermarket_count()