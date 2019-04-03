import pandas as pd
import cv2

df = pd.read_csv("cert.csv")

for index, row in df.iterrows():
    name = str(row['NAME'])
    r_no = str(row['REG NO'])
    w1 = str(row['E-CERTI WORKSHOP1'])
    w2 = str(row['E-CERTI WORKSHOP2'])
    
    if r_no != "nan":
        a = 0
        p = 0
        c = 0
        if w1=="AndroHop":
            a = 1
        elif w1=="PY.AI":
            p = 1
        else:
            c = 1

        if w2=="CryptoBit":
            c = 1


        image = cv2.imread("newinception.jpg")

        h,w = image.shape[0:2]
        image=cv2.resize(image,(w,h),interpolation=cv2.INTER_LINEAR)

        #putting text on our image
        cv2.putText(image,name,(1250,1000),cv2.FONT_HERSHEY_SIMPLEX ,3,(0,0,0),10,cv2.LINE_AA)
        cv2.putText(image,r_no,(1250,1130),cv2.FONT_HERSHEY_SIMPLEX,3,(0,0,0),10,cv2.LINE_AA)
        pyth = (1006,1773)
        andr = (2036,1773)
        cryp = (3125,1773)
        if p:
            cv2.circle(image,pyth, 30, (0,0,0),-2 )
        if a:
            cv2.circle(image,andr, 30, (0,0,0),-2 )
        if c:
            cv2.circle(image,cryp, 30, (0,0,0),-2 )

        #show
        #     cv2.imshow('image',image)

        #writing image to memory
        cv2.imwrite("image/"+r_no+".png", image)
