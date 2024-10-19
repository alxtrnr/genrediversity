from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from collections import Counter
import math

class GenreDiversityPlugin(BeetsPlugin):

    def __init__(self):
        super(GenreDiversityPlugin, self).__init__()

    def commands(self):
        cmd = Subcommand('genrediversity', help='Calculate genre diversity of your library')
        cmd.func = self.calculate_diversity
        return [cmd]

    def calculate_diversity(self, lib, opts, args):
        try:
            # Print explanations of each index and analysis type
            print("About the Diversity Measures:")
            print("Shannon Diversity Index: Measures diversity by considering both the number of genres and their relative abundances.")
            print("Simpson Diversity Index: Focuses on the probability that two randomly selected items belong to different genres.\n")
            
            print("Difference Between Overall and Primary Genre Analysis:")
            print("Overall Genre Analysis: Considers all genres assigned to tracks, providing a comprehensive view of total genre diversity.")
            print("Primary Genre Analysis: Only considers the first genre assigned to each track, reflecting the main musical style.\n")

            # Fetch genres using Beets library
            genres = lib.items('genre:""')

            # Count occurrences of each genre
            all_genres = [item.genre for item in genres if item.genre]
            primary_genres = [item.genre.split(',')[0] for item in genres if item.genre]
            
            overall_counts = Counter(all_genres)
            primary_counts = Counter(primary_genres)

            # Calculate genre count distribution
            genre_count_distribution = Counter(len(item.genre.split(',')) for item in genres if item.genre)

            # Print distribution by number of assigned genres
            print("\nDistribution of tracks by number of assigned genres:")
            for count in sorted(genre_count_distribution.keys()):
                num_tracks = genre_count_distribution[count]
                plural = 'genres' if count > 1 else 'genre'
                print(f"{count} {plural}: {num_tracks} tracks")

            # Perform analysis
            self.print_analysis("Overall Genre", overall_counts)
            self.print_analysis("Primary Genre", primary_counts)
            
            overall_shannon, overall_simpson, _ = self.analyze_diversity(overall_counts)
            primary_shannon, primary_simpson, _ = self.analyze_diversity(primary_counts)

            self.print_implications(overall_shannon, overall_simpson, primary_shannon, primary_simpson, genre_count_distribution)

        except Exception as e:
            print(f"An error occurred during genre diversity calculation: {e}")

    def calculate_shannon_diversity(self, counts):
        try:
            total = sum(counts.values())
            shannon_diversity = 0
            for count in counts.values():
                p = count / total
                shannon_diversity -= p * math.log(p)
            return shannon_diversity
        except Exception as e:
            print(f"Error calculating Shannon Diversity: {e}")
            return 0

    def calculate_simpson_diversity(self, counts):
        try:
            total = sum(counts.values())
            simpson_diversity = 1 - sum((count/total)**2 for count in counts.values())
            return simpson_diversity
        except Exception as e:
            print(f"Error calculating Simpson Diversity: {e}")
            return 0

    def analyze_diversity(self, counts):
        shannon_diversity = self.calculate_shannon_diversity(counts)
        simpson_diversity = self.calculate_simpson_diversity(counts)
        max_shannon_diversity = math.log(len(counts))
        normalized_shannon_diversity = shannon_diversity / max_shannon_diversity if max_shannon_diversity > 0 else 0
        return shannon_diversity, simpson_diversity, normalized_shannon_diversity

    def explain_shannon_score(self, score):
        if score < 0.2:
            return "Very low diversity. The library is dominated by a few genres."
        elif score < 0.4:
            return "Low diversity. A small number of genres make up most of the library."
        elif score < 0.6:
            return "Moderate diversity. There's a mix of genres, but some dominate."
        elif score < 0.8:
            return "High diversity. The library has a good spread across many genres."
        else:
            return "Very high diversity. Genres are very evenly distributed across the library."

    def explain_simpson_score(self, score):
        if score < 0.2:
            return "Very low diversity. One or two genres heavily dominate the library."
        elif score < 0.4:
            return "Low diversity. A few genres make up the vast majority of the library."
        elif score < 0.6:
            return "Moderate diversity. There's a mix of genres, but some are significantly more common than others."
        elif score < 0.8:
            return "High diversity. The library has a good balance of genres with no single genre overly dominant."
        else:
            return "Very high diversity. Genres are very evenly represented, with no clear dominant genres."

    def print_analysis(self, category_name, counts):
        try:
            total = sum(counts.values())
            
            shannon_diversity, simpson_diversity, normalized_shannon_diversity = self.analyze_diversity(counts)

            print(f"\n{category_name} Analysis:")
            print(f"Total genre entries: {total}")
            print(f"Unique genres: {len(counts)}")
            
            print(f"Shannon Diversity Index: {shannon_diversity:.4f}")
            print(f"Normalized Shannon Diversity Score: {normalized_shannon_diversity:.4f}")
            
            print(f"Explanation (Shannon): {self.explain_shannon_score(normalized_shannon_diversity)}")
            
            print(f"Simpson Diversity Index: {simpson_diversity:.4f}")
            
            print(f"Explanation (Simpson): {self.explain_simpson_score(simpson_diversity)}")
            
            # Print top ten genres
            print("\nTop 10 Genres:")
            for genre, count in counts.most_common(10):
                print(f"{genre}: {count}")
        
        except Exception as e:
           print(f"Error during analysis for {category_name}: {e}")

    def print_implications(self, overall_shannon, overall_simpson, primary_shannon, primary_simpson, genre_count_distribution):
       try:
           # Print implications based on calculated indices
           print("\nImplications for Your Beets Library:")
           if overall_shannon > 0.7:
               print("1. High Overall Shannon Diversity: Your library has a wide variety of genres.")
           elif overall_shannon > 0.5:
               print("1. Moderate Overall Shannon Diversity: Your library has a good mix of genres.")
           else:
               print("1. Low Overall Shannon Diversity: Your library is dominated by a few genres.")

           if overall_simpson > 0.7:
               print("2. High Overall Simpson Diversity: Your library has a very even distribution of genres.")
           elif overall_simpson > 0.5:
               print("2. Moderate Overall Simpson Diversity: There's a good balance of genres.")
           else:
               print("2. Low Overall Simpson Diversity: A few genres dominate your library.")

           if primary_shannon > 0.7:
               print("3. High Primary Genre Shannon Diversity: The main genres are well-distributed.")
           elif primary_shannon > 0.5:
               print("3. Moderate Primary Genre Shannon Diversity: There's a good spread of main genres.")
           else:
               print("3. Low Primary Genre Shannon Diversity: A few primary genres dominate.")

           if primary_simpson > 0.7:
               print("4. High Primary Genre Simpson Diversity: Your primary genres are very evenly distributed.")
           elif primary_simpson > 0.5:
               print("4. Moderate Primary Genre Simpson Diversity: There's a good balance of primary genres.")
           else:
               print("4. Low Primary Genre Simpson Diversity: A few primary genres are much more common.")

           multi_genre_percentage = (genre_count_distribution[2] + genre_count_distribution[3]) / sum(genre_count_distribution.values()) * 100

           if multi_genre_percentage > 80:
               print("5. Extensive Use of Multi-Genre Tagging: Most tracks have multiple genres.")
           elif multi_genre_percentage > 50:
               print("5. Moderate Use of Multi-Genre Tagging: Many tracks have multiple genres.")
           else:
               print("5. Limited Use of Multi-Genre Tagging.")

       except Exception as e:
          print(f"Error printing implications or distribution: {e}")
