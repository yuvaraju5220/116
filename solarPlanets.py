import cv2


img="solar-system.jpg"

img = cv2.imread("solar-system.jpg")


cv2.putText(img,
            "sun",
            (100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "mercury",
            (110,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
             )
cv2.putText(img,
            "mars",
            (190,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
             )
cv2.putText(img,
            "Earth",
            (300,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
             )
cv2.putText(img,
            "venus",
            (400,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
             )
cv2.putText(img,
            "jupiter",
            (520,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
             )

cv2.putText(img,
            "saturn",
            (720,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
             )
cv2.putText(img,
            "uranus",
            (900,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
             )
cv2.putText(img,
            "neptune",
            (1080,300),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
             )




cv2.imshow("Output",img)
cv2.waitKey(0)
cv2.imwrite("solar-system.jpg",img)