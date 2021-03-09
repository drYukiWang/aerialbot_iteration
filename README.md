# ærialbot

For the aerialbot project, please refer [here](https://github.com/doersino/aerialbot) 

# aerialbot_iteration

## Usage

### Setup

I recommed using `conda` to create and manage a virtual environment. To create a new virtual environment and install all required dependencies:

```bash
$ git clone https://github.com/doersino/aerialbot
$ conda create --name <ENVNAME>
$ cd aerialbot
$ conda activate <ENVNAME>
$ pip install -r requirements.txt
```

### Configuration

Copy `config.sample.ini` to `config.ini`, open it and modify it based on the (admittedly wordy) instructions in the comments.


### Running

Once you've set everything up and configured it to your liking, run:

```bash
$ python aerialbot.py

Enter the latitude longitude of the reference central point and the length of the interested square and the number that divides the length into grid cells, e.g., if you intend to scan a 5km X 5km area into 10X10 grid cells around a central point(21.255079,79.163345), then enter the following then hit `return` 
 
$ 21.255079 79.163345 5 10 

Enter the name of the cluster that is used for naming the image directory then hit `return`, e.g.,

$ Nagpur

Then you will have 100 images downloaded in the `Nagpur` folder.
```

That's basically it!