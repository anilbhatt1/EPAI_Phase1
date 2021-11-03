from PIL import Image
import os

def j2p_convert(img_name, folder_name):

    if folder_name is None and img_name is None:
        raise ValueError('Need one of the imputs - folder_name or img_name')
    elif folder_name is not None and img_name is not None:
        raise ValueError('Cant give both inputs together - either give folder_name or img_name to be converted')
    elif folder_name is not None:
        results = j2p_convert_folder(folder_name)
    else:
        results = j2p_convert_image(img_name)

    return results

def j2p_convert_folder(folder_name):

    pwd = os.getcwd()

    if os.path.exists(os.path.join(pwd, folder_name)):
        folder_path = os.path.join(pwd, folder_name)
    else:
        raise ValueError('Folder path doesnt exist : ', os.path.exists(os.path.join(pwd,folder_name)))

    save_path = os.path.join(pwd,'Converted_png_images', folder_name+'_converted')
    if os.path.exists(save_path):
        pass
    else:
        os.mkdir(save_path)

    modified_cnt = 0
    modified_images = []
    for file in os.listdir(folder_path):
        if file.split('.')[-1] == 'jpg' or file.split('.')[-1] == 'jpeg':
            im = Image.open(os.path.join(folder_path, file))
            rgba_im=im.convert('RGBA')
            file_name = file.split('.')[0] + '.png'
            img_save_path = os.path.join(save_path, file_name)
            rgba_im.save(img_save_path)
            modified_cnt += 1
            modified_images.append(img_save_path)
        else:
            pass

    return modified_cnt, modified_images

def j2p_convert_image(image_name):

    pwd = os.getcwd()

    if os.path.exists(os.path.join(pwd, 'Sample_Images',image_name)):
        image_path = os.path.join(pwd, 'Sample_Images',image_name)
    else:
        raise ValueError('Image path doesnt exist : ', os.path.join(pwd, 'Sample_Images',image_name))

    save_path = os.path.join(pwd, 'Converted_png_images')
    if os.path.exists(save_path):
        pass
    else:
        os.mkdir(save_path)

    modified_images = []
    im = Image.open(image_path)
    rgba_im = im.convert('RGBA')
    file_name = image_name.split('.')[0] + '.png'
    img_save_path = os.path.join(save_path, file_name)
    rgba_im.save(img_save_path)
    modified_cnt = 1
    modified_images.append(img_save_path)

    return modified_cnt, modified_images