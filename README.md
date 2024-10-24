# Genre Diversity Plugin for Beets

This repository contains a Beets plugin that calculates and analyzes the genre diversity of your music library. The plugin provides insights into how diverse your music collection is, using metrics such as the Shannon and Simpson Diversity Indices.

## Features

- **Shannon Diversity Index**: Measures diversity by considering both the number of genres and their relative abundances.
- **Simpson Diversity Index**: Focuses on the probability that two randomly selected items belong to different genres.
- **Overall Genre Analysis**: Considers all genres assigned to tracks, providing a comprehensive view of total genre diversity.
- **Primary Genre Analysis**: Only considers the first genre assigned to each track, reflecting the main musical style.
- **Top 10 Genres**: Displays the most common genres in both overall and primary categories.
- **Distribution of Tracks by Number of Genres**: Shows how many tracks have one, two, or three assigned genres.
- **Implications for Your Library**: Provides insights into the diversity and potential areas for exploration within your collection.

## Installation

1. Ensure you have [Beets](https://beets.io/) installed on your system.
2. Clone this repository.
3. Place the genrediversity.py script in your Beets plugin directory or configure it in your beetsconfig.yaml.

## Usage
beet genrediversity

Works with single or comma seperated genres. If using another seperator just find and edit this line to suit  your needs -   
```primary_genres = [item.genre.split(',')[0] for item in genres if item.genre]```

## Example Output
About the Diversity Measures:
- Shannon Diversity Index: Measures diversity by considering both the number of genres and their relative abundances.
- Simpson Diversity Index: Focuses on the probability that two randomly selected items belong to different genres.

Difference Between Overall and Primary Genre Analysis:
- Overall Genre Analysis: Considers all genres assigned to tracks, providing a comprehensive view of total genre diversity.
- Primary Genre Analysis: Only considers the first genre assigned to each track, reflecting the main musical style.

Distribution of tracks by number of assigned genres:
- 1 genre: 2482 tracks
- 2 genres: 3123 tracks
- 3 genres: 15702 tracks

Overall Genre Analysis:
- Total genre entries: 21307
- Unique genres: 719
- Shannon Diversity Index: 5.0256
- Normalized Shannon Diversity Score: 0.7640
- Explanation (Shannon): High diversity. The library has a good spread across many genres.
- Simpson Diversity Index: 0.9751
 - Explanation (Simpson): Very high diversity. Genres are very evenly represented, with no clear dominant genres.

Top 10 Genres:
- Drum And Bass, Jungle, Electronic: 2042
- Electronic, Jazz, Rock: 2025
- Dub, Reggae, Roots Reggae: 863
- Reggae, Roots Reggae, Dub: 463
- Reggae, Roots Reggae: 463
- Dub, Reggae: 444
- Hip Hop, Rap: 429
- Britpop, Rock, Alternative Rock: 393
- Reggae: 368
- Dub, Reggae, Electronic: 320

Primary Genre Analysis:
- Total genre entries: 21307
- Unique genres: 127
- Shannon Diversity Index: 3.2467
- Normalized Shannon Diversity Score: 0.6702
- Explanation (Shannon): High diversity. The library has a good spread across many genres.
- Simpson Diversity Index: 0.9276
- Explanation (Simpson): Very high diversity. Genres are very evenly represented, with no clear dominant genres.

Top 10 Genres:
- Drum And Bass: 2859
- Electronic: 2763
- Reggae: 2692
- Dub: 2244
- Rap: 1139
- Hip Hop: 1044
- Soul: 583
- Rock: 554
- Britpop: 458
- House: 439

Implications for Your Beets Library:
1. High Overall Shannon Diversity: Your library has a wide variety of genres.
2. High Overall Simpson Diversity: Your library has a very even distribution of genres.
3. High Primary Genre Shannon Diversity: The main genres are well-distributed.
4. High Primary Genre Simpson Diversity: Your primary genres are very evenly distributed.
5. Extensive Use of Multi-Genre Tagging: Most tracks have multiple genres.

## Contributing
Feel free to submit issues or pull requests if you have suggestions for improvements or new features.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

