from logging import root
from Plotwarts import RonPLotWheasley
import os

root_path_to_img = "./static/images/"
png = ".png"

def GetList(Req, age_tag):

    return RonPLotWheasley().Generate_plots_for_person_X(Req, age_tag)


