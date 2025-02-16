# Dictionary of movies

movies = [
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

# def q(movie):
#     if movie["imdb"] >= 5.5:
#         return True
#     return False

# i = int(input())
# print(q(movies[i]))

# def im(q):
#     return [q for q in movies if q["imdb"] > 5.5]

# print(im(movies))

# def q(zhanr):
#     return [i for i in movies if i["category"] == zhanr]

# i = input()
# print(q(i))

# def avg(movies):
#     return sum(i["imdb"] for i in movies) / len(movies)

# print(avg(movies))

def cavg(zhanr):
    return sum(c["imdb"] for c in zhanr) / len(zhanr)
    
def cat(zhanr):
    return [i for i in movies if i["category"] == zhanr]

zhanr = input()
d = cat(zhanr)
print(cavg(d))