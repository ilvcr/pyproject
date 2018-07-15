#!/usr/bin/env python
# coding=utf-8

#*************************************************************************#
# File Name: quineMcCluskey.py
# Author: yoghourt->ilvcr 
# Mail: liyaoliu@foxmail.com  @@  ilvcr@outlook.com 
# Created Time: 2018年07月15日 星期日 20时36分49秒
# Description: 
#************************************************************************#


def compare_string(string1, string2):
    l1 = list(string1)
    l2 = list(string2)
    count = 0

    for i in range(len(l1)):
        if l1[i] != l2[i]:
            count += 1
            l1[i] = '_'

    if count > 1:
        return -1
    else:
        return "".jion(l1)


def check(binary):
    pi = []

    while 1:
        check1 = ['$'] * len(binary)
        temp = []
        for i in range(len(binary)):
            for j in range(i+1, len(binary)):
                k = compare_string(binary[i], binary[j])

                if k != -1:
                    check1[i] = '*'
                    check1[j] = '*'
                    temp.append(k)

        for i in range(len(binary)):
            if check1[i] == '$':
                pi.append(binary[i])
        if len(temp) == 0:
            return pi
        binary = list(set(temp))


def decimal_to_binary(no_of_variable, minterms):
    temp = []
    s = ''
    for m in minterms:
        for m in range(no_of_variable):
            s = str(m%2) + s
            m //= 2
        temp.append(s)
        s = ''
    return temp

def is_for_table(string1, string2, count):
    l1 = list(string1)
    l2 = list(string2)
    count_n = 0

    for i in range(l1n(l1)):
        if l1[i] != l2[i]:
            count_n += 1

    if count_n == count:
        return True
    else:
        return False


def selection(chart, prime_implicants):
    temp = []
    select = [0] * len(chart)
    for i in range(len(chart[0])):
        count = 0
        rem = -1
        for j in range(len(chart)):
            if chart[j][i] == 1:
                count += 1
                rem = j
        
        if count == 1:
            select[rem] = 1

    for i in range(len(select)):
        if select[i] == 1:
            for j in range(len(chart[0])):
                if chart[i][j] == 1:
                    for k in range(len(chart)):
                        chart[k][j] = 0
            temp.append(prime_implicants[i])

    while 1:
        max_n = 0
        rem = -1
        count_n = 0
        for i in range(len(chart)):
            count_n = chart[i].count(1)
            if count_n > max_n:
                max_n = count_n
                rem = i

        if max_n == 0:
            return temp

        temp.append(prime_implicants[rem])

        for i in range(len(chart[0])):
            if chart[rem][i] == 1:
                for j in range(len(chart)):
                    chart[j][i] = 0



def prime_implicant_chart(prime_implicants, binary):
    chart = [[0 for x in range(len(binary))] for x in range(len(prime_implicants))]
    for i in range(len(prime_implicants)):
        count = prime_implicants[i].count('_')
        for j in range(len(binary)):
            if(is_for_table(prime_implicants[i], binary[j], count)):
                chart[i][j] = 1


def main():
    no_of_variable = int(input("Enter the no. of variables\n"))
    minterms = [int(x) for x in input("Enter the decimal representation of Minterms 'Spaces Seprated'\n").split()]
    binary = decimal_to_binary(no_of_variable, minterms)


    prime_implicants = check(binary)
    print "Prime Implicants are: "
    print prime_implicants
    chart = prime_implicant_chart(prime_implicants, binary)


    essential_prime_implicants = selection(chart, prime_implicants)
    print "Essential Prime Implicants are: "
    print essential_prime_implicants


if __name__ == '__main__':
    main()



