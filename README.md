# Playlist Hashing Project

## Overview

This project is a that demonstrates how hashing can be used to store and retrieve music playlist data efficiently.

The program uses a Python dictionary as a hash table. Each song title is used as a key, and the song information is stored as the value. The user can search for a song by title, and the program compares a hash-based search with a traditional linear search.

## Project Purpose

The purpose of this project is to show the difference between hash-based searching and linear searching. Hashing allows data to be found quickly by using a key, while linear search checks each item one at a time.

This helps demonstrate why hash tables are useful for fast lookup operations.

## Features

- Stores a dataset of songs
- Uses a Python dictionary as a hash table
- Allows the user to search for a song by title
- Performs a hash-based search
- Performs a linear search for comparison
- Displays the song information if found
- Displays the hash index and list index
- Demonstrates basic algorithm efficiency

## Concepts Used

- Python dictionaries
- Hash tables
- Hashing
- Lists
- Functions
- User input
- Linear search
- Time complexity
- Algorithm comparison

## Time Complexity

### Hash Search

The hash-based search uses a Python dictionary. On average, dictionary lookup has a time complexity of:

```text
O(1)
