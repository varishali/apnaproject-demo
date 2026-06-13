class Movie:

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating


class MovieManager:

    def __init__(self):
        self.movies = []

    def add_movie(self, name, rating):

        movie = Movie(name, rating)

        self.movies.append(movie)

        print("Movie Added Successfully!")

    def view_movies(self):

        if len(self.movies) == 0:
            print("No Movies Found!")

        else:

            print("\nMovie Collection:")

            for movie in self.movies:

                print(
                    f"Movie: {movie.name} | Rating: {movie.rating}/10"
                )

    def search_movie(self, name):

        for movie in self.movies:

            if movie.name.lower() == name.lower():

                print(
                    f"Found: {movie.name} | Rating: {movie.rating}/10"
                )
                return

        print("Movie Not Found!")

    def top_rated(self):

        if len(self.movies) == 0:
            print("No Movies Found!")

        else:

            top = max(
                self.movies,
                key=lambda movie: movie.rating
            )

            print(
                f"Top Movie: {top.name} ({top.rating}/10)"
            )


manager = MovieManager()

while True:

    print("\n===== Movie Collection Manager =====")
    print("1. Add Movie")
    print("2. View Movies")
    print("3. Search Movie")
    print("4. Top Rated Movie")
    print("5. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":

        name = input("Movie Name: ")
        rating = float(input("Rating (1-10): "))

        manager.add_movie(name, rating)

    elif choice == "2":

        manager.view_movies()

    elif choice == "3":

        name = input("Search Movie: ")

        manager.search_movie(name)

    elif choice == "4":

        manager.top_rated()

    elif choice == "5":

        print("Thank You!")
        break

    else:

        print("Invalid Choice!")