def compute_bmi(weight, height):
    bmi = weight / height ** 2

    if bmi < 18.5:
        result = 'underweight'
    elif bmi > 25:
        result = 'overweigth'
    else:
        result = 'normal'
    return result

if __name__ == '__main__':
    user_weight = float(input('Provide wieght[kg]: '))
    user_height = float(input('Provide height[m]: '))
    user_result = compute_bmi(user_weight, user_height)
    print(f'You are: {user_result} ')
