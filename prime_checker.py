def is_prime(n):
    """
    주어진 수가 소수인지 판별하는 함수
    """
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if n % 2 == 0:
        return False
    
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    
    return True


def main():
    """
    사용자 입력을 받아 소수 판별을 수행하는 메인 함수
    """
    try:
        num = int(input("정수를 입력하세요: "))
        
        if is_prime(num):
            print(f"{num}은(는) 소수입니다.")
        else:
            print(f"{num}은(는) 소수가 아닙니다.")
    
    except ValueError:
        print("정수를 입력해주세요.")


if __name__ == "__main__":
    main()
