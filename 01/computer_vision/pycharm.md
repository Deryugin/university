Установка PyCharm и OpenCV на Debian
============================
Взято [отсюда](http://thelinuxfaq.com/296-how-to-install-pycharm-on-ubuntu-14-04-debian-7-linux-mint-17) и [отсюда](http://docs.opencv.org/doc/tutorials/introduction/linux_install/linux_install.html).

PyCharm
--------------
``` bash
wget -q -O - http://archive.getdeb.net/getdeb-archive.key

sudo sh -c 'echo "deb http://archive.getdeb.net/ubuntu trusty-getdeb apps" >> /etc/apt/sources.list.d/getdeb.list'

sudo apt-get update

sudo apt-get install pycharm
```

OpenCV
--------------
``` bash
# compiler
sudo apt-get install build-essential
# required
sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev libgtk2.0-dev
# optional
sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libjasper-dev libdc1394-22-dev

cd /tmp
git clone https://github.com/Itseez/opencv.git
cd opencv
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local ..
make
sudo make install
```



Всё готово!
