import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
img2 = cv.imread('comparador2.jpg')

while(True):
    # Capturar frames.
    ret, img1 = cap.read()
    
    # Initiate SIFT detector
    sift = cv.xfeatures2d.SIFT_create()
    
    # Find the keypoints and descriptors with SIFT
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 0
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks=5)   # or pass empty dictionary

    flann = cv.FlannBasedMatcher(index_params,search_params)

    matches = flann.knnMatch(des1,des2,k=2)

    # Need to draw only good matches, so create a mask
    matchesMask = [[0,0] for i in xrange(len(matches))]

    # ratio test as per Lowe's paper
    for i,(m,n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            matchesMask[i]=[1,0]
    
    draw_params = dict(matchColor = (0,255,0),
                   singlePointColor = (255,0,0),
                   matchesMask = matchesMask,
                   flags = 0)

    img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,matches,None,**draw_params)
    
    #Mostrar imagen
    cv.imshow('Matching', img3)
    
    #Salir con ESC
    tecla = cv.waitKey(5) & 0xFF
    if tecla == 27:
        break

# When everything done, release the capture
cap.release()
cv.destroyAllWindows()
