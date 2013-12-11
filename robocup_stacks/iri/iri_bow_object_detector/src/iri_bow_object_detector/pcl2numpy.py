from sensor_msgs.msg import PointCloud2
import numpy as np
import struct
import time

def get_auto(data, wants, flipit=True):
    resolution = (data.height, data.width)
    img = np.fromstring(data.data, np.float32)
    step=img.shape[0]/(data.height*data.width)
    ret = []
    for w, p in wants:
        if w=="pos":
            x = img[p::step].reshape(resolution)
            y = img[p+1::step].reshape(resolution)
            z = img[p+2::step].reshape(resolution) 
            if flipit:
                x    = np.flipud(x) 
                y    = np.flipud(y)
                z    = np.flipud(z)
            ret.extend([x, y, z])
        elif w=="rgb":
            rgb = img[p::step]
            r = np.zeros(data.height*data.width)
            g = np.zeros(data.height*data.width)
            b = np.zeros(data.height*data.width)
            for i in range(rgb.shape[0]):
                int_rgb = struct.unpack('i', struct.pack('f', rgb[i]))[0]
                r[i] = (int_rgb & 0xff0000) >> 16
                g[i] = (int_rgb & 0xff00) >> 8
                b[i] = (int_rgb & 0xff)
            r = r.reshape(resolution)
            g = g.reshape(resolution)
            b = b.reshape(resolution)
            if flipit:
                r = np.flipud(r)
                g = np.flipud(g)
                b = np.flipud(b)
            gray = (0.30*r+0.59*g+0.11*b).astype('uint8')
            ret.extend([r,g,b,gray])
        elif w=="norm":
            n_x = img[p::step].reshape(resolution)
            n_y = img[p+1::step].reshape(resolution)
            n_z = img[p+2::step].reshape(resolution)
            if flipit:
                n_x = np.flipud(n_x)
                n_y = np.flipud(n_y)
                n_z = np.flipud(n_z)
            ret.extend([n_x, n_y, n_z])
        elif w=="curv":
            curv = img[p::step].reshape(resolution)
            if flipit:
                curv = np.flipud(curv)
            ret.extend([curv])
    return ret

def get_pos_rgb(data):
    resolution = (data.height, data.width)
    # 3D position for each pixel
    img = np.fromstring(data.data, np.float32)

    x = img[0::8].reshape(resolution)
    y = img[1::8].reshape(resolution)
    z = img[2::8].reshape(resolution) 
    rgb = img[4::8]
    r = np.zeros(data.height*data.width)
    g = np.zeros(data.height*data.width)
    b = np.zeros(data.height*data.width)
    for i in range(rgb.shape[0]):
        int_rgb = struct.unpack('i', struct.pack('f', rgb[i]))[0]
        r[i] = (int_rgb & 0xff0000) >> 16
        g[i] = (int_rgb & 0xff00) >> 8
        b[i] = (int_rgb & 0xff)
    r = r.reshape(resolution)
    g = g.reshape(resolution)
    b = b.reshape(resolution)
    x    = np.flipud(x)
    y    = np.flipud(y)
    z    = np.flipud(z)
    return (x, y, z, r, g, b)

def get_pos_rgb_gray(data):
    resolution = (data.height, data.width)
    # 3D position for each pixel
    img = np.fromstring(data.data, np.float32)

    x = img[0::8].reshape(resolution)
    y = img[1::8].reshape(resolution)
    z = img[2::8].reshape(resolution) 
    rgb = img[4::8]
    r = np.zeros(data.height*data.width)
    g = np.zeros(data.height*data.width)
    b = np.zeros(data.height*data.width)
    for i in range(rgb.shape[0]):
        int_rgb = struct.unpack('i', struct.pack('f', rgb[i]))[0]
        r[i] = (int_rgb & 0xff0000) >> 16
        g[i] = (int_rgb & 0xff00) >> 8
        b[i] = (int_rgb & 0xff)
    r = r.reshape(resolution)
    g = g.reshape(resolution)
    b = b.reshape(resolution)
    x    = np.flipud(x)
    y    = np.flipud(y)
    z    = np.flipud(z)
    gray = np.flipud(0.30*r+0.59*g+0.11*b).astype('uint8')
    return (x, y, z, r, g, b, gray)


def get_pos_rgb_gray_norm(data):
    resolution = (data.height, data.width)
    # 3D position for each pixel
    img = np.fromstring(data.data, np.float32)
    
    print img.shape
    x = img[0::12].reshape(resolution)
    y = img[1::12].reshape(resolution)
    z = img[2::12].reshape(resolution) 
    n_x = img[4::12].reshape(resolution)
    n_y = img[5::12].reshape(resolution)
    n_z = img[6::12].reshape(resolution)
    rgb = img[8::12]
    r = np.zeros(data.height*data.width)
    g = np.zeros(data.height*data.width)
    b = np.zeros(data.height*data.width)
    curv = img[9::12].reshape(resolution)
    for i in range(rgb.shape[0]):
        int_rgb = struct.unpack('i', struct.pack('f', rgb[i]))[0]
        r[i] = (int_rgb & 0xff0000) >> 16
        g[i] = (int_rgb & 0xff00) >> 8
        b[i] = (int_rgb & 0xff)
    r = r.reshape(resolution)
    g = g.reshape(resolution)
    b = b.reshape(resolution)

    x    = np.flipud(x)
    y    = np.flipud(y)
    z    = np.flipud(z)
    n_x  = np.flipud(n_x)
    n_y  = np.flipud(n_y)
    n_z  = np.flipud(n_z)
    curv = np.flipud(curv)
    gray = np.flipud(0.30*r+0.59*g+0.11*b).astype('uint8')

    return (x, y, z, n_x, n_y, n_z, r, g, b, curv, gray)
