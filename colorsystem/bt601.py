from numpy import clip


def to_yuv(img_f):
    yuv_image = img_f.copy()

    yuv_image[:, :, 0] = 0.299 * img_f[:, :, 0] + 0.587 * img_f[:, :, 1] + 0.114 * img_f[:, :, 2]
    yuv_image[:, :, 1] = 0.4921 * (img_f[:, :, 2] - yuv_image[:, :, 0])
    yuv_image[:, :, 2] = 0.87732 * (img_f[:, :, 0] - yuv_image[:, :, 0])

    yuv_image[:, :, 0] = clip(yuv_image[:, :, 0], -1.000, 1.000)
    yuv_image[:, :, 1] = clip(yuv_image[:, :, 1], -1.000, 1.000)
    yuv_image[:, :, 2] = clip(yuv_image[:, :, 2], -1.000, 1.000)
    return yuv_image


def to_rgb(yuv_f):
    img_out = yuv_f.copy()
    img_out[:, :, 0] = yuv_f[:, :, 0] + 1.14 * yuv_f[:, :, 2]
    img_out[:, :, 1] = yuv_f[:, :, 0] - 0.395 * yuv_f[:, :, 1] - 0.581 * yuv_f[:, :, 2]
    img_out[:, :, 2] = yuv_f[:, :, 0] + 2.033 * yuv_f[:, :, 1]

    img_out[:, :, 0] = clip(img_out[:, :, 0], -1.000, 1.000)
    img_out[:, :, 1] = clip(img_out[:, :, 1], -1.000, 1.000)
    img_out[:, :, 2] = clip(img_out[:, :, 2], -1.000, 1.000)
    return img_out
