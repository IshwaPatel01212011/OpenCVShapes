import cv2

dog = cv2.imread("Lesson 4/images/dog.png")

# drawing a line

line = cv2.line(dog, (150,100),(250,150),(0,171,250),4)
cv2.imshow("Line on the Image",line)
cv2.waitKey(0)


# drawing a circle 

dog = cv2.imread("Lesson 4/images/dog.png")

circle = cv2.circle(dog, (150,100),25,(250,96,0),3)
cv2.imshow("Circle on the Image",circle)
cv2.waitKey(0)

# drawing filled cricle 

dog = cv2.imread("Lesson 4/images/dog.png")

circle = cv2.circle(dog, (150,100),25,(250,96,0),-3)
cv2.imshow("Circle on the Image",circle)
cv2.waitKey(0)

# drawing rectangle/suqare

dog = cv2.imread("Lesson 4/images/dog.png")

rectanglesquare = cv2.rectangle(dog, (150,150),(300,400),(251,143,255),3)
cv2.imshow("Rectangle/Square on the Image",rectanglesquare)
cv2.waitKey(0)

# drawing filled reactangle/square

dog = cv2.imread("Lesson 4/images/dog.png")

rectanglesquare = cv2.rectangle(dog, (150,150),(300,400),(251,143,255),-3)
cv2.imshow("Rectangle/Square on the Image",rectanglesquare)
cv2.waitKey(0)

# putting text on the screen

dog = cv2.imread("Lesson 4/images/dog.png")

text = cv2.putText(dog, "Cute Little Puppy!", (50,100), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1,(250,60,76), 2)
cv2.imshow("Text on the screen",text)
cv2.waitKey(0)

# drawing a arrow using a line

dog = cv2.imread("Lesson 4/images/dog.png")

arrow = cv2.arrowedLine(dog, (150,150),(250,300),(251,143,255), 3)
cv2.imshow("Arrow on the Image", arrow)
cv2.waitKey(0)

# drawing ellipse on the image

dog = cv2.imread("Lesson 4/images/dog.png")

ellipse = cv2.ellipse(dog, (300,250),(50,30),40,0,360,(250,60,76), 4)
cv2.imshow("Ellipse on the screen", ellipse)
cv2.waitKey(0)

# multple shapes on one image 

dog = cv2.imread("Lesson 4/images/dog.png")

circle_2 = cv2.circle(dog, (190,210),15,(250,96,0),3)
cv2.imshow("Multiple shpaes on the image",circle_2)
cv2.waitKey(0)

circle_3 = cv2.circle(dog, (285,208),15,(250,96,0),3)
cv2.imshow("Multiple shpaes on the image",circle_3)
cv2.waitKey(0)

circle_4 = cv2.circle(dog, (240,246),25,(250,96,0),3)
rectangle  = cv2.rectangle(dog, (75,100),(150,275),(250,96,0),3)
rectangle_2 = cv2.rectangle(dog, (300,100),(375,275),(250,96,0),3)
cv2.imshow("Multiple shapes on the image",rectangle)
cv2.imshow("Multiple shapes on the image",circle_4)
cv2.imshow("Multiple shapes on the image", rectangle_2)
cv2.waitKey(0)


