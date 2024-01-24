from abc import ABC, abstractmethod

class AbstractClass(ABC):

    _hi = []

    # 알고리즘의 뼈대는 추상 클래스의 메소드로 설계되어 있다.
    def template_method(self):
        self.my_name_is()
        self.second_name()
        self.first_name()

    # 기본 - 서브클래스 전반에서 사용되는 연산
    def my_name_is(self):
        print("my name is ", end="")

    # 훅 - 서브클래스에서 필요에 따라 재정의하는 연산
    def first_name(self):
        pass

    # 필수 - 서브클래스에서 필수로 재정의해야 하는 연산
    @abstractmethod
    def second_name(self):
        pass


# 필수만 재정의
class Name(AbstractClass):

    def second_name(self):
        print("thon")


# 필수 및 훅 또한 정의
class FullName(AbstractClass):

    def first_name(self):
        print("Py", end="")

    def second_name(self):
        print("thon", end=" ")


if __name__ == "__main__":

    name = Name()
    name.template_method()

    full_name = FullName()
    full_name.template_method()