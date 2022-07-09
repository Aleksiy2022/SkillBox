while True:

  act = input('Введите операцию: плюс + , минус - , умножить *, разделить /. break - для выхода из программы.')
  if act == 'break':
    print('Выход из программы')
    break
  nums = int(input('Сколько операндов? '))
  count = 1
  answer = ''
  total_answer = 0
  
  for number in range(nums):
    print('Введите операнд', count, ':', end = ' ')
    num = int(input(''))
    if act == '+' and count >= 2:
      total_answer += num
    elif act == '-' and count >= 2:
      total_answer -= num
    elif act == '*' and count >= 2:
      total_answer *= num
    elif act == '/' and count >= 2:
      total_answer /= num
    elif count == 1:
      total_answer += num
    
    count += 1
    if count == nums + 1:
      answer += str(num)
      break
    answer += str(num) + ' ' + act + ' '
    
  print(answer, '=', total_answer)





