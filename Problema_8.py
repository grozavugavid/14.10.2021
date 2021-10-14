x="A B C D E F G H I J K L M N O P Q R S T U V W X Y "
x1="A B C D E F G H I J K L M N O P Q R S T U V W X Y "
x2="A B C D E F G H I J K L M N O P Q R S T U V W X Y "
x3="A B C D E F G H I J K L M N O P Q R S T U V W X Y "
for i in x:
    z=chr(ord(i)+1)
    x1+=z
    y=x1.replace('!',' ')
    line=y.replace('[','A')
print("Line1:", line)

