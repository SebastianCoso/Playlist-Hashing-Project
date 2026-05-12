"""
Music Playlist Lookup System Using Hashing
CSCI 209 Final Project

This program demonstrates how hashing can be used to efficiently store
and retrieve music data. It compares hash-based search with linear search
to show differences in algorithm efficiency.
"""

# -----------------------------
# Dataset of Songs
# -----------------------------
songs = [
    {"title": "Blinding Lights", "artist": "The Weeknd", "album": "After Hours", "duration": 3.20},
    {"title": "Levitating", "artist": "Dua Lipa", "album": "Future Nostalgia", "duration": 3.23},
    {"title": "Lose Yourself", "artist": "Eminem", "album": "8 Mile", "duration": 5.20},
    {"title": "Shape of You", "artist": "Ed Sheeran", "album": "Divide", "duration": 4.24},
    {"title": "Rolling in the Deep", "artist": "Adele", "album": "21", "duration": 3.48}
]

# -----------------------------
# Hash Table (Dictionary)
# -----------------------------
# This dictionary represents a hash table where:
# key = song title (string)
# value = song data (dictionary)
hash_table = {}

# -----------------------------
# Function to Add Songs to Hash Table
# -----------------------------
def add_song(song):
    """
    Maps a song title to its song data using hashing.
    This demonstrates a function acting as a mapping.
    """
    key = song["title"].lower()
    hash_table[key] = song

# Load all songs into the hash table
for song in songs:
    add_song(song)

# -----------------------------
# Hash-Based Search
# -----------------------------
def hash_search(title):
    """
    Searches for a song using hashing.
    Average time complexity: O(1)
    """
    key = title.lower()

    if key in hash_table:
        # Compute an index value to demonstrate hashing
        index = hash(key) % len(hash_table)
        return hash_table[key], index

    return None, None

# -----------------------------
# Linear Search (Comparison)
# -----------------------------
def linear_search(title):
    """
    Searches for a song using linear search.
    Time complexity: O(n)
    """
    for index, song in enumerate(songs):
        if song["title"].lower() == title.lower():
            return song, index

    return None, None

# -----------------------------
# Main Program
# -----------------------------
def main():
    search_title = input("Enter a song title to search: ")

    song, hash_index = hash_search(search_title)
    if song:
        print("\nHash Search Result:")
        print(song)
        print("Hash Index:", hash_index)
    else:
        print("\nSong not found using hash search.")

    song, linear_index = linear_search(search_title)
    if song:
        print("\nLinear Search Result:")
        print(song)
        print("List Index:", linear_index)
    else:
        print("\nSong not found using linear search.")

# Run the program
main()
