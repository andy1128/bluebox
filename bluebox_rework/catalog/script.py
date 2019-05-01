# import os
from  catalog.models import Movie

#TODO: change path
with open('C:/Users/Juan/Desktop/movies.txt') as movie_file:
    for line in movie_file:
        cur_movie = line.split(', ')
        cur_movie[9] = ''.join(('$', cur_movie[9]))
        cur_movie[10] = ''.join(('$', cur_movie[10]))
        cur_movie[8] = str(cur_movie[8].replace("\n", ""))
        cur_movie[2] = str(cur_movie[2].strip())
        cur_movie[3] = str(cur_movie[3].strip())
        print(line)
        m = Movie(title=cur_movie[0],year=cur_movie[1],director=cur_movie[2],actors=cur_movie[3],link=cur_movie[4],genre=cur_movie[5],img=cur_movie[6],img_r=cur_movie[7],hd_link=cur_movie[8], sd_price=cur_movie[9], hd_price=cur_movie[10])
        m.save()