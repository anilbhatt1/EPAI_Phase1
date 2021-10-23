from PIL import Image
import os

def crop_process(img_name, folder_name, crop_type, crop_percent, crop_pixels):

    if folder_name is None and img_name is None:
        raise ValueError('Need one of the imputs - folder_name or img_name')
    elif folder_name is not None and img_name is not None:
        raise ValueError('Cant give both inputs together - either give folder_name or img_name to be converted')

    if folder_name is not None:
        if crop_type == 'crp_p':
            results = crop_folder(folder_name, crop_type, crop_percent)
        elif crop_type == 'crp_px':
            results = crop_folder(folder_name, crop_type, crop_pixels)
    else:
        if crop_type == 'crp_p':
            results = crop_image(img_name, crop_type, crop_percent)
        elif crop_type == 'crp_px':
            results = crop_image(img_name, crop_type, crop_pixels)

    return results

def crop_folder(folder_name, crop_type, crop_parm):

    pwd = os.getcwd()

    if os.path.exists(os.path.join(pwd, folder_name)):
        folder_path = os.path.join(pwd, folder_name)
    else:
        raise ValueError('Folder path doesnt exist : ', os.path.exists(os.path.join(pwd,folder_name)))

    save_path = os.path.join(pwd,'Cropped_images', folder_name+'_cropped')
    if os.path.exists(save_path):
        pass
    else:
        os.mkdir(save_path)

    modified_cnt = 0
    modified_images = []
    for file in os.listdir(folder_path):
        if file.split('.')[-1] == 'png' or file.split('.')[-1] == 'jpg' or file.split('.')[-1] == 'jpeg':
            im = Image.open(os.path.join(folder_path, file))
            if crop_type == 'crp_p':
                cropped_im = crp_p_process(im, crop_parm)
            elif crop_type == 'crp_px':
                cropped_im = crp_px_process(im, crop_parm)
            if cropped_im is not None:
                img_save_path = os.path.join(save_path, file)
                cropped_im.save(img_save_path)
                modified_cnt += 1
                modified_images.append(img_save_path)
            else:
                err_message = f'Couldnt resize the image {os.path.join(folder_path, file)} due to size mismatch'
                modified_images.append(err_message)
        else:
            pass

    return modified_cnt, modified_images


def crop_image(image_name, crop_type, crop_parm):

    pwd = os.getcwd()

    if os.path.exists(os.path.join(pwd, 'Sample_Images',image_name)):
        image_path = os.path.join(pwd, 'Sample_Images',image_name)
    else:
        raise ValueError('Image path doesnt exist : ', os.path.join(pwd, 'Sample_Images',image_name))

    save_path = os.path.join(pwd,'Cropped_images')
    if os.path.exists(save_path):
        pass
    else:
        os.mkdir(save_path)

    modified_images = []
    if image_name.split('.')[-1] == 'png' or image_name.split('.')[-1] == 'jpg' or image_name.split('.')[-1] == 'jpeg':
        im = Image.open(image_path)
        if crop_type == 'crp_p':
            cropped_im = crp_p_process(im, crop_parm)
        elif crop_type == 'crp_px':
            cropped_im = crp_px_process(im, crop_parm)
        if cropped_im is not None:
            img_save_path = os.path.join(save_path, image_name)
            cropped_im.save(img_save_path)
            modified_cnt = 1
            modified_images.append(img_save_path)
        else:
            modified_cnt = 0
            err_message = f'Couldnt resize the image {image_path} due to size mismatch'
            modified_images.append(err_message)

        return modified_cnt, modified_images
    else:
        raise ValueError('Image given should be in jpg/jpeg or png format')

def crp_p_process(im, percent):

    if percent is None:
        raise ValueError('Crop Percent must be provided for crop type of crp_p')
    elif percent == 0 or percent > 1:
        raise ValueError('Crop Percent supplied should be between 0 & 1')

    width, height = im.size
    remove = 1 - percent
    left = int(width * remove / 2)
    right = int(left + width * percent)
    upper = int(height * remove / 2)
    lower = int(upper + height * percent)
    crp_px = (left, upper, right, lower)
    if right > width or lower > height:
        im_crop = None
    else:
        im_crop = im.crop(crp_px)
    return im_crop

def crp_px_process(im, crp_px):

    if crp_px is None:
        raise ValueError('Crop Pixels must be provided for crop type of crp_px')

    if isinstance(crp_px, list) or isinstance(crp_px, tuple):
        pass
    else:
        raise ValueError('Crop Pixels provided must be in list format or tuple format for crop type of crp_px')

    width, height = im.size
    left, upper, right, lower = crp_px
    crop_height = lower - upper
    crop_width  = right - left
    if crop_width > width or crop_height > height:
        im_crop = None
    else:
        im_crop = im.crop(crp_px)
    return im_crop

def res_h_process(im, input_height):

    if input_height is None:
        raise ValueError('Resize height must be provided for resize type of res_h')
    elif input_height <= 1:
        raise ValueError('Resize height must be > 1')

    width, height = im.size
    w_h_ratio = width / height
    calc_width = input_height * w_h_ratio
    new_width, new_height = int(calc_width), int(input_height)
    im_new = im.resize((new_width, new_height), Image.LANCZOS)
    return im_new