import pytest
import os
from PIL import Image
import numpy as np
#import convert_app
import subprocess

# what is "value" given in "value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)" ?
   # Answer :
    # Sample value when test_j2p fails
        # CompletedProcess(args='python convert_app/j2p convert --convert_type j2p --img_name sample_jpg.jpg', returncode=2, stdout=b'', stderr=b"python: can't open file 'C:\\Users\\anila\\Desktop\\AI\\EPAI-Phase1\\S11_Modules\\convert_app\\j2p': [Errno 2] No such file or directory\n")
    # Sample value when test_j2p success
        # CompletedProcess(args='python convert_app convert --convert_type j2p --img_name sample_jpg.jpg', returncode=0, stdout=b'Running main module\r\n\r\nconvert completed successfully.\r\n\r\nconvert : j2p\r\n\r\nNo: of images converted : 1\r\n\r\nNo: of images NOT converted : 0\r\n\r\nconverted image/s can be found in below location :\r\n\r\n1 : C:\\Users\\anila\\Desktop\\AI\\EPAI-Phase1\\S11_Modules\\Converted_png_images\\sample_jpg.png\r\n', stderr=b'')

def test_j2p():
    cmd = 'python convert_app.zip convert --convert_type j2p --img_name sample_jpg.jpg'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value)
    assert value.returncode == 0, 'Error in image formatting from jpg to png'

def test_p2j():
    cmd = 'python convert_app.zip convert --convert_type p2j --img_name sample_png.png'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode == 0, 'Error in image formatting from png to jpg'

def test_resize_percent():
    cmd = 'python convert_app.zip resize --resize_type res_p --resize_percent 0.75 --img_name sample_png.png'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stdout)
    assert value.returncode == 0, 'Error in image percent resizing'

def test_resize_width():
    cmd = 'python convert_app.zip resize --resize_type res_w --resize_width 95 --img_name sample_jpeg.jpeg'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stdout)
    assert value.returncode == 0, 'Error in image width resizing'

def test_resize_height():
    cmd = 'python convert_app.zip resize --resize_type res_h --resize_height 195 --img_name sample_jpg.jpg'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stdout)
    assert value.returncode == 0, 'Error in image height resizing'

def test_crop_percent():
    cmd = 'python convert_app.zip crop --crop_type crp_p --crop_percent 0.695 --img_name sample_png.png'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stdout)
    assert value.returncode == 0, 'Error in image percent cropping'

def test_crop_pixel():
    cmd = 'python convert_app.zip crop --crop_type crp_px --crop_pixel 20 25 200 100 --img_name sample_jpg.jpg'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stdout)
    assert value.returncode == 0, 'Error in image pixel cropping'

def test_j2p_folder():
    cmd = 'python convert_app.zip convert --convert_type j2p --folder_name Sample_Images'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value)
    assert value.returncode == 0, 'Error in folder formatting from jpg to png'

def test_p2j_folder():
    cmd = 'python convert_app.zip convert --convert_type p2j --folder_name Sample_Images'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode == 0, 'Error in folder formatting from png to jpg'

def test_resize_percent_folder():
    cmd = 'python convert_app.zip resize --resize_type res_p --resize_percent 0.75 --folder_name Sample_Images'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stdout)
    assert value.returncode == 0, 'Error in folder percent resizing'

def test_resize_width_folder():
    cmd = 'python convert_app.zip resize --resize_type res_w --resize_width 95 --folder_name Sample_Images'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stdout)
    assert value.returncode == 0, 'Error in folder width resizing'

def test_resize_height_folder():
    cmd = 'python convert_app.zip resize --resize_type res_h --resize_height 195 --folder_name Sample_Images'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stdout)
    assert value.returncode == 0, 'Error in folder height resizing'

def test_crop_percent_folder():
    cmd = 'python convert_app.zip crop --crop_type crp_p --crop_percent 0.695 --folder_name Sample_Images'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stdout)
    assert value.returncode == 0, 'Error in folder percent cropping'

def test_crop_pixel_folder():
    cmd = 'python convert_app.zip crop --crop_type crp_px --crop_pixel 20 25 200 100 --folder_name Sample_Images'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stdout)
    assert value.returncode == 0, 'Error in folder pixel cropping'

def test_j2p_img_not_found():
    cmd = 'python convert_app.zip convert --convert_type j2p --img_name sample_jpg1.jpg'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in image formatting from jpg to png'

def test_p2j_img_not_found():
    cmd = 'python convert_app.zip convert --convert_type p2j --img_name sample_png1.png'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in image formatting from png to jpg'

def test_resize_percent_img_not_found():
    cmd = 'python convert_app.zip resize --resize_type res_p --resize_percent 0.75 --img_name sample_png1.png'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in image percent resizing'

def test_resize_width_img_not_found():
    cmd = 'python convert_app.zip resize --resize_type res_w --resize_width 95 --img_name sample_jpeg1.jpeg'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in image width resizing'

def test_resize_height_img_not_found():
    cmd = 'python convert_app.zip resize --resize_type res_h --resize_height 195 --img_name sample_jpg1.jpg'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in image height resizing'

def test_crop_percent_img_not_found():
    cmd = 'python convert_app.zip crop --crop_type crp_p --crop_percent 0.695 --img_name sample_png1.png'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in image percent cropping'

def test_crop_pixel_img_not_found():
    cmd = 'python convert_app.zip crop --crop_type crp_px --crop_pixel 20 25 200 100 --img_name sample_jpg1.jpg'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in image pixel cropping'

def test_j2p_folder_not_found():
    cmd = 'python convert_app.zip convert --convert_type j2p --folder_name Sample_Images1'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in folder formatting from jpg to png'

def test_p2j_folder_not_found():
    cmd = 'python convert_app.zip convert --convert_type p2j --folder_name Sample_Images1'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in folder formatting from png to jpg'

def test_resize_percent_folder_not_found():
    cmd = 'python convert_app.zip resize --resize_type res_p --resize_percent 0.75 --folder_name Sample_Images1'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in folder percent resizing'

def test_resize_width_folder_not_found():
    cmd = 'python convert_app.zip resize --resize_type res_w --resize_width 95 --folder_name Sample_Images1'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in folder width resizing'

def test_resize_height_folder_not_found():
    cmd = 'python convert_app.zip resize --resize_type res_h --resize_height 195 --folder_name Sample_Images1'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in folder height resizing'

def test_crop_percent_folder_not_found():
    cmd = 'python convert_app.zip crop --crop_type crp_p --crop_percent 0.695 --folder_name Sample_Images1'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in folder percent cropping'

def test_crop_pixel_folder_not_found():
    cmd = 'python convert_app.zip crop --crop_type crp_px --crop_pixel 20 25 200 100 --folder_name Sample_Images1'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in folder pixel cropping'

def test_j2p_non_jpg_given():
    cmd = 'python convert_app.zip convert --convert_type j2p --img_name sample_png.png'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in image formatting from jpg to png'

def test_p2j_non_png_given():
    cmd = 'python convert_app.zip convert --convert_type p2j --img_name sample_jpg.jpg'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in image formatting from png to jpg'

def test_resize_zero_percent():
    cmd = 'python convert_app.zip resize --resize_type res_p --resize_percent 0 --img_name sample_png.png'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in image percent resizing'

def test_resize_gt_one_percent():
    cmd = 'python convert_app.zip resize --resize_type res_p --resize_percent 50 --img_name sample_png.png'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in image percent resizing'

def test_resize_width_decimal():
    cmd = 'python convert_app.zip resize --resize_type res_w --resize_width 0.95 --img_name sample_jpeg.jpeg'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in image width resizing'

def test_resize_height_negative():
    cmd = 'python convert_app.zip resize --resize_type res_h --resize_height -195 --img_name sample_jpg.jpg'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in image height resizing'

def test_crop_zero_percent():
    cmd = 'python convert_app.zip crop --crop_type crp_p --crop_percent 0 --img_name sample_png.png'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in image percent cropping'

def test_crop_gt_one_percent():
    cmd = 'python convert_app.zip crop --crop_type crp_p --crop_percent 1.695 --img_name sample_png.png'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert value.returncode != 0, 'Error in image percent cropping'

def test_crop_pixel_incompatible_size():
    pwd = os.getcwd()
    if os.path.exists(os.path.join(pwd, 'Cropped_Images', 'sample_jpg.jpg')):
        os.remove(os.path.join(pwd, 'Cropped_Images', 'sample_jpg.jpg'))
    cmd = 'python convert_app.zip crop --crop_type crp_px --crop_pixel 20 25 250 150 --img_name sample_jpg.jpg'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stderr)
    assert os.path.exists(os.path.join(pwd, 'Cropped_Images', 'sample_jpg.jpg')) == 0, 'Error in image pixel cropping'

def test_crop_pixel_square():
    cmd = 'python convert_app.zip crop --crop_type crp_px --crop_pixel 20 25 90 95 --img_name sample_jpg.jpg'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(value.stdout)
    assert value.returncode == 0, 'Error in image pixel cropping'

def test_j2p_bulk():
    pwd = os.getcwd()
    cmd = 'python convert_app.zip convert --convert_type j2p --folder_name Sample_Images'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    cnt = 0
    for _ in os.listdir(os.path.join(pwd, 'Converted_png_images', 'Sample_Images_converted')):
        cnt +=1
    assert cnt == 28, 'Count of jpg/jpeg to png conversions not matching'

def test_resize_percent_bulk():
    pwd = os.getcwd()
    cmd = 'python convert_app.zip resize --resize_type res_p --resize_percent 0.8 --folder_name Sample_Images'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    im = Image.open((os.path.join(pwd, 'Resized_images', 'Sample_Images_resized', 'val_99.JPEG')))
    assert np.array(im).shape == (851, 851, 3), 'Resize not happening correctly'
    cnt = 0
    for _ in os.listdir(os.path.join(pwd, 'Resized_images', 'Sample_Images_resized')):
        cnt +=1
    assert cnt == 32, 'Count of resized images not matching'

def test_resize_width_bulk():
    pwd = os.getcwd()
    cmd = 'python convert_app.zip resize --resize_type res_w --resize_width 500 --folder_name Sample_Images'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    im1 = Image.open((os.path.join(pwd, 'Resized_images', 'Sample_Images_resized', 'val_99.JPEG')))
    im2 = Image.open((os.path.join(pwd, 'Resized_images', 'Sample_Images_resized', 'resized_jpg.jpg')))
    assert np.array(im1).shape == (500, 500, 3), 'Resize not happening correctly for im1'
    assert np.array(im2).shape == (280, 500, 3), 'Resize not happening correctly for im2'
    cnt = 0
    for _ in os.listdir(os.path.join(pwd, 'Resized_images', 'Sample_Images_resized')):
        cnt +=1
    assert cnt == 32, 'Count of resized images not matching'

def test_resize_height_bulk():
    pwd = os.getcwd()
    cmd = 'python convert_app.zip resize --resize_type res_h --resize_height 500 --folder_name Sample_Images'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    im1 = Image.open((os.path.join(pwd, 'Resized_images', 'Sample_Images_resized', 'val_99.JPEG')))
    im2 = Image.open((os.path.join(pwd, 'Resized_images', 'Sample_Images_resized', 'resized_jpg.jpg')))
    assert np.array(im1).shape == (500, 500, 3), 'Resize not happening correctly for im1'
    assert np.array(im2).shape == (500, 892, 3), 'Resize not happening correctly for im2'
    cnt = 0
    for _ in os.listdir(os.path.join(pwd, 'Resized_images', 'Sample_Images_resized')):
        cnt +=1
    assert cnt == 32, 'Count of resized images not matching'

def test_crop_pixels_bulk():
    pwd = os.getcwd()
    cmd = 'python convert_app.zip crop --crop_type crp_px --crop_pixels 420 420 644 644 --folder_name Sample_Images_Crop_Test'
    value = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    resized_image_dir = os.path.join(pwd, 'Cropped_images', 'Sample_Images_Crop_Test_cropped')
    cnt = 0
    for idx, file in enumerate(os.listdir(resized_image_dir),1):
        cnt +=1
        im = Image.open((os.path.join(resized_image_dir, file)))
        assert np.array(im).shape == (224, 224, 3), f'Resize not happening correctly for image # {idx}, name # {file}'
    assert cnt == 21, 'Count of resized images not matching'