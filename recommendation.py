movies = {
    "Avengers": ["action", "superhero", "adventure"],
    "Inception": ["sci-fi", "thriller", "mind-bending"],
    "Interstellar": ["scifi", "space", "thriller"],
    "The Notebook": ["romance", "drama", "love"],
    "Titanic": ["romance", "drama", "tragedy"],
    "Toy Story": ["animation", "comedy", "family"],
    "Finding Nemo": ["animation", "family", "adventure"],
    "The Dark Knight": ["action", "superhero", "dc"],
    "Batman Begins": ["action", "superhero", "dc"],
    "Iron Man": ["action", "superhero", "marvel"]
}



def recommend_movies(liked_movie, movies):
    if liked_movie not in movies:
        return []
    
    liked_tags = movies[liked_movie]
    scores={}

    for movie, tags in movies.items():
        if movie == liked_movie:
            continue

        #count matching tags
        match_count = 0
        for tag in liked_tags:
            if tag in tags:
                match_count += 1

        if match_count > 0:
            scores[movie] = match_count

    #sort movies by score
    recommended = sorted(scores, key=scores.get, reverse=True)

    return recommended



# Add this at the end of your file

def main():
    print("=" * 40)
    print("   🎬 Movie Recommendation System")
    print("=" * 40)
    
    while True:
        print("\nAvailable Movies:")
        for i, movie in enumerate(movies, 1):
            print(f"  {i}. {movie}")
        
        print("\nOptions:")
        print("  1. Get recommendations")
        print("  2. Exit")
        
        choice = input("\nChoose option (1/2): ")
        
        if choice == "2":
            print("\nThank you for using Movie Recommender! 👋")
            break
        
        elif choice == "1":
            user_input = input("\nEnter movie name: ")
            recommendations = recommend_movies(
                user_input, movies)
            
            if recommendations:
                print(f"\n🎬 Because you liked {user_input}:")
                print("-" * 35)
                for i, movie in enumerate(
                        recommendations, 1):
                    tags = ", ".join(movies[movie])
                    print(f"{i}. {movie}")
                    print(f"   Genre: {tags}")
            else:
                print("❌ Movie not found! Check spelling.")
        else:
            print("Invalid option! Try again.")

# Replace your existing code at bottom with:
main()