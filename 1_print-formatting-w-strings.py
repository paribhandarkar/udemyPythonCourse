name = "pari"
print("my name is {}".format("pari"))
print(f"her name is also {name}")
print("the {} {} {}.".format('quick', 'brown', 'fox'))
print("the {q} {b} {f}.".format(q='quick', b='brown', f='fox'))
print("the {f} {q} {b}.".format(q='quick', b='brown', f='fox'))
print("the {0} {1} {2}.".format('quick', 'brown', 'fox'))

#float formatting
result = 100/777
print(f"the result is {result:{1}.{6}f}")
#{value:width.precisionf}

print("the reuslt is {r:3.4f}".format(r=result))

print("{0:<8} | {1:>9}".format('left', 'right'))
print("{0:=<8} | {1:a^10} | {2:->9}".format('left', 'center', 'right'))

num = 23.45678
print("My 10 character, four decimal number is:{0:10.4f}".format(num))
print(f"My 10 character, four decimal number is:{num:{10}.{6}}")
# Note that with f-strings, precision refers to the total number of digits, not just those following the decimal. This fits more closely with scientific notation and statistical analysis.