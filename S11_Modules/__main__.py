import p2j
import j2p
import image_resize
import image_crop
import argparse

def img_convert():
    if args.convert_type == 'p2j':
        conv_stats = p2j.p2j_convert(args.img_name, args.folder_name)
        return conv_stats
    elif args.convert_type == 'j2p':
        conv_stats = j2p.j2p_convert(args.img_name, args.folder_name)
        return conv_stats
    else:
        raise ValueError('Invalid Image conversion mode given :', args.convert_type)

def img_resize():
    if args.resize_type == 'res_p' or args.resize_type == 'res_w' or args.resize_type == 'res_h':
        resize_stats = image_resize.resize_process(args.img_name, args.folder_name, args.resize_type,
                                                   args.resize_percent, args.resize_width, args.resize_height)
        return resize_stats
    else:
        raise ValueError('Invalid Image Resize option given : ', args.resize_type)

def img_crop():
    if args.crop_type == 'crp_px' or 'crp_p':
        cropped_stats = image_crop.crop_process(args.img_name, args.folder_name, args.crop_type,
                                                args.crop_percent, args.crop_pixels)
        return cropped_stats
    else:
        raise ValueError('Invalid Image Crop option given :', args.crop_type)

if __name__ == '__main__':
    print('Running main module\n')

    parser = argparse.ArgumentParser(description='This app helps to convert image format, resize an image & crop an image, \
                                                  Use one of these commands : \
                                                  convert - To convert images from jpg/jpeg to png or viceversa, \
                                                  resize  - To resize the image, \
                                                  crop    - To crop the image')

    subparser = parser.add_subparsers(dest='command')
    convert   = subparser.add_parser('convert')
    resize    = subparser.add_parser('resize')
    crop      = subparser.add_parser('crop')

    convert.add_argument('--convert_type',type=str, help='Available modes - p2j, j2p', required=True)
    convert.add_argument('--img_name', type=str, help='Name of image to be converted')
    convert.add_argument('--folder_name', type=str, help='Folder name that holds images to be converted. It needs to be in same dir as python pgm.')

    resize.add_argument('--resize_type', type=str, help=' 1) res_p : To resize an image by determined percentage, \
                                                   2) res_w : To resize an image based on supplied width,  \
                                                   3) res_h : To resize an image based on supplied height',
                         required=True)
    resize.add_argument('--img_name', type=str, help='Name of image to be resized')
    resize.add_argument('--folder_name', type=str, help='Folder name that holds images to be resized. It needs to be in same dir as python pgm.')
    resize.add_argument('--resize_percent', type=float, help='Resize an image based on percentage value given between 0 and 1')
    resize.add_argument('--resize_width', type=float, help='Resize an image based on supplied width maintaining aspect ratio')
    resize.add_argument('--resize_height', type=float, help='Resize an image based on supplied height maintaining aspect ratio')

    crop.add_argument('--crop_type', type=str,
                       help=' 1) crp_px : To Crop an image based on pixel positions given as -> left, upper, right, lower \
                              2) crp_p  : To Crop an image based on percentage', required=True)
    crop.add_argument('--img_name', type=str, help='Name of image OR Folder name that holds images')
    crop.add_argument('--folder_name', type=str, help='Folder name that holds images to be resized. It needs to be in same dir as python pgm.')
    crop.add_argument('--crop_pixels', type=int, nargs=4, help='Crop an image based on pixel positions given as -> left, upper, right, lower')
    crop.add_argument('--crop_percent', type=float, help='Crop an image based on percentage value given between 0 and 1')

    args=parser.parse_args()

    if args.command == 'convert':
        out_stats = img_convert()
    elif args.command == 'resize':
         out_stats = img_resize()
    elif args.command == 'crop':
        out_stats = img_crop()
    else:
        raise ValueError(args.command , ' : Invalid command given')

    print(f'{args.command} completed successfully.\n')
    if args.command == 'convert':
        print(f'{args.command} : {args.convert_type}\n')
    elif args.command == 'resize':
        print(f'{args.command} : {args.resize_type}, Parameters - %: {args.resize_percent}, w : {args.resize_width}, h : {args.resize_height}\n')
    print(f'No: of images {args.command}ed : {out_stats[0]}\n')
    print(f'No: of images NOT {args.command}ed : {len(out_stats[1]) - out_stats[0]}\n')
    print(f'{args.command}ed image/s can be found in below location :\n')
    for num, saved_path in enumerate(out_stats[1], 1):
        print(f'{num} : {saved_path}')