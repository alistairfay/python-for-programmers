#if, else and elif

sunny = True
if sunny:
    print("sunny")

sunny = False
if sunny:
    print("sunny")
else:
    print("not sunny")

a=0
if a>4:
    print("bigger than 4")
elif a>0:
    print("bigger than 0 but less than 4")
else:
    print("less than 0")

#conditionals
"""
>
<
>=
<=
!
==
!==
"""

a=5.5
if 7>= a >= 5:
    print("Between 5 and 7")

a=2
if a%2==0:
    print("even")

if 7>= a >= 5 and a%2==0:
    print("Between 5 and 7 and even")

if 7>= a >= 5 or a%2==0:
    print("Between 5 and 7 or even")

if a:
    print("a is anything other than 0 none of empty string")
