import os
from . models import Movie

#TODO: change path
with open('C:/Users/Juan/Desktop/movies.txt') as movie_file:
    for line in movie_file:
        print(line)
        cur_movie = line.split(', ')
        m = Movie(title=cur_movie[0],year=cur_movie[1],director=cur_movie[2],actors=cur_movie[3],link=cur_movie[4],genre=cur_movie[5],img=cur_movie[6],img_r=cur_movie[7],hd_link=cur_movie[8])
        m.save()