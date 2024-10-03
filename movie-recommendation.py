movies = [
    # Romantic Comedies
    {"title": "When Harry Met Sally", "genre": "Rom-Com", "description": "Harry and Sally navigate the ups and downs of friendship and romance over several years.", "rating": None},
    {"title": "10 Things I Hate About You", "genre": "Rom-Com", "description": "A modern adaptation of Shakespeare's 'The Taming of the Shrew' set in a high school.", "rating": None},
    {"title": "Notting Hill", "genre": "Rom-Com", "description": "A chance encounter between a London bookseller and a famous actress leads to unexpected romance.", "rating": None},

    # Horror
    {"title": "Get Out", "genre": "Horror", "description": "A young Black man uncovers a disturbing secret when he meets his white girlfriend's family.", "rating": None},
    {"title": "The Shining", "genre": "Horror", "description": "A family heads to an isolated hotel where a sinister presence influences the father.", "rating": None},
    
    # Comedy
    {"title": "Superbad", "genre": "Comedy", "description": "Two high school friends navigate a wild night of partying and misadventures.", "rating": None},
    {"title": "Groundhog Day", "genre": "Comedy", "description": "A weatherman finds himself reliving the same day over and over again.", "rating": None},

    # Suspense
    {"title": "Se7en", "genre": "Suspense", "description": "Two detectives hunt for a serial killer who uses the seven deadly sins as motives.", "rating": None},
    {"title": "Gone Girl", "genre": "Suspense", "description": "A man's wife disappears, and he becomes the prime suspect in her disappearance.", "rating": None},

    # War
    {"title": "Saving Private Ryan", "genre": "War", "description": "During WWII, a group of soldiers sets out to find a paratrooper whose brothers have been killed in action.", "rating": None},
    {"title": "1917", "genre": "War", "description": "Two British soldiers must cross enemy lines to deliver a message that could save hundreds.", "rating": None},

    # Historical
    {"title": "Schindler's List", "genre": "Historical", "description": "The true story of Oskar Schindler, who saved over a thousand Polish Jews during the Holocaust.", "rating": None},
    {"title": "Gladiator", "genre": "Historical", "description": "A betrayed Roman general seeks revenge against the corrupt emperor who murdered his family.", "rating": None},

    # Others
    {"title": "Inception", "genre": "Sci-Fi", "description": "A thief who steals corporate secrets through dream-sharing technology.", "rating": None},
    {"title": "The Godfather", "genre": "Crime", "description": "An organized crime dynasty's aging patriarch transfers control of his clandestine empire to his reluctant son.", "rating": None},
    {"title": "The Dark Knight", "genre": "Action", "description": "When the menace known as the Joker emerges from his mysterious past, he wreaks havoc and chaos on the people of Gotham.", "rating": None},
]

def recommend_movies(query):
    recommendations = []
    for movie in movies:
        if query.lower() in movie["title"].lower() or query.lower() in movie["genre"].lower():
            recommendations.append(movie)
    return recommendations

def rate_movie(title, rating):
    for movie in movies:
        if movie["title"].lower() == title.lower():
            movie["rating"] = rating
            print(f"Rated '{title}' with {rating} stars.")
            return
    print("Movie not found.")

def main():
    print("Welcome to the Movie Recommendation Program!")
    while True:
        user_input = input("Enter a movie title or genre (or type 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        recommendations = recommend_movies(user_input)
        if recommendations:
            print("Here are some recommendations:")
            for movie in recommendations:
                rating = movie["rating"] if movie["rating"] is not None else "Not rated yet"
                print(f"- {movie['title']} ({movie['genre']}): {movie['description']} | Rating: {rating}")
            
            rate_input = input("Would you like to rate any of these movies? (yes/no): ")
            if rate_input.lower() == 'yes':
                title_to_rate = input("Enter the title of the movie you'd like to rate: ")
                rating_value = input("Enter your rating (1-5 stars): ")
                if rating_value.isdigit() and 1 <= int(rating_value) <= 5:
                    rate_movie(title_to_rate, int(rating_value))
                else:
                    print("Invalid rating. Please enter a number between 1 and 5.")
        else:
            print("No recommendations found.")

if __name__ == "__main__":
    main()