import numpy as np
import cv2

def show(img: np.ndarray, scale=None):
    """Show image after scaling

    Parameters
    ----------
    img: np.ndarray
        Image
    scale: float
        Scale from 0 to 100
    """
    if scale is not None:
        h,w = img.shape[0], img.shape[1]
        h_small, w_small = int(h*scale/100) , int(w*scale/100)
        img = cv2.resize(img, (w_small, h_small))
    cv2.imshow("image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# One time function
def get_pad_and_mask(h,w,scale):
    dh = int(scale*h)
    dw = int(scale*w)
    pad = np.zeros((h+2*dh, w+2*dw, 3)).astype(np.float32)
    mask = np.copy(pad)
    whites = np.ones((h,w,3))
    mask[dh:h+dh, dw:w+dw, :] = whites
    return pad, mask

# One time function
def get_rot_axis(h,w,scale):
    rot_axis_x = scale*w
    rot_axis_y = scale*h + h
    return (rot_axis_x, rot_axis_y)

def add_padding(img, padding):
    """Add padding to the given image"""
    dh = int((padding.shape[0]-img.shape[0])/2)
    dw = int((padding.shape[1]-img.shape[1])/2)

    h = int(img.shape[0])
    w = int(img.shape[1])

    padding[dh:h+dh,dw:w+dw,:]=img
    return padding

def rotate_and_shift(image, mask, angle, axis, shift):
  rot_mat = cv2.getRotationMatrix2D(axis, angle, 1.0)
  rot_mat[:,2] += np.array([0,shift]) 

  rot_image = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  rot_mask = cv2.warpAffine(mask, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return rot_image, rot_mask

def to_degrees(radian):
    return radian*(180/np.pi)