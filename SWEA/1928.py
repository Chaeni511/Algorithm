# import base64
# code  = input()
# code_bytes = base64.b64decode(code)
# result = code_bytes .decode('ascii')
# print(result)

ascii = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
          'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          '0','1','2','3','4','5','6','7','8','9','+','/'
          ]

for s in range(T):
    code = list(input())
    decode = ''
    for c in code:
        num = str(ascii.index(c))
        bin_num = str(bin(num)[2:1])
        while len(bin_num) < 6:
            bin_num = '0' + bin_num
        decode += bin_num

    result = ''

    for i in range(len(code)*6//8):
        j = int(result)
