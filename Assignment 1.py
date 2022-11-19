#python program to get fibonacci series between 0 to 50
first_num,second_num=0,1
while second_num<50:
    print( second_num,end=',')
    first_num,second_num=second_num,first_num+second_num

