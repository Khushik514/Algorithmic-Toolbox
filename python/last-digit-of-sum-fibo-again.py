# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18
    pisano_period = 60
    n=to_index
    m=from_index
    # Taking mod of N with
    # period length
    n = n % pisano_period
    sum1=1
    previous, current = 0, 1
    if n==0:
        sum1=0
    elif n==1:
        sum1=1
    for i in range(n-1):
        previous, current = current%10, (previous + current)%10
        sum1+=current
    m=m-1
    m = m % pisano_period
    sum2=1
    previous, current = 0, 1
    if m==0:
        sum2=0
    elif m==1:
        sum2=1
    for i in range(m-1):
        previous, current = current%10, (previous + current)%10
        sum2+=current
    return ((sum1-sum2) % 10)


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
