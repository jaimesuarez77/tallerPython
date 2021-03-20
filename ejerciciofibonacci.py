

fibonacci=1 
auxiliar=0
init = 1


while (init<=10):
     auxiliar += fibonacci 
     fibonacci = auxiliar - fibonacci
     init += 1
     print(fibonacci)
