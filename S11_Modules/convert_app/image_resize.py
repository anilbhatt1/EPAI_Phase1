from PIL import Image
import os

def resize_process(img_name, folder_name, resize_type, resize_percent, resize_width, resize_height):

    if folder_name is None and img_name is None:
        raise ValueError('Need one of the imputs - folder_name or img_name')
    elif folder_name is not None and img_name is not None:
        raise ValueError('Cant give both inputs together - either give folder_name or img_name to be converted')

    if folder_name is not None:
        if resize_type == 'res_p':
            results = resize_folder(folder_name, resize_type, resize_percent)
        elif resize_type == 'res_w':
            results = resize_folder(folder_name, resize_type, resize_width)
        elif resize_type == 'res_h':
            results = resize_folder(folder_name, resize_type, resize_height)
    else:
        if resize_type == 'res_p':
            results = resize_image(img_name, resize_type, resize_percent)
        elif resize_type == 'res_w':
            results = resize_image(img_name, resize_type, resize_width)
        elif resize_type == 'res_h':
            results = resize_image(img_name, resize_type, resize_height)

    return results

def resize_folder(folder_name, resize_type, resize_parm):

    pwd = os.getcwd()

    if os.path.exists(os.path.join(pwd, folder_name)):
        folder_path = os.path.join(pwd, folder_name)
    else:
        raise ValueError('Folder path doesnt exist : ', os.path.exists(os.path.join(pwd,folder_name)))

    save_path = os.path.join(pwd,'Resized_images', folder_name+'_resized')
    if os.path.exists(save_path):
        pass
    else:
        os.mkdir(save_path)

    modified_cnt = 0
    modified_images = []
    for file in os.listdir(folder_path):
        if file.split('.')[-1] == 'png' or file.split('.')[-1] == 'jpg' or file.split('.')[-1] == 'jpeg':
            im = Image.open(os.path.join(folder_path, file))
            if resize_type == 'res_p':
                resized_im = res_p_process(im, resize_parm)
            elif resize_type == 'res_w':
                resized_im = res_w_process(im, resize_parm)
            elif resize_type == 'res_h':
                resized_im = res_h_process(im, resize_parm)
            img_save_path = os.path.join(save_path, file)
            resized_im.save(img_save_path)
            modified_cnt += 1
            modified_images.append(img_save_path)
        else:
            pass

    return modified_cnt, modified_images


def resize_image(image_name, resize_type, resize_parm):

    pwd = os.getcwd()

    if os.path.exists(os.path.join(pwd, 'Sample_Images',image_name)):
        image_path = os.path.join(pwd, 'Sample_Images',image_name)
    else:
        raise ValueError('Image path doesnt exist : ', os.path.join(pwd, 'Sample_Images',image_name))

    save_path = os.path.join(pwd,'Resized_images')
    if os.path.exists(save_path):
        pass
    else:
        os.mkdir(save_path)

    modified_images = []
    if image_name.split('.')[-1] == 'png' or image_name.split('.')[-1] == 'jpg' or image_name.split('.')[-1] == 'jpeg':
        im = Image.open(image_path)
        if resize_type == 'res_p':
            resized_im = res_p_process(im, resize_parm)
        elif resize_type == 'res_w':
            resized_im = res_w_process(im, resize_parm)
        elif resize_type == 'res_h':
            resized_im = res_h_process(im, resize_parm)
        img_save_path = os.path.join(save_path, image_name)
        resized_im.save(img_save_path)
        modified_cnt = 1
        modified_images.append(img_save_path)

        return modified_cnt, modified_images
    else:
        raise ValueError('Image given should be in jpg/jpeg or png format')

def res_p_process(im, percent):

    if percent is None:
        raise ValueError('Resize Percent must be provided for resize type of res_p')
    elif percent == 0 or percent > 1:
        raise ValueError('Resize Percent supplied should be between 0 & 1')

    new_width, new_height = int(im.size[0] * percent), int(im.size[1] * percent)
    im_new = im.resize((new_width, new_height), Image.LANCZOS)
    return im_new

def res_w_process(im, input_width):

    if input_width is None:
        raise ValueError('Resize Width must be provided for resize type of res_w')
    elif input_width <= 1:
        raise ValueError('Resize width must be > 1')

    width, height = im.size
    w_h_ratio = width / height
    calc_height = input_width / w_h_ratio
    new_width, new_height = int(input_width), int(calc_height)
    im_new = im.resize((new_width, new_height), Image.LANCZOS)
    return im_new

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