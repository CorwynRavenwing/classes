#Replace all ______ with rjust, ljust or center. 

thickness = int(input()) #This must be an odd number
c = 'H'

#Top Cone
for i in range(thickness):
    left = (c *i).rjust(thickness-1)
    right = (c*i).ljust(thickness-1)
    print(left+c+right)

#Top Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Middle Belt
for i in range((thickness+1)//2):
    print((c*thickness*5).center(thickness*6))

#Bottom Pillars
for i in range(thickness+1):
    print((c*thickness).center(thickness*2)+(c*thickness).center(thickness*6))

#Bottom Cone
for i in range(thickness):
    left = (c *(thickness-i-1)).rjust(thickness)
    right = (c*(thickness-i-1)).ljust(thickness)
    arrow = left+c+right
    print(arrow.rjust(thickness*6))

