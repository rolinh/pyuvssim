#!/usr/bin/env python
# coding: utf-8

import argparse
import ssim
import utils

import os
try:
    import Image
except ImportError:
    from PIL import Image


def main():
    parser = argparse.ArgumentParser(prog="pyuvssim",
                                     description="Compares two YUV I420/IYUV raw video files using the SSIM metric")
    parser.add_argument('base_video', metavar='video1.yuv')
    parser.add_argument('comparison_video', metavar='video2.yuv')
    parser.add_argument('-W', '--width',
                        type=int,
                        action='store',
                        default=1920,
                        nargs='?',
                        help='video width in pixels')
    parser.add_argument('-H', '--height',
                        type=int,
                        action='store',
                        default=1080,
                        nargs='?',
                        help='video width in pixels')
    args = parser.parse_args()

    vid1 = args.base_video
    vid2 = args.comparison_video

    width = args.width
    height = args.height
    frame_size = width * height
    frame_weight = (frame_size * 3) / 2
    video_size = min(os.stat(vid1)[6], os.stat(vid2)[6])
    nb_frames = video_size / frame_weight

    print("Videos information:")
    print("width: {} px".format(width))
    print("height: {} px".format(height))
    print("frame size: {} px^2".format(frame_size))
    print("frame weight: {} ({})".format(utils.bytes2human(frame_weight), frame_weight))
    print("video size: {} ({})".format(utils.bytes2human(video_size), video_size))
    print("number of frames: {}\n".format(nb_frames))

    f1 = open(vid1, 'rb')
    f2 = open(vid2, 'rb')

    print("Pic #, SSIM value")
    for n in range(nb_frames):
        frame_offset = (n * frame_weight)
        im1 = Image.new("RGB", (width, height))
        im2 = Image.new("RGB", (width, height))
        pix1 = im1.load()
        pix2 = im2.load()
        # I420/IYUV: NxN Y plane, then (N/2)x(N/2) U and V planes
        for y in range(height):
            for x in range(width):
                pos_y = frame_offset + (y * width + x)
                pos_u = frame_offset + (y/2 * width/2 + x/2 + frame_size)
                pos_v = frame_offset + (y/2 * width/2 + x/2 + frame_size + frame_size/4)

                f1.seek(pos_y, 0)
                y1 = ord(f1.read(1))
                f1.seek(pos_u, 0)
                u1 = ord(f1.read(1))
                f1.seek(pos_v, 0)
                v1 = ord(f1.read(1))

                f2.seek(pos_y, 0)
                y2 = ord(f2.read(1))
                f2.seek(pos_u, 0)
                u2 = ord(f2.read(1))
                f2.seek(pos_v, 0)
                v2 = ord(f2.read(1))

                pix1[x, y] = utils.yuv2rgb(y1, u1, v1)
                pix2[x, y] = utils.yuv2rgb(y2, u2, v2)
        print("{}, {}".format(n, ssim.compute_ssim(im1, im2)))

    f1.close()
    f2.close()

if __name__ == '__main__':
    main()
