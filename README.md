# Live Migration
=========
Experiments done on machines gr120 and gr121 at AIST

## Structure
* /scripts
* /shared
* /vmanage/controller/congestor   : script for congestion  
  /exp         : script for experiments  
  /multiple.py : controller for multiple VMs with migrator included

```python
    ./multiple.py -s [schedule] -v [vm window] -g [number of parallel connections for gridftp]
    where schedule is one of lf(largest first), sf(smallest first), rand(randomly chosen) VM scheduling algorithm and
          vm window 0 indicates controller
```

controller
- single
- multiple: multple.py

experiments
- exp

# node memory distributon
# total of 30VMs
node1 (4/4GB): 512MB, 512MB, 1GB, and 2GB
node2 (6/4GB): 512MB, 512MB, 512MB, 512MB, 1GB, and 1GB
node3 (8/4GB): 512MB, 512MB, 512MB, 512MB, 512MB, 512MB, 512MB, and 512MB
node4 (4/4GB): 1GB, 1GB, 1GB and 1GB
node5 (3/4GB): 1GB, 1GB and 2GB
node6 (2/4GB): 1GB and 3GB
node7 (2/4GB): 2GB and 2GB
node8 (1/4GB): 4GB


Pyechonest is an open source Python library for the Echo Nest API.  With Pyechonest you have Python access to the entire set of API methods including:

* **artist** - search for artists by name, description, or attribute, and get back detailed information about any artist including audio, similar artists, blogs, familiarity, hotttnesss, news, reviews, urls and video.
* **song** - search songs by artist, title, description, or attribute (tempo, duration, etc) and get detailed information back about each song, such as hotttnesss, audio_summary, or tracks.
* **track** - upload a track to the Echo Nest and receive summary information about the track including key, duration, mode, tempo, time signature along with detailed track info including timbre, pitch, rhythm and loudness information.

## Install
There are a few different ways you can install pyechonest:

* Use setuptools: `easy_install -U pyechonest`
* Download the zipfile from the [downloads](https://github.com/echonest/pyechonest/archives/master) page and install it. 
* Checkout the source: `git clone git://github.com/echonest/pyechonest.git` and install it yourself.
   
## Getting Started
* Install Pyechonest
* **Get an API key** - to use the Echo Nest API you need an Echo Nest API key.  You can get one for free at [developer.echonest.com](http://developer.echonest.com).
* **Set the API** key - you can do this one of two ways:
* set an environment variable named `ECHO_NEST_API_KEY` to your API key
* Include this snippet of code at the beginning of your python scripts:

```python
    from pyechonest import config
    config.ECHO_NEST_API_KEY="YOUR API KEY"
```

* Check out the [docs](http://echonest.github.com/pyechonest/) and examples below.

## Examples
*All examples assume you have already setup your api key!*

Find artists that are similar to 'Bikini Kill':

```python
from pyechonest import artist
bk = artist.Artist('bikini kill')
print "Artists similar to: %s:" % (bk.name,)
for similar_artist in bk.similar: print "\t%s" % (similar_artist.name,)
```
