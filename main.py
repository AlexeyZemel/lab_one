import os
from bs4 import BeautifulSoup
import requests
import re
from re import sub
from decimal import Decimal
import io
from datetime import datetime
import pandas as pd
import cv2
import urllib.request
import random

if not os.path.isdir('E:\dataset'):
    os.mkdir('E:\dataset')

if not os.path.isdir('E:\dataset\\brownbears'):
    os.mkdir('E:\dataset\\brownbears')

if not os.path.isdir('E:\dataset\polarbears'):
    os.mkdir('E:\dataset\polarbears')