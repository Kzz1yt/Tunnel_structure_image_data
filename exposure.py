import os
import cv2
import numpy as np
import shutil

def adjust_exposure(image, alpha=2.5):
    """
    调整图像的曝光度（亮度）。
    :param image: 输入的 OpenCV 图像
    :param alpha: 曝光增强系数 (默认 1.5 范围建议 1.0 - 3.0)
    :return: 曝光增强后的图像
    """
    return np.clip(image * alpha, 0, 255).astype(np.uint8)

def process_images(input_folder, exposure_strength=1.5):
    """
    遍历输入文件夹，处理所有 JPG/PNG 图片，提高曝光，并保存到新的文件夹。
    :param input_folder: 输入文件夹路径
    :param exposure_strength: 曝光增强强度
    """
    # 输出文件夹路径
    output_folder = os.path.join(os.path.dirname(input_folder), "data_exposure")

    # 如果目标文件夹存在，则删除
    if os.path.exists(output_folder):
        shutil.rmtree(output_folder)
    
    os.makedirs(output_folder, exist_ok=True)

    # 遍历输入文件夹中的所有图像
    for file_name in os.listdir(input_folder):
        if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
            img_path = os.path.join(input_folder, file_name)
            img = cv2.imread(img_path)
            
            if img is None:
                print(f"无法读取文件: {file_name}")
                continue
            
            # 处理图像
            adjusted_img = adjust_exposure(img, alpha=exposure_strength)

            # 生成新的文件名
            new_file_name = os.path.splitext(file_name)[0] + "_exp" + os.path.splitext(file_name)[1]
            output_path = os.path.join(output_folder, new_file_name)

            # 保存处理后的图像
            cv2.imwrite(output_path, adjusted_img)
            print(f"已处理: {file_name} -> {new_file_name}")

if __name__ == "__main__":
    input_dir = r""  # 替换为你的文件夹路径
    process_images(input_dir, exposure_strength=2.5)  # 调整 exposure_strength 以控制亮度