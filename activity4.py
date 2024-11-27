#There are five trees in Jack's front yard. He checks each tree to find out how tall it is in inches and writes the height on a sheet of paper. Jack's list: 98, 94, 41, 96, and 11. What is the average height of a tree in Jack's front yard?

tree1=98
tree2=94
tree3=41
tree4=96
tree5=11

sum=tree1+tree2+tree3+tree4+tree5 #sum=98+94+41+96+11
Average=sum/5
print(Average)#print is for displaying

#rite a program to calculate the number of notes in the given amount

#5760 5 thousand 

amount=int(input("Enter the amount"))#taking the value from the user

note1=amount//100 # if 16//5:-3
note2=(amount%100)//50  # if u r doing modulus(%) 16%5:- 1
note3=((amount%100)%50)//10
print("the hundreds:", note1)
print("the fifty: ", note2)
print("the ten :", note3)