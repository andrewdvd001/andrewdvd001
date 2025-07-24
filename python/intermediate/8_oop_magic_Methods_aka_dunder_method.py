class Movie:
    def __init__(self, title, genre, rating ):
        self.title = title
        self.genre = genre
        self.rating = rating
    
    def __str__(self):
        return f"Title: {self.title} | Genre: {self.genre} | Rating: {self.rating}/10"
    
    def __repr__(self):
        return f"Movie('{self.title}', '{self.genre}', {self.rating})"
    
    def __len__(self):
        return int(self.rating * 10)
    
m = Movie("Interstellar", "Sci-Fi", 8.6)
print(m)            # Title: Interstellar | Genre: Sci-Fi | Rating: 8.6/10
print(repr(m))      # Movie('Interstellar', 'Sci-Fi', 8.6)
print(len(m))       # 86
