# SYNOPSIS

`pyuvssim` computes the structural similarity (SSIM) between each frames of two
raw YUV videos. As the name implies, it is written in `python` and for what it
is, it is just slow as hell. Seriously. This code is just a proof of concept and
*shall not be used* to compute SSIM between two videos. Its main purpose is
only to be read by people interested to see how SSIM can be computed between
two videos as `python` is pretty straightforward to read.

If you need to compute SSIM between two raw YUV videos, I suggest you have a
look at `VQMT` (see project on [Github](https://github.com/Rolinh/VQMT)) which
is written in `C++`, uses `OpenCV`, performs way better (in the magnitude order
of 1:100) and can provide other metrics as well (PSNR, VIFp, ...).

The SSIM module credits go to [pyssim](https://github.com/jterrace/pyssim).
