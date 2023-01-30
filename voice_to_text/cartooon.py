import cv2
def cartooify(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray =cv2.medianBlur(gray,5)
    edges = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
    color = cv2.bilateralFilter(img,9,300,300)
    catroon = cv2.bitwise_and(color,color,mask=edges)
    return catroon
if __name__ == "__main__":
    img = cv2.imread(r"H:\vijay rana\Green Abstract Health Care YouTube Thumbnail.png")
    cartoon = cartooify(img)
    cv2.imshow("cartoon",cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()