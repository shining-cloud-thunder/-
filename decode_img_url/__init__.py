import pyzbar.pyzbar as pyzbar
from PIL import Image


def decode_qr_code(image_path):
    """给定图片路径, 解析其中的二维码"""

    # 打开指定路径下的二维码文件
    img = Image.open(image_path)

    # 将彩色图像转换为灰度图像是提高解码成功率的一种方法
    gray_img = img.convert('L')

    # 对图像进行解码操作
    decoded_objects = pyzbar.decode(gray_img)

    results = []
    for obj in decoded_objects:
        result = {
            "type": obj.type,
            "data": obj.data.decode("utf-8"),
            # "quality": obj.quality,
            "rect": obj.rect
        }
        results.append(result)

    return results

#
# if __name__ == "__main__":
    # qrcode_path = 'testUrlImg.png'
    # qr_codes_info = decode_qr_code(qrcode_path)
    # for info in qr_codes_info:
    #     print(f"类型: {info['type']}, 数据: {info['data']}")