

movies =[
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

#ex 1
def imdb_5_5(movie):
    for movie in movies:
        if movie["imdb"] > 5.5:
            pass
    print("True")

imdb_5_5(movies)

#ex 2
good_movies = []
def find_movie(movie):
    for movie in movies:
        if movie["imdb"] > 5.5:
            good_movies.append(movie)

    print(good_movies)
    return 

find_movie(movies)

#ex 3

movie_category = []
def movies_in_category(category):
    for movie in movies:
        if movie["category"] == category:
            movie_category.append(movie)
    print(movie_category)
    return movie_category

movies_in_category("Romance")
       
# ex 4
all_scores = []
def average_imdb(movies):
    for movie in movies:
        all_scores.append(movie["imdb"])
        average = sum(all_scores) / len(movies)    
    print(average)

average_imdb(movies)

#ex 5
categories = []

def avarage_imdb_of_categorie(category):

    for movie in movies:
        if movie["category"] == category:
            categories.append(movie)
    imdb_scores = []
    for i in categories:
        imdb_scores.append(i["imdb"])
        avarage_imdb_score = sum(imdb_scores) / len(categories)

    print(avarage_imdb_score)
avarage_imdb_of_categorie("Romance")