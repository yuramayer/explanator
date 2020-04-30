import back

first_time = True

while True:
    u_word = back.greetings(first_time)
    first_time = False
    if u_word == 'Exit()':
        break
    output = back.translate(u_word)
    if isinstance(output, list):
        for number in range(len(output)):
            print(str(number + 1) + '. ' + output[number])
    else:
        print(output)
    print('')
