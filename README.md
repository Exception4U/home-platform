# HoME Platform

HoME is a platform for artificial agents to learn from vision, audio, semantics, physics, and interaction with objects and
other agents, all within a realistic context.

Check out the paper on Arxiv for more details: [HoME: a Household Multimodal Environment](https://arxiv.org/abs/1711.11017)

![alt tag](https://github.com/HoME-Platform/home-platform/raw/master/doc/images/overview.png)

## Dependencies

Main requirements:
- Python 2.7+ with Numpy, Scipy and Matplotlib
- [Panda3d](https://www.panda3d.org/) game engine for 3D rendering
- [EVERT](https://github.com/sbrodeur/evert) engine for 3D acoustic ray-tracing
- [PySoundFile](https://github.com/bastibe/PySoundFile) for Ogg Vorbis decoding

To install dependencies on Ubuntu operating systems:
```
sudo apt-get install python-pip python-dev build-essential libsndfile1
sudo pip2 install --upgrade pip numpy scipy matplotlib panda3d pysoundfile resampy nose coverage Pillow
```

(Packages `nose` and `coverage` are for tests only and can be omitted)

Finally you have to install EVERT. In order to do so, please follow the instructions over at 
https://github.com/sbrodeur/evert

## SUNCG Dataset

The Home environment is based on the [SUNCG](http://suncg.cs.princeton.edu/) dataset. To use the complete dataset of
45,000 houses, please follow the instruction mentioned on the SUNCG website.


## Installing the library

Download the source code from the git repository:
```
mkdir -p $HOME/work
cd $HOME/work
git clone https://github.com/HoME-Platform/home-platform.git
```

Note that the library must be in the PYTHONPATH environment variable for Python to be able to find it:
```
export PYTHONPATH=$HOME/work/home-platform:$PYTHONPATH 
```
This can also be added at the end of the configuration file $HOME/.bashrc

## Running unit tests

To ensure all libraries where correctly installed, it is advised to run the test suite:
```
cd $HOME/work/home-platform/tests
./run_tests.sh
```
Note that this can take some time.
